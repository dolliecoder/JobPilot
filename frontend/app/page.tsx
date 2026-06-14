export default function Home() {
  return (
    <div>
      <h2>Welcome to AI Job Application System</h2>
      <p>Get started by uploading your resume and exploring job opportunities.</p>
      
      <div style={{ marginTop: '2rem' }}>
        <h3>Quick Actions</h3>
        <ul>
          <li><a href="/upload">Upload Resume</a></li>
          <li><a href="/jobs">Browse Jobs</a></li>
          <li><a href="/applications">View Applications</a></li>
        </ul>
      </div>
    </div>
  )
}
