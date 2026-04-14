import MyForm from './components/form';
import FileUpload from './components/add_pdf';
import './App.css';

function App() {
  return (
    <>
      <p className="welcome">Welcome! Ask the AI chatbot anything about patient information. First upload a pdf. File names must be unique.</p>
      <FileUpload/>
      <MyForm/>
    </>
  );
}

export default App;
