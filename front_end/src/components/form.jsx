import { useState } from 'react';

// Create a component for the form.
function MyForm() {

  // Manage state for question and chat log.
  const [question, setQuestion] = useState('');
  const [log, setLog] = useState([]);

  // Prevent page reload and state clearing.
  const handleSubmit = async (e) => {
    e.preventDefault();

    // Fetch data from backend.
    try {
      const response = await fetch('http://localhost:5000/question', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ question })
      });

      // Convert response into JSON.
      const data = await response.json();
      console.log("Backend response:", data);

      // Update chat log.
      setLog(data.log);
      // Clear placeholder.
      setQuestion('');

    } catch (error) {
      console.error("Error sending question:", error);
    }
  };

  return (
    <>
      <div className="chat-container">
        <h3 className="chat-title">Chat History</h3>
        <div className="chat-box">
          {log.map((entry, index) => (
            <div key={index} className="chat-entry">
              <div className="chat-user">
                <strong>User:</strong> {entry.question}
              </div>
              <div className="chat-ai">
                <strong>AI:</strong> {entry.response}
              </div>
            </div>
          ))}
        </div>

        <form onSubmit={handleSubmit} className="chat-form">
          <input
            type="text"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            placeholder="Ask something..."
            className="chat-input"
          />
          <button type="submit" className="chat-button">
            Send
          </button>
        </form>
      </div>
    </>
  );
}

export default MyForm;
