import './App.css'
import ScoreBoard from './pages/ScoreBoard/ScoreBoard';
import { ErrorBoundary } from 'react-error-boundary';

function handleClick() {

}

function App() {
  return (
    <div className='flex justify-center items-center bg-gray-100'>
      <button onClick={handleClick}></button>
      <ErrorBoundary fallback={<div>ScoreBoard Fallback</div>}>
        <ScoreBoard />
      </ErrorBoundary>
    </div>
  );
}

export default App;
