import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter as Router } from 'react-router-dom';
import { ErrorBoundary } from 'react-error-boundary';
import './index.css'
import App from './App.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <Router>
      <ErrorBoundary fallback={ <div>Cod Score Tracker App Fallback</div> }>
        <App />
      </ErrorBoundary>
    </Router>
  </StrictMode>,
)
