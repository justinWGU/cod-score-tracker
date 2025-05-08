export interface ScoresAPIData {
  leftTeamScore: number | null;
  rightTeamScore: number | null;
}

export interface Scores {
  left: number | null;
  right: number | null;
}

export interface Teams {
  left: string;
  right: string;
}

export interface SeriesWins {
  left: number;
  right: number;
}

export interface GameDetails {
  mode: string;
  map: string;
}