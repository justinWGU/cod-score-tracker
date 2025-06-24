import './App.css'
import ScoreBoard from './pages/ScoreBoard/ScoreBoard';
import { ErrorBoundary } from 'react-error-boundary';


function App() {
  return (
    <div className='flex justify-center items-center bg-gray-100'>
      <ErrorBoundary fallback={<div>ScoreBoard Fallback</div>}>
        <ScoreBoard />
      </ErrorBoundary>
    </div>
  );
}

export default App;
