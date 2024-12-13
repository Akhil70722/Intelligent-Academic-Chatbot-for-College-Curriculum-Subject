# Intelligent-Academic-Chatbot-for-College-Curriculum-Subject
## Document Analysis and Conversational Agent

The Intelligent Academic Chatbot is a cutting-edge system designed to enhance academic learning and exploration. It allows students and educators to upload educational documents in formats like PDF, DOCX, and TXT. By leveraging advanced language models and vector-based search techniques, the chatbot can analyze the contents of these documents, extract key information, and provide context-aware responses to any queries related to the documents.

The system offers a seamless interaction where users can ask subject-specific questions and get precise answers derived from the uploaded materials. This makes it an invaluable tool for studying, exam preparation, and revisiting lecture notes. The core functionalities include document processing, embeddings generation, and querying via a conversational AI interface, providing an interactive and personalized academic assistant.

## Project Features

1. **Document Upload and Management**:
   - Supports common document formats: PDF, DOCX, and TXT.
   - Allows multiple document uploads for comprehensive analysis.

2. **Automated Document Processing**:
   - Extracts textual content from uploaded documents.
   - Breaks content into smaller, manageable chunks for efficient querying.
   - Handles complex documents with headings, tables, and bullet points.

3. **Conversational AI**:
   - Employs a **Groq-powered Large Language Model (LLM)** for intelligent question-answering.
   - Provides precise and contextually relevant answers.
   - Retains the history of queries for ongoing conversational context.

4. **FAISS Vector Store Integration**:
   - Uses **FAISS (Facebook AI Similarity Search)** to index document embeddings and retrieve the most relevant information.
   - Leverages **HuggingFace models** for creating robust embeddings.

5. **Persistent Query Memory**:
   - Maintains conversational flow by remembering previous interactions.
   - Enhances user experience by providing continuity across multiple queries.

6. **Scalability and Customization**:
   - Easily extendable for additional features such as summarization or translation.
   - Suitable for a wide range of academic subjects and document types.

## Prerequisites

- Python 3.x
- Groq API Key (required for interacting with the ChatGroq model)
- Environment variables configured using a `.env` file

## Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/yourusername/document-analysis-agent.git
    cd document-analysis-agent
    ```

2. **Install Dependencies**:

    You can install the required Python dependencies using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

    Alternatively, if you're using a virtual environment, make sure to activate it first before installing dependencies.

3. **Set Up the Environment**:

    - Create a `.env` file in the root of the project directory.
    - Add your `GROQ_API_KEY` to the `.env` file:

    ```
    GROQ_API_KEY=your_groq_api_key_here
    ```

    Make sure not to commit this `.env` file to your GitHub repository.

## Usage

1. **Processing Documents**:

    - Place the documents (PDF, DOCX, TXT) in the `./documents` directory (or any directory of your choice).
    - Run the `ingest.py` script to process the documents and generate the vector store.

    ```bash
    python ingest.py
    ```

    This will load the documents, extract text, split them into chunks, generate embeddings, and store them in a FAISS vector store.

2. **Interacting with the Conversational Agent**:

    - After the vector store is created, you can interact with the conversational agent by running the following script:

    ```bash
    python chat.py
    ```

    The agent will load the vector store, and you can start asking questions related to the documents you've processed.

## .gitignore

This project uses a `.gitignore` file to exclude files and directories that should not be tracked by Git, such as:

- `.env` file containing sensitive information (e.g., API keys).
- Virtual environment folders (`env/`, `venv/`).
- Compiled Python files (`*.pyc`, `__pycache__/`).
- Pickle files (`*.pkl`) used for storing the vector store.

## Contributing

Contributions are welcome! If you'd like to contribute to this project:

1. Fork the repository.
2. Create a new branch.
3. Make your changes and test them.
4. Create a pull request with a detailed description of your changes.
