/**
 * TypeScript type definitions for Tic-Tac-Toe game API
 * These types match the Pydantic models from the FastAPI backend
 */

export type Player = 'X' | 'O';
export type CellValue = Player | null;
export type Board = CellValue[][];

export interface CreateGameRequest {
  player1_name?: string;
  player2_name?: string;
}

export interface MakeMoveRequest {
  row: number;
  col: number;
}

export interface GameResponse {
  game_id: string;
  player1_name: string;
  player2_name: string;
  current_player: Player;
  current_player_name: string;
  board: Board;
  winner: Player | null;
  winner_name: string | null;
  is_draw: boolean;
  is_game_over: boolean;
}

export interface MoveResponse {
  success: boolean;
  message: string;
  game_state: GameResponse;
}

export interface GameStatus {
  game_id: string;
  current_player: string;
  winner: string | null;
  is_draw: boolean;
  is_game_over: boolean;
  moves_made: number;
}

export interface ApiError {
  error: string;
  message: string;
  status_code?: number;
}

export interface HealthCheck {
  message: string;
  version: string;
  docs: string;
}

// UI-specific types
export interface GameState extends GameResponse {
  loading?: boolean;
  error?: string;
}

export interface CellProps {
  value: CellValue;
  onClick: () => void;
  disabled: boolean;
  isWinningCell?: boolean;
}

export interface GameBoardProps {
  board: Board;
  onCellClick: (row: number, col: number) => void;
  disabled: boolean;
  winningCells?: Array<[number, number]>;
}

export interface PlayerInfoProps {
  player1Name: string;
  player2Name: string;
  currentPlayer: Player;
  currentPlayerName: string;
}

export interface GameControlsProps {
  onNewGame: () => void;
  onResetGame: () => void;
  gameId: string | null;
  isGameOver: boolean;
}