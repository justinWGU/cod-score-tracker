interface GameDetailsProps {
  winsLeft: number;
  winsRight: number;
  mode: string;
  map: string;
}

function GameDetails({winsLeft, winsRight, mode, map}: GameDetailsProps) {
 return (
  <div className="border-2 self-start border-gray-700 p-2 rounded-3xl">
    <div className="flex flex-col items-center bg-gray-700 p-2 size-60 rounded-2xl">
      <div className="border-2 border-gray-700 p-2 rounded-full">
        <div className="rounded-full bg-gray-700 w-[200px] text-center text-[30px]">
          <span>{winsLeft}</span>
          <span> - </span>
          <span>{winsRight}</span>
        </div>
      </div>
      <div className='text-[30px]'>{mode}</div>
      <div className='text-[30px]'>{map}</div>
    </div>
  </div>
 ); 
} export default GameDetails;