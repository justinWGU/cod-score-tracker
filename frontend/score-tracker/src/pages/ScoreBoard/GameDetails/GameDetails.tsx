interface GameDetailsProps {
  winsLeft: number;
  winsRight: number;
  mode: string;
}

function GameDetails({winsLeft, winsRight, mode}: GameDetailsProps) {
 return (
  <div className="flex flex-col items-center size-60 rounded-2xl p-3 border-2 border-black-600">
    <div className="border-2 border-black-600 rounded-full w-[200px] text-center text-[30px]">
      <span>{winsLeft}</span>
      <span> - </span>
      <span>{winsRight}</span>
    </div>
    <div className='text-[30px]'>{mode}</div>
  </div>
 ); 
} export default GameDetails;