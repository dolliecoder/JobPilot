import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'AI Job Application System',
  description: 'Manage your job applications with AI-powered matching',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>
        <header style={{ padding: '1rem', borderBottom: '1px solid #ccc' }}>
          <h1>AI Job Application System</h1>
          <nav>
            <a href="/" style={{ marginRight: '1rem' }}>Home</a>
            <a href="/upload" style={{ marginRight: '1rem' }}>Upload Resume</a>
            <a href="/jobs" style={{ marginRight: '1rem' }}>Jobs</a>
            <a href="/applications">Applications</a>
          </nav>
        </header>
        <main style={{ padding: '2rem' }}>
          {children}
        </main>
      </body>
    </html>
  )
}
