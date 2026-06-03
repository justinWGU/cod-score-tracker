import { useState, useEffect, useRef } from 'react';
import { Scores, UseScoresData } from '../../../types';
import { scoresService } from '../../../services/scoresService';

export function useScores(id: number): UseScoresData {
  const [scores, setScores] = useState<Scores | null>(null);
  const [hasError, setHasError] = useState(false);
  const ref = useRef(0);

  //
  useEffect( () => {
    console.log('in useEffect');
    const interval = setInterval( async () => {
      try {
        console.log('in setInterval try block');
        const data = await scoresService(id);
        setHasError(false); 
        setScores( { left: data.leftTeamScore, right: data.rightTeamScore } );
      } catch (err) {
          console.log('Ref: ', ref.current);
          ref.current = ref.current + 1;
          console.error(err);
          if (ref.current > 3) {
            setHasError(true);
          }
        }
    }, 3000);
    return () => clearInterval(interval);
  }, [id]);  
  return { 
    scores: scores,
    teams: {left: 'optic', right: 'faze'},
    seriesWins: {left: 0, right: 0},
    gameDetails: {mode: 'Hardpoint', map: 'Protocol'},
    hasError: hasError
   };
}