import optic from '../assets/optic.png';
import faze from '../assets/faze.png';

interface TeamPanelProps {
  team: string;
  score: number | null;
}

function TeamPanel({ team, score }: TeamPanelProps) {
  return (
   <div className="size-125 rounded-2xl flex flex-col items-center gap-1 p-5">
    <div className='w-[200px] h-[200px]'>
      <img src={team === 'optic' ? optic : faze} alt={team} width={'200px'} height={'200px'} />
    </div>
    <div className='border-2 border-gray-700 p-2 rounded-full'>
      <div className='rounded-full bg-gray-700 w-[200px] text-center text-[30px]'>{score !== null ? score : '--'}</div>
    </div>
   </div>
  ); 
 } export default TeamPanel;