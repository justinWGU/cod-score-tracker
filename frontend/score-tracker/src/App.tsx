import './App.css'
import Landing from './pages/Landing/Landing';
import ScoreBoard from './pages/ScoreBoard/ScoreBoard';
import { ErrorBoundary } from 'react-error-boundary';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <Router>
      <Routes>
        <Route path='/' element={ <Landing /> }/>
        <Route path='/scoreboard' element={ <ErrorBoundary fallback={<div>ScoreBoard Fallback</div>}><ScoreBoard /></ErrorBoundary> } />
      </Routes>
    </Router>
  );
}

export default App;
