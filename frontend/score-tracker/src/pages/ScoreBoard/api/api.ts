import type { ScoresAPIData } from "../types.ts";


export const getScores = async (id: number): Promise<ScoresAPIData> => {
  console.log("Fetching...");
  const url: string = 'https://codscoretracker.pythonanywhere.com/api/get-scores/';
  
  const response = await fetch(url + `?id=${id}`);
  if (!response.ok) {
    throw new Error(`Failed to fetch ${url}`);
  }

  const data: ScoresAPIData = await response.json();
  return data;
}