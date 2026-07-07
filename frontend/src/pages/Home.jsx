import { useState } from "react";
import api from "../services/api";
import "./Home.css";

function Home() {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const [question, setQuestion] = useState("");
  const [chatAnswer, setChatAnswer] = useState("");
  const [chatLoading, setChatLoading] = useState(false);
  const statusEmoji = {
  Normal: "🟢",
  High: "🔴",
  Low: "🟠",
  Unknown: "⚪",
};
  const normalCount =
  result?.parameters.filter(p => p.status === "Normal").length || 0;

  const highCount =
  result?.parameters.filter(p => p.status === "High").length || 0;

  const lowCount =
  result?.parameters.filter(p => p.status === "Low").length || 0;

  const unknownCount =
  result?.parameters.filter(p => p.status === "Unknown").length || 0;
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

      console.log(response.data);

      setResult(response.data);

    } catch (error) {

      console.error(error);

      if (error.response) {
        console.log(error.response.data);
      }

      alert("Analysis failed.");

    } finally {

      setLoading(false);

    }
  };

  const askQuestion = async () => {

    if (!question.trim()) {
      alert("Please enter a question.");
      return;
    }

    try {

      setChatLoading(true);

      const response = await api.post(
        "/report-chat",
        {
          question: question
        }
      );

      setChatAnswer(response.data.answer);

    } catch (error) {

      console.error(error);

      alert("Unable to get answer.");

    } finally {

      setChatLoading(false);

    }
  };

  return (

    <div className="home">

      <div className="hero">

    <div className="logo">
        🩺
    </div>

    <h1>MediMind AI</h1>

    <p>
        AI-Powered Clinical Decision Support Platform
    </p>

    <div className="hero-tags">

        <span>📄 CBC</span>

        <span>🧪 LFT</span>

        <span>🤖 AI Analysis</span>

        <span>💬 Report Chat</span>

    </div>

</div>

      <div className="upload-card">

        <h2>Upload Laboratory Report</h2>

<p className="upload-text">

Upload a CBC or Liver Function Test report in PDF format.
Our AI will extract medical parameters, compare them against
reference ranges and generate an easy-to-understand summary.

</p>
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

          <h2>Medical Report Summary</h2>
          <div className="stats">

        <div className="stat-card">
        <h3>🟢</h3>
        <p>Normal</p>
        <span>{normalCount}</span>
        </div>

  <div className="stat-card">
    <h3>🔴</h3>
    <p>High</p>
    <span>{highCount}</span>
  </div>

  <div className="stat-card">
    <h3>🟠</h3>
    <p>Low</p>
    <span>{lowCount}</span>
  </div>

  <div className="stat-card">
    <h3>⚪</h3>
    <p>Unknown</p>
    <span>{unknownCount}</span>
  </div>

</div>

          <p>

            <strong>Report Type:</strong>{" "}

            {result.report_type}

          </p>

          <br />

          <p className="summary">

            {result.overall_summary}

          </p>

          <br />

          <h3>Extracted Parameters</h3>

          <table className="result-table">

            <thead>

              <tr>

                <th>Parameter</th>

                <th>Value</th>

                <th>Reference</th>

                <th>Status</th>

              </tr>

            </thead>

            <tbody>

              {result.parameters.map((item, index) => (

                <tr key={index}>

                  <td>{item.parameter}</td>

                  <td>

                    {item.value} {item.unit}

                  </td>

                  <td>

                    {item.reference_range ?? "-"}

                  </td>

                  <td>

                    <span
                      className={`status ${item.status.toLowerCase()}`}
                    >

                      {statusEmoji[item.status] && `${statusEmoji[item.status]} ${item.status}`}

                    </span>

                  </td>

                </tr>

              ))}

            </tbody>

          </table>

        </div>

      )}

      {result && (

        <div className="upload-card">

          <h2>Ask Questions About Your Report</h2>

          <textarea

            rows="4"

            placeholder="Example: Are my liver enzymes normal?"

            value={question}

            onChange={(e) => setQuestion(e.target.value)}

          />

          <button

            onClick={askQuestion}

            disabled={chatLoading}

          >

            {chatLoading ? "Thinking..." : "Ask AI"}

          </button>

          {chatAnswer && (

            <div className="answer-card">

              <h3>AI Answer</h3>

              <p>{chatAnswer}</p>

            </div>

          )}

        </div>

      )}

    </div>

  );
}

export default Home;