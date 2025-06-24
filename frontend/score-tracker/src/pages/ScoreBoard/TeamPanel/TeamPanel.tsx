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
      <img src={team === 'optic' ? optic : faze} width={'200px'} height={'200px'} />
    </div>
    {/* <div>{team}</div> */}
    <div className="rounded-full border-2 border-black-600 w-[200px] text-center text-[30px]">{score !== null ? score : '--'}</div>
   </div>
  ); 
 } export default TeamPanel;