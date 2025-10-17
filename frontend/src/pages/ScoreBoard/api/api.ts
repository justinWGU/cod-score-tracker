export const getScores = async (id: number) => {
  console.log("Fetching...");
  // const url = 'https://codscoretracker.pythonanywhere.com/api/get-scores/';
  // const url = 'http://localhost:8000/api/get-scores/';
  const url = 'https://cod-score-tracker.onrender.com/api/get-scores/';
  
  const response = await fetch(url + `?id=${id}`);
  
  return response;
}