interface TeamPanelProps {
  team: string;
  score: number | null;
}

function TeamPanel({ team, score }: TeamPanelProps) {
  return (
   <div className="rounded-2xl items-center border-2 border-gray-600 flex gap-1 p-5">
    <p>{team}</p>
    <p className="p-3">{score !== null ? score : '--'}</p>
   </div>
  ); 
 } export default TeamPanel;