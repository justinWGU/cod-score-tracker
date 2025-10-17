import { useEffect, useState } from 'react';
import type {Scores, Teams, SeriesWins, GameInfo, ScoresAPIData} from './types.ts';
import { getScores } from './api/api.ts';
import TeamPanel from './TeamPanel/TeamPanel.tsx';
import GameDetails from './GameDetails/GameDetails.tsx';

function ScoreBoard() {
  const [hasError, setHasError] = useState<boolean>(false);
  const [scores, setScores] = useState<Scores>({left: 150, right: 200});
  const [teams] = useState<Teams>({left: 'optic', right: 'faze'});
  const [seriesWins] = useState<SeriesWins>({left: 0, right: 0});
  const [gameDetails] = useState<GameInfo>({mode: 'Hardpoint', map: 'Protocol'});

  // continuously fetch scores every X secs
  useEffect( () => {
    const interval = setInterval( async () => {
      try {
        const response = await getScores(1);
        const data: ScoresAPIData = await response.json();
        setHasError(false); 
        if (!response.ok) {
          throw new Error('Failed to fetch data');
        }
        setScores({left: data.leftTeamScore, right: data.rightTeamScore});
        // more state will be set here
      } catch (err) {
          setHasError(true);
          console.error(err);
      }
    }, 5000);
    return () => clearInterval(interval);
  }, []);
  
  if (hasError) {
    return (
      <div className='bg-white shadow-2xl rounded-2xl p-5 w-xl min-h-40 flex gap-2 justify-center items-center border-2 border-gray-500'>
        <p className='text-red-600'>Error occurred fetching scores. Retrying...</p>
      </div>
    );
  } else {
    return(
      <div className='flex flex-col min-h-screen justify-center items-center bg-gray-900 text-[#EAEAF2]'>
        <h1 className='text-6xl'>Call of Duty Score Tracker</h1>
        <div className='p-5 mt-8 flex gap-2 '>
          <TeamPanel team={teams.left} score={scores.left}/>
          <GameDetails winsLeft={seriesWins.left} winsRight={seriesWins.right} mode={gameDetails.mode} map={gameDetails.map}/>
          <TeamPanel team={'optic'} score={scores.right}/>
        </div>
      </div>
    );
  }
}
export default ScoreBoard;