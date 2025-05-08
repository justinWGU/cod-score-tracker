import { useEffect, useState } from 'react';
import type {Scores, Teams, SeriesWins, GameInfo, ScoresAPIData} from './types.ts';
import { getScores } from './api.ts';
import TeamPanel from './TeamPanel/TeamPanel.tsx';
import GameDetails from './GameDetails/GameDetails.tsx';

function ScoreBoard() {
  const [scores, setScores] = useState<Scores>({left: 150, right: 200});
  const [teams, setTeams] = useState<Teams>({left: 'Optic Gaming', right: 'Faze Clan'});
  const [seriesWins, setSeriesWins] = useState<SeriesWins>({left: 2, right: 1});
  const [gameDetails, setGameDetails] = useState<GameInfo>({mode: 'Hardpoint', map: 'Protocol'});


  // continuously fetch scores every 10 secs
  useEffect( () => {
    try {
      const interval = setInterval( async () => {
        const data: ScoresAPIData = await getScores(1);
        setScores({left: data.leftTeamScore, right: data.rightTeamScore});
        // more state will be set here
      }, 100000);

      return () => clearInterval(interval);
    } catch (err) {
      console.error(err);
    }
  }, []);
  
  return(
    <div className='bg-white shadow-2xl rounded-2xl p-5 w-xl min-h-40 flex gap-2 justify-center items-center border-2 border-gray-500'>
      <TeamPanel team={teams.left} score={scores.left}/>
      <GameDetails winsLeft={seriesWins.left} winsRight={seriesWins.right} mode={gameDetails.mode}/>
      <TeamPanel team={teams.right} score={scores.right}/>
    </div>
  );
}
export default ScoreBoard;