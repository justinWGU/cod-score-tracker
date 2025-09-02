import { useNavigate } from "react-router-dom";
import preview from "./static/preview.png";


function Landing() {
  const navigate = useNavigate();
  return (
      <div className="flex pl-15 pr-15 flex-col border-black border-4 bg-[#0a192f] text-white p-10 ">
        
        <h1 className="text-4xl text-green-400">Call of Duty Score Tracker</h1>
        <p className="mt-1">Live Call of Duty Scores Anytime, Anywhere</p>
        <div className="flex mt-2">
          <button className="mr-5 bg-blue-800 rounded-lg pr-6 pl-6 p-3 hover:cursor-pointer" onClick={() => navigate('/scoreboard')}>View Demo</button>
          <a href="#section-get-involved" className=" rounded-lg pr-6 pl-6 p-3 border border-blue-800">Get Involved</a>
        </div>
        
        <h2 className="text-2xl mt-2">What is it?</h2>
        <p>Call of Duty Tracking app for real-time game scores. Never miss out on your favorite teams even if you can't tune in to the stream.</p>
        
        <div>
          <h2 className="text-2xl mt-5">Preview</h2>
          <img src={preview} className="rounded-lg" width='50%' alt="img"></img>
        </div>

        <h3 className="text-xl mt-5 mb-1">Help Build it</h3>
          <p>This project is still in development and you could be a part of it!</p>
          <p>What we are looking for:</p>
          <ul className="list-disc list-inside">
            <li>Developers(React, Django)</li>
            <li>Designers(UI/UX)</li>
            <li>DevOps(hosting, Netlify, AWS)</li>
            <li>Gamers(testing, feedback, feature ideas)</li>
          </ul>
          <div className="flex">
            <a id="section-get-involved" href="https://github.com/justinWGU/cod-score-tracker" className="ml-0 m-5">Github</a>
            <a className="m-5">Contact</a>
          </div>
      </div>
  );
} export default Landing;