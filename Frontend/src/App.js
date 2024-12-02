import React, { useState } from "react";
import axios from "axios";
import './App.css';  // Import the CSS file for styling

const App = () => {
  const [jobs, setJobs] = useState([]);
  const [keyword, setKeyword] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const keywords = [
    "software-engineer", "engineering-manager", "artificial-intelligence-engineer",
    "machine-learning-engineer", "product-manager", "backend-engineer",
    "mobile-engineer", "product-designer", "frontend-engineer",
    "full-stack-engineer", "data-scientist", "designer",
    "software-architect", "devops-engineer"
  ];

  const fetchJobs = async () => {
    try {
      setLoading(true);
      setError(null);
      const response = await axios.get(`http://127.0.0.1:5000/scrape?keyword=${keyword}`);
      
      const fetchedJobs = response.data;
      if (Array.isArray(fetchedJobs)) {
        setJobs(fetchedJobs);
      } else {
        setJobs([]);
      }
    } catch (error) {
      setError("Error fetching job listings. Please try again later.");
      console.error("Error fetching jobs:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>Job Scraper</h1>
      <div className="form-container">
        <select
          className="dropdown"
          value={keyword}
          onChange={(e) => setKeyword(e.target.value)}
        >
          <option value="" disabled>Select a keyword</option>
          {keywords.map((key) => (
            <option key={key} value={key}>
              {key.replace("-", " ")}
            </option>
          ))}
        </select>
        <button
          className="search-btn"
          onClick={fetchJobs}
          disabled={!keyword || loading}
        >
          {loading ? "Loading..." : "Search Jobs"}
        </button>
      </div>
      
      {loading && <p className="loading-text">Loading job listings...</p>}
      {error && <p className="error-text">{error}</p>}
      {jobs.length === 0 && !loading && !error && <p>No jobs found.</p>}
      
      <table className="job-table">
        <thead>
          <tr>
            <th>Company</th>
            <th>Job Title</th>
            <th>Job URL</th>
          </tr>
        </thead>
        <tbody>
          {jobs.map((company, index) => (
            company.Job_openings.map((job, jobIndex) => (
              <tr key={`${index}-${jobIndex}`}>
                <td>
                  <a href={company.company_url} target="_blank" rel="noopener noreferrer" className="company-link">
                    {company.company_name}
                  </a>
                  <br />
                  <small className="company-slogan">{company.company_slogan}</small>
                </td>
                <td>{job.job_title}</td>
                <td>
                  <a href={job.job_url} target="_blank" rel="noopener noreferrer" className="job-link">
                    View Job
                  </a>
                </td>
              </tr>
            ))
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default App;
