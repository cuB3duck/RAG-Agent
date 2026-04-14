# Personal-Data-Assistant

Local AI agent uses RAG to answers questions about a personal information dataset.
<br>The LLM uses semantic search to retrieve data to answer questions.  
The model is deployed locally to protect sensitive information.  
Ollama runs the **llama3.2** model and **nomic-embed-text** model is used for embeddings.  
LangChain is the open source framework used for tasks such as making the prompt template.  
LangChain's Chroma stores and retrieves text embeddings.

## Installation

1. **Create a virtual environment**
   ```bash
   python -m venv venv
2. **Activate the virtual environment**
   ```bash
   .\venv\Scripts\activate
3. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
4. **Install required Ollama models**
   ```bash
   ollama pull llama3.2
   ollama pull nomic-embed-text


## Dataset Setup
Personal information is stored in a CSV file and loaded as a Pandas DataFrame.
<br>The expected columns are Name, DOB, and SSN.
<br>The agent requires a CSV file.

##  Running the Agent
``` bash
python main.py
```

Question:  
"When was John Doe born?"

Answer:  
"John Doe was born 8/1/2001."

