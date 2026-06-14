import type { Metadata } from 'next'
import './globals.css'

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
        <header>
          <h1>🎯 AI Job Application System</h1>
          <nav>
            <a href="/">Home</a>
            <a href="/upload">Upload Resume</a>
            <a href="/jobs">Jobs</a>
            <a href="/applications">Applications</a>
          </nav>
        </header>
        <main>
          {children}
        </main>
      </body>
    </html>
  )
}
