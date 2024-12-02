// src/components/JobItem.js
import React from 'react';

function JobItem({ job }) {
  return (
    <div className="job-item" style={styles.jobItem}>
      <h3>{job.job_title}</h3>
      <a href={job.job_url} target="_blank" rel="noopener noreferrer">View Job</a>
    </div>
  );
}

const styles = {
  jobItem: {
    backgroundColor: 'white',
    padding: '10px',
    margin: '10px',
    borderRadius: '5px',
    boxShadow: '0px 4px 6px rgba(0, 0, 0, 0.1)',
  },
};

export default JobItem;
