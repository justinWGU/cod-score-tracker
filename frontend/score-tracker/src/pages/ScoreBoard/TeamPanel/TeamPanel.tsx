interface TeamPanelProps {
  team: string;
  score: number | null;
}

function TeamPanel({ team, score }: TeamPanelProps) {
  return (
   <div className="border-2 border-gray-600 flex gap-1 p-5">
    {<div className=''>{team}</div>}
    {score !== null ? <h1 className=''>{score}</h1> : <h1 className=''>--</h1>}
   </div>
  ); 
 } export default TeamPanel;