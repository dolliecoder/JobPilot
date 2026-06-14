'use client'

export default function ResumeUpload() {
  return (
    <div style={{ border: '2px dashed #ccc', padding: '2rem', textAlign: 'center' }}>
      <p>Resume upload component</p>
      <input type="file" accept=".pdf,.doc,.docx" />
      <button style={{ marginLeft: '1rem' }}>Upload</button>
    </div>
  )
}
