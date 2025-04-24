import { useState } from 'react';

function ScoreBoard() {
  const [leftTeamScore, setLeftTeamScore] = useState('');
  const [rightTeamScore, setRightTeamScore] = useState('');

  const getScores = async () => {
    console.log("Fetching...");
    const response = await fetch('http://localhost:8000/api/get-scores/'); //http://localhost:8000/api/signin/
    const data = await response.json();
    const leftTeamScore = data.leftTeamScore;
    const rightTeamScore = data.rightTeamScore;
    setLeftTeamScore(leftTeamScore);
    setRightTeamScore(rightTeamScore);
  }
  
  return(
    <div>
      {leftTeamScore&& <h2>{leftTeamScore}</h2>}
      <h2>HardPoint</h2>
      {rightTeamScore&& <h2>{rightTeamScore}</h2>}
      <button onClick={getScores}>Click</button>
    </div>
  );
}
export default ScoreBoard;