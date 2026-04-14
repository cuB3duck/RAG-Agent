from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_community.document_loaders import PyPDFium2Loader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

# Directory to save uploaded pdfs.
uploads = "./uploads"

# Creates uploads directory if not exist.
os.makedirs(uploads, exist_ok=True)

# Instantiate model object using embedding model pulled from Ollama.
embeddings = OllamaEmbeddings(model = "nomic-embed-text")

# Initialize Chroma Vector Store.
vector_store = Chroma(
    collection_name = "medical_information",
    embedding_function = embeddings,
)

# Initialize splitter. Have overlap so meaning is kept.
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=150
)

# Retriver finds the top 5 similar chunks in the vector store.
retriever = vector_store.as_retriever(search_kwargs={"k": 5})

# Chunks all pdfs that were uploaded.
def add_pdfs(files):
    # Create a list for all the documents.
    list_docs = []

    # Loop through added pdfs.
    for file in files:
        # Save upload to uploads directory.
        add_path = os.path.join(uploads, file.filename)
        file.save(add_path)

        # Add each pdf to the list of documents.
        loader = PyPDFium2Loader(add_path)
        docs = loader.load()
        list_docs.extend(docs)

    # Split documents and add to vector store.
    chunks = splitter.split_documents(list_docs)
    vector_store.add_documents(chunks, batch_size=64)

    return len(chunks)