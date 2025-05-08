import { useEffect, useState } from 'react';
import type {Scores, Teams, SeriesWins, GameDetails, ScoresAPIData} from './types.ts';
import { getScores } from './api.ts';

function ScoreBoard() {
  const [scores, setScores] = useState<Scores>({left: 150, right: 200});
  const [teams, setTeams] = useState<Teams>({left: 'Optic Gaming', right: 'Faze Clan'});
  const [seriesWins, setSeriesWins] = useState<SeriesWins>({left: 2, right: 1});
  const [gameDetails, setGameDetails] = useState<GameDetails>({mode: 'Hardpoint', map: 'Protocol'});


  // continuously fetch scores every 10 secs
  useEffect( () => {
    try {
      const interval = setInterval( async () => {
        const data: ScoresAPIData = await getScores(1);
        setScores({left: data.leftTeamScore, right: data.rightTeamScore});
        // more state will be set here
      }, 5000);

      return () => clearInterval(interval);
    } catch (err) {
      console.error(err);
    }
  }, []);
  
  return(
    <div className='bg-white shadow-2xl rounded-2xl p-5 w-xl min-h-40 flex gap-2 justify-center items-center border-2 border-red-600'>
      <div className='border-2 border-red-600'>{teams.left}</div>
      {scores.left !== null ? <h1 className='border-2 border-red-600'>{scores.left}</h1> : <h1 className='border-2 border-red-600'>--</h1>}
      <div className='text-center'>
        <h1 className='inline border-2 border-red-600'>{seriesWins.left}</h1>
        <div className='pr-1 pl-1 inline'>-</div>
        <h1 className='inline border-2 border-red-600'>{seriesWins.right}</h1>
        <h1 className='border-2 border-red-600'>{gameDetails.mode}</h1>
      </div>
      {scores.right !== null ? <h1 className='border-2 border-red-600'>{scores.right}</h1> : <h1 className='border-2 border-red-600'>--</h1>}
      <div className='border-2 border-red-600'>{teams.right}</div>
    </div>
  );
}
export default ScoreBoard;