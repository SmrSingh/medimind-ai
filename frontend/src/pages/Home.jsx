import { useState } from "react";
import api from "../services/api";
import "./Home.css";

function Home() {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const analyzeReport = async () => {
    if (!file) {
      alert("Please select a PDF report.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);

     const response = await api.post(
        "/report-analysis",
        formData
    );

    console.log("Backend Response:");
    console.log(response);
    console.log(response.data);

    setResult(response.data);
    } catch (error) {
        console.error("Axios Error:", error);

    if (error.response) {
        console.log(error.response.data);
        console.log(error.response.status);
    }

    alert(error.message);
    }
  };

  return (
    <div className="home">

      <div className="hero">
        <h1>MediMind AI</h1>
        <p>AI-powered Medical Report Analysis</p>
      </div>

      <div className="upload-card">

        <h2>Upload Medical Report</h2>

        <input
          type="file"
          accept=".pdf"
          onChange={(e) => setFile(e.target.files[0])}
        />

        <button
          onClick={analyzeReport}
          disabled={loading}
        >
          {loading ? "Analyzing..." : "Analyze Report"}
        </button>

      </div>

      {result && (
        <div className="upload-card">

          <h2>Analysis Result</h2>

          <p>
            <strong>Report Type:</strong>{" "}
            {result.report_type}
          </p>

          <br />

          <p>{result.overall_summary}</p>

        </div>
      )}

    </div>
  );
}

export default Home;