import { useEffect, useState } from 'react';

interface ScoresAPIData {
  leftTeamScore: number | null;
  rightTeamScore: number | null;
}

interface Scores {
  left: number | null;
  right: number | null;
}

interface Teams {
  left: string;
  right: string;
}

interface SeriesWins {
  left: number;
  right: number;
}

interface GameDetails {
  mode: string;
  map: string;
}

function ScoreBoard() {
  const [scores, setScores] = useState<Scores>({left: 150, right: 200});
  const [teams, setTeams] = useState<Teams>({left: 'Optic Gaming', right: 'Faze Clan'});
  const [seriesWins, setSeriesWins] = useState<SeriesWins>({left: 2, right: 1});
  const [gameDetails, setGameDetails] = useState<GameDetails>({mode: 'Hardpoint', map: 'Protocol'});

 
  const getScores = async () => {
    console.log("Fetching...");
    try {
      const response = await fetch('http://localhost:8000/api/get-scores/?id=1');
      const data: ScoresAPIData = await response.json();
      setScores({left: data.leftTeamScore, right: data.rightTeamScore});
      // more state will be set here
    }
    catch(err) {
      console.log("Error: ", err);
    }
  }

  // continuously fetch scores every 10 secs
  useEffect( () => {
    console.log("Getting scores...");
    // research this code later
    const interval = setInterval(getScores, 2000);
    return () => clearInterval(interval);
  }, [])
  
  return(
    <div className='flex gap-2 justify-center border-2 border-red-600'>
      <div className='border-2 border-red-600'>{teams.left}</div>
      {scores.left !== null ? <h1 className='border-2 border-red-600'>{scores.left}</h1> : <h1 className='border-2 border-red-600'>--</h1>}
      <h1 className='border-2 border-red-600'>{seriesWins.left}</h1>
      <div>-</div>
      <h1 className='border-2 border-red-600'>{seriesWins.right}</h1>
      <h1 className='border-2 border-red-600'>{gameDetails.mode}</h1>
      {scores.right !== null ? <h1 className='border-2 border-red-600'>{scores.right}</h1> : <h1 className='border-2 border-red-600'>--</h1>}
      <div className='border-2 border-red-600'>{teams.right}</div>
    </div>
  );
}
export default ScoreBoard;