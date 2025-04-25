import { useEffect, useState } from 'react';

function ScoreBoard() {
  const [leftTeamScore, setLeftTeamScore] = useState('');
  const [rightTeamScore, setRightTeamScore] = useState('');

  const getScores = async () => {
    console.log("Fetching...");
    try {
      const response = await fetch('http://localhost:8000/api/get-scores/');
      const data = await response.json();
      const leftTeamScore = data.leftTeamScore;
      const rightTeamScore = data.rightTeamScore;
      setLeftTeamScore(leftTeamScore);
      setRightTeamScore(rightTeamScore);
    }
    catch(err) {
      console.log("Error: ", err);
    }
  }

  // continuously fetch scores every 10 secs
  useEffect( () => {
    console.log("Getting scores...");
    setInterval(getScores, 5000)
  }, [])
  
  return(
    <div>
      {leftTeamScore? <h2>{leftTeamScore}</h2> : <h2>--</h2>}
      <h2>HardPoint</h2>
      {rightTeamScore? <h2>{rightTeamScore}</h2> : <h2>--</h2>}
    </div>
  );
}
export default ScoreBoard;