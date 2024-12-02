// src/components/JobList.js
import React from 'react';
import JobItem from './JobItem';

function JobList({ jobs }) {
  return (
    <div className="job-list" style={styles.jobList}>
      {jobs.map(job => (
        <JobItem key={job.job_url} job={job} />
      ))}
    </div>
  );
}

const styles = {
  jobList: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
  },
};

export default JobList;
