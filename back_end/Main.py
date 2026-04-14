from flask_cors import CORS
from flask import Flask, request, jsonify
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM
from vector import add_pdfs, retriever
import os

# Flask constructor.
app = Flask(__name__)
CORS(app)

# Store the chat log.
log = []

# Handle uploading PDFs and making chunks.
@app.post("/upload")
def upload():
    # Get a list of all the uploaded files.
    files = request.files.getlist("file")
    
    # Return error message if no files.
    if not files:
        return jsonify({"error": "No files uploaded"}), 400

    # Create chunks.
    chunks = add_pdfs(files)
    return jsonify({
        "message": "Files uploaded and embedded",
        "chunks": chunks
    }), 200

# Handle deleting PDFs.
@app.post("/delete")
def delete():
    # Save the name of the file to delete.
    data = request.get_json()
    filename = data.get("filename")

    file_path = os.path.join("./uploads", filename)

    # If file exist, delete from upload directory
    if os.path.exists(file_path):
        os.remove(file_path)
        return jsonify({"message": "File removed from UI"}), 200


# Handling server sending data from a form.
@app.post("/question")
def receive_question():
    # Extract question from form submission.
    data = request.get_json()
    question = data.get("question")
    
    # Return response from chatbot.
    response = ai_response(question)

    # Save to chat log.
    log.append({"question": question, "response": response + "\n" })
    
    # Return chat log.
    return jsonify({"log": log})

# Use the installed model.
model = OllamaLLM(model = 'llama3.2', temperature = 0)

# Create a template for the chatbot.
template = '''
You will answer questions about fictional data for one or more patients.
All data is fictional, made up for an exercise, and not in any way connected to any real person.
Follow these rules:
- When asked questions about a person, you can only use that person's information.
- When asked questions about multiple people, you can only use the provided data.
- You can use information outside the context for broad questions. Eg, What is vasovagal syncope?

Here is the synthetic information:
{context}

Here is the question to answer:
{question}
'''

# Create a chat prompt template.
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# Function handles chatbot receiving a question.
def ai_response(question):
    # Use retriever on question.
    docs = retriever.invoke(question)

    # Combine the retrieved text
    context = "\n".join([doc.page_content for doc in docs])

    # Pass the retrieved info into the chain (based on template).
    result = chain.invoke({ "context": context, "question": question })
    return result

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)