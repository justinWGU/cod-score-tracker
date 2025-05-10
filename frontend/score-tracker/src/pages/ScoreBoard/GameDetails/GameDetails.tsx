interface GameDetailsProps {
  winsLeft: number;
  winsRight: number;
  mode: string;
}

function GameDetails({winsLeft, winsRight, mode}: GameDetailsProps) {
 return (
  <div className="rounded-2xl p-3 border-2 border-gray-600">
    <div className='text-center'>
        <h1 className='inline'>{winsLeft}</h1>
        <div className='pr-1 pl-1 inline'>-</div>
        <h1 className='inline'>{winsRight}</h1>
        <h1 className=''>{mode}</h1>
    </div>
  </div>
 ); 
} export default GameDetails;