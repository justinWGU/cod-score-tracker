export const getScores = async (id: number) => {
  console.log("Fetching...");
  // const url: string = 'https://codscoretracker.pythonanywhere.com/api/get-scores/';
  const url: string = 'http://localhost:8000/api/get-scores/';
  
  const response = await fetch(url + `?id=${id}`);
  
  return response;
}