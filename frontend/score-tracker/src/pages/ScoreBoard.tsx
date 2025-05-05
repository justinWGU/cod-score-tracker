import { useEffect, useState } from 'react';

function ScoreBoard() {
  const [leftTeamScore, setLeftTeamScore] = useState(null);
  const [rightTeamScore, setRightTeamScore] = useState(null);

  const getScores = async () => {
    console.log("Fetching...");
    try {
      const response = await fetch('http://localhost:8000/api/get-scores/?id=1');
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
    setInterval(getScores, 2000);
  }, [])
  
  return(
    <div className='flex gap-2 justify-center'>
      {leftTeamScore !== null ? <h1>{leftTeamScore}</h1> : <h1>--</h1>}
      <h1>HardPoint</h1>
      {rightTeamScore !== null ? <h1>{rightTeamScore}</h1> : <h1>--</h1>}
    </div>
  );
}
export default ScoreBoard;