# Personal-Data-Assistant

Local AI agent uses RAG to answers questions about medical document pdfs.
<br>The LLM uses semantic search to retrieve data to answer questions.  
The model is deployed locally to protect sensitive information.  
Ollama runs the **llama3.2** model and **nomic-embed-text** model is used for embeddings.  
LangChain is the open source framework used for tasks such as making the prompt template.  
LangChain's Chroma stores and retrieves text embeddings.

## Installation

1. **Install requirements in the back_end directory.**
   ```bash
   pip install -r .\requirements.txt
2. **Install these in terminal.**
   ```bash
   ollama pull llama3.2
   ollama pull nomic-embed-text
3. **Run this while in the directory for each docker file**

   Docker file in the front end
      ```bash
      docker build -t front .
      ```
   Docker file in the back end
      ```bash
      docker build -t back .
      ```

4.  **Use these commands for the yml file.**

   When making changes to the code use
      ```bash
      docker compose down
      ```
   When running the program use
      ```bash
      docker compose up --build
      ```
