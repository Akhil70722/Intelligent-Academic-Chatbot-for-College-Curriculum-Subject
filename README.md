# Intelligent-Academic-Chatbot-for-College-Curriculum-Subject
## Document Analysis and Conversational Agent

This project implements a document analysis system using language models and vector-based search. It enables users to upload documents (PDF, DOCX, TXT) and interact with a conversational agent to ask questions based on the content of the documents. The system processes documents, generates embeddings, and provides relevant responses to user queries.

## Features

- **Document Upload**: Supports various document formats such as PDF, DOCX, and TXT.
- **Document Processing**: Extracts content from the documents and splits it into manageable chunks for efficient querying.
- **Conversational AI**: Uses a Groq-powered LLM (Large Language Model) for conversational retrieval-based Q&A.
- **FAISS Vector Store**: Utilizes FAISS for fast similarity search, powered by embeddings created using HuggingFace models.
- **Memory**: The conversational agent remembers the user's query history to provide context for ongoing conversations.

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
