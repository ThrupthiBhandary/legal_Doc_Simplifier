import { useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [simplified, setSimplified] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
    setSimplified("");
    setError("");
  };

  const handleUpload = async () => {
    if (!file) {
      setError("Please select a PDF file first");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);
      const res = await axios.post("http://127.0.0.1:5000/simplify", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      setSimplified(res.data.simplified_text);
      setLoading(false);
    } catch (err) {
      setError(err.response?.data?.error || "Something went wrong");
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100 p-4">
      <h1 className="text-3xl font-bold mb-4">Legal Document Simplifier</h1>

      <input
        type="file"
        accept="application/pdf"
        onChange={handleFileChange}
        className="mb-4 p-2 border rounded"
      />

      <button
        onClick={handleUpload}
        className="mb-4 px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
      >
        {loading ? "Processing..." : "Upload & Simplify"}
      </button>

      {error && <p className="text-red-500">{error}</p>}

      {simplified && (
        <div className="mt-4 p-4 w-full max-w-xl bg-white rounded shadow">
          <h2 className="font-semibold mb-2">Simplified Text:</h2>
          <p>{simplified}</p>
        </div>
      )}
    </div>
  );
}

export default App;
