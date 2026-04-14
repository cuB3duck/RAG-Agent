import { useState } from "react";

export default function FileUpload() {
  // Manage state for list of files.
  const [files, setFiles] = useState([]);

  // Updates the list of pdfs. Adds a new pdf to existing list of files.
  const handleUpload = (e) => {
    // Convert file list to an array. Combine the arrays for the previous list of files and added files.
    const selectedFiles = Array.from(e.target.files);
    setFiles((prev) => [...prev, ...selectedFiles]);
  };

  // Removing a pdf from the list of pdfs.
  const deleteFile = async (index) => {
    const fileToDelete = files[index];

    // Remove from UI.
    setFiles((prev) => prev.filter((_, i) => i !== index));

    try {
      await fetch("http://localhost:5000/delete", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ filename: fileToDelete.name }),
      });
    } catch (error) {
      console.error("Error deleting file:", error);
    }
  };

  // Send all pdfs to the backend.
  const uploadFiles = async () => {
    try {      
      // Add each file to the FormData object.
      const formData = new FormData();
      files.forEach((file) => formData.append("file", file));

      const response = await fetch("http://localhost:5000/upload", {
        method: "POST",
        body: formData,
      });

      // Convert response into JSON.
      const data = await response.json();
      console.log("Server response:", data);
    
    } catch (error) {
      console.error("Error uploading files:", error);
    }
  };

  return (
  <div>
      <h2>Upload PDF Files</h2>
      <input
        type="file"
        accept="application/pdf"
        multiple
        onChange={handleUpload}
      />
        {files.map((file, index) => (
          <li key={index}
          className="file-list">
            {file.name}
            <button
              onClick={() => deleteFile(index)}
              className="delete-button"
            >
              Delete
            </button>
          </li>
        ))}
      <button onClick={uploadFiles}
      className="final-upload-button"
      >
    Upload</button>
    </div>
  );
}
