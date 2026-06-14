'use client'

export default function JobSearch() {
  return (
    <div style={{ marginBottom: '2rem' }}>
      <input 
        type="text" 
        placeholder="Search jobs..." 
        style={{ padding: '0.5rem', width: '300px', marginRight: '1rem' }}
      />
      <button>Search</button>
    </div>
  )
}
