import os
import pickle
import streamlit as st
from langchain_groq import ChatGroq
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate

# Load the vector store
try:
    with open('vector_store.pkl', 'rb') as f:
        vector_store = pickle.load(f)
except FileNotFoundError:
    vector_store = None
    st.error("Vector store not found. Please run the ingestion script to generate it.")

# Create a prompt template
template = """
You are an assistant specialized in Computer Organization and Architecture. The user will provide questions based on this subject.

If the question is related to COA, respond with:
---
Please answer the following question using the context provided:

Context: {context}

Question: {question}

Answer in a concise and informative manner.
Try to answer in bullet points.
---

If the question is outside the topic of Computer Organization and Architecture, respond with:
---
I'm specialized in answering questions about Computer Organization and Architecture. Could you please ask a question related to this topic?
---
"""
prompt = PromptTemplate(input_variables=["context", "question"], template=template)

# Function to create the conversational chain
def create_conversational_chain(vector_store):
    groq_api_key = "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"
    model = 'mixtral-8x7b-32768'
    
    llm = ChatGroq(groq_api_key=groq_api_key, model_name=model)
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    chain = ConversationalRetrievalChain.from_llm(
        llm=llm, 
        chain_type='stuff',
        retriever=vector_store.as_retriever(search_kwargs={"k": 2}),
        memory=memory
    )
    return chain

# Create the conversation chain
conversation_chain = create_conversational_chain(vector_store) if vector_store else None

# Function to handle a user query
def handle_query(query, history):
    if conversation_chain is None:
        st.error("No documents processed. Please run the ingestion script first.")
        return "Error: Vector store not initialized."
    
    # Retrieve relevant context from the retriever
    context = conversation_chain.retriever.get_relevant_documents(query)

    # Format the input with the context using the prompt template
    formatted_prompt = prompt.format(context=context, question=query)

    # Pass the formatted prompt to the LLM within the chain
    result = conversation_chain({"question": formatted_prompt, "chat_history": history})

    # Append to the conversation history
    history.append((query, result["answer"]))

    return result["answer"]

# Streamlit app interface
st.title("Computer Organization and Architecture Chatbot")
st.write("Ask questions based on the Computer Organization and Architecture subject.")

# Session state for conversation history
if 'history' not in st.session_state:
    st.session_state.history = []

# User input for questions
user_query = st.text_input("Enter your question:")

if st.button("Submit"):
    if user_query:
        answer = handle_query(user_query, st.session_state.history)
        st.session_state.history.append((user_query, answer))
        st.write("**Answer:**", answer)
    else:
        st.warning("Please enter a question.")

# Display conversation history
st.write("### Conversation History")
for q, a in st.session_state.history:
    st.write(f"**Q:** {q}")
    st.write(f"**A:** {a}")

# Clear conversation button
if st.button("Clear Conversation"):
    st.session_state.history = []
    st.success("Conversation history cleared.")

# Feedback mechanism
st.write("### Feedback")
feedback = st.radio("Was the response helpful?", ["Yes", "No"], index=0)
if feedback == "No":
    st.text_area("What can be improved?", placeholder="Share your feedback here.")

# Quiz section
st.write("### Quiz Section")
quiz_question = "What is the role of the ALU in the CPU?"
if st.button("Show Quiz Question"):
    st.write("**Quiz Question:**", quiz_question)
