import os
import pickle
from langchain_groq import ChatGroq
from langchain.chains import ConversationalRetrievalChain
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.document_loaders import PyPDFLoader, TextLoader, Docx2txtLoader
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Prompt template definition
template = """
You are an assistant specialized in analyzing documents. The user will provide questions based on a document.
Please answer the following question using the context provided:

Context: {context}

Question: {question}

Answer in a concise and informative manner.
Try to answer in bullet points.
"""

# Function to create the conversational chain
def create_conversational_chain(vector_store):
    groq_api_key = os.getenv("GROQ_API_KEY")  # Securely fetch API key from .env
    model = "mixtral-8x7b-32768"

    if not groq_api_key:
        raise ValueError("GROQ API key is missing. Please set it in the .env file.")

    llm = ChatGroq(groq_api_key=groq_api_key, model_name=model)
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        chain_type="stuff",
        retriever=vector_store.as_retriever(search_kwargs={"k": 2}),
        memory=memory
    )
    return chain

# Function to process documents in a specified directory
def process_documents(directory):
    text = []

    # Validate if directory exists
    if not os.path.exists(directory):
        raise FileNotFoundError(f"The directory '{directory}' does not exist.")

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        file_extension = os.path.splitext(filename)[1].lower()

        loader = None
        if file_extension == ".pdf":
            loader = PyPDFLoader(file_path)
        elif file_extension in [".docx", ".doc"]:
            loader = Docx2txtLoader(file_path)
        elif file_extension == ".txt":
            loader = TextLoader(file_path)
        else:
            print(f"Skipping unsupported file type: {filename}")

        if loader:
            try:
                documents = loader.load()
                text.extend(documents)
                print(f"Loaded {filename} successfully.")
            except Exception as e:
                print(f"Error loading {filename}: {e}")

    # Split documents into manageable chunks
    text_splitter = CharacterTextSplitter(
        separator="\n", chunk_size=1000, chunk_overlap=100, length_function=len
    )
    text_chunks = text_splitter.split_documents(text)

    # Create embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"}
    )

    # Create vector store
    vector_store = FAISS.from_documents(text_chunks, embedding=embeddings)
    print("Vector store created successfully.")

    return vector_store

# Main entry point for the ingestion script
if __name__ == "__main__":
    # Specify the directory containing documents
    documents_directory = "./documents"  # Update this path as needed

    try:
        # Process the documents
        vector_store = process_documents(documents_directory)

        # Save the vector store for later use
        with open("vector_store.pkl", "wb") as f:
            pickle.dump(vector_store, f)
            print("Vector store saved successfully to 'vector_store.pkl'.")
    
    except Exception as e:
        print(f"An error occurred: {e}")