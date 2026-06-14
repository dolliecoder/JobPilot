'use client'

import { useState } from 'react'

interface JobSearchProps {
  onSearch: (keyword: string) => void
}

export default function JobSearch({ onSearch }: JobSearchProps) {
  const [keyword, setKeyword] = useState('')

  const handleSearch = () => {
    onSearch(keyword)
  }

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter') {
      handleSearch()
    }
  }

  const handleClear = () => {
    setKeyword('')
    onSearch('')
  }

  return (
    <div style={{ marginBottom: '2rem' }}>
      <input 
        type="text" 
        placeholder="Search by title, company, location, or job type..." 
        value={keyword}
        onChange={(e) => setKeyword(e.target.value)}
        onKeyPress={handleKeyPress}
        style={{ 
          padding: '0.75rem', 
          width: '400px', 
          marginRight: '1rem',
          border: '1px solid #ccc',
          borderRadius: '4px',
          fontSize: '1rem'
        }}
      />
      <button 
        onClick={handleSearch}
        style={{
          padding: '0.75rem 1.5rem',
          backgroundColor: '#0070f3',
          color: 'white',
          border: 'none',
          borderRadius: '4px',
          cursor: 'pointer',
          fontSize: '1rem',
          marginRight: '0.5rem'
        }}
      >
        Search
      </button>
      {keyword && (
        <button 
          onClick={handleClear}
          style={{
            padding: '0.75rem 1.5rem',
            backgroundColor: '#666',
            color: 'white',
            border: 'none',
            borderRadius: '4px',
            cursor: 'pointer',
            fontSize: '1rem'
          }}
        >
          Clear
        </button>
      )}
    </div>
  )
}
