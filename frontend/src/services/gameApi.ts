/**
 * API service for Tic-Tac-Toe game operations
 * Handles all HTTP requests to the FastAPI backend
 */

import type {
  CreateGameRequest,
  GameResponse,
  MakeMoveRequest,
  MoveResponse,
  GameStatus,
  HealthCheck,
  ApiError,
  Board
} from '../types';

const API_BASE_URL = '/api';

class GameApiError extends Error {
  statusCode?: number;
  apiError?: ApiError;

  constructor(
    message: string,
    statusCode?: number,
    apiError?: ApiError
  ) {
    super(message);
    this.name = 'GameApiError';
    this.statusCode = statusCode;
    this.apiError = apiError;
  }
}

/**
 * Handle API response and throw appropriate errors
 */
async function handleResponse<T>(response: Response): Promise<T> {
  if (!response.ok) {
    let errorMessage = `HTTP ${response.status}: ${response.statusText}`;
    let apiError: ApiError | undefined;

    try {
      const errorData = await response.json();
      if (errorData.message) {
        errorMessage = errorData.message;
        apiError = errorData;
      }
    } catch {
      // If we can't parse the error response, use the default message
    }

    throw new GameApiError(errorMessage, response.status, apiError);
  }

  return response.json();
}

/**
 * Game API service class
 */
export class GameApiService {
  /**
   * Health check - verify API is running
   */
  static async healthCheck(): Promise<HealthCheck> {
    const response = await fetch(`${API_BASE_URL}/`);
    return handleResponse<HealthCheck>(response);
  }

  /**
   * Create a new game
   */
  static async createGame(request: CreateGameRequest = {}): Promise<GameResponse> {
    const response = await fetch(`${API_BASE_URL}/games`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(request),
    });

    return handleResponse<GameResponse>(response);
  }

  /**
   * Get all games
   */
  static async getAllGames(): Promise<GameResponse[]> {
    const response = await fetch(`${API_BASE_URL}/games`);
    return handleResponse<GameResponse[]>(response);
  }

  /**
   * Get a specific game by ID
   */
  static async getGame(gameId: string): Promise<GameResponse> {
    const response = await fetch(`${API_BASE_URL}/games/${gameId}`);
    return handleResponse<GameResponse>(response);
  }

  /**
   * Make a move in a game
   */
  static async makeMove(gameId: string, move: MakeMoveRequest): Promise<MoveResponse> {
    const response = await fetch(`${API_BASE_URL}/games/${gameId}/moves`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(move),
    });

    return handleResponse<MoveResponse>(response);
  }

  /**
   * Reset a game
   */
  static async resetGame(gameId: string): Promise<GameResponse> {
    const response = await fetch(`${API_BASE_URL}/games/${gameId}/reset`, {
      method: 'POST',
    });

    return handleResponse<GameResponse>(response);
  }

  /**
   * Delete a game
   */
  static async deleteGame(gameId: string): Promise<void> {
    const response = await fetch(`${API_BASE_URL}/games/${gameId}`, {
      method: 'DELETE',
    });

    if (!response.ok) {
      const errorMessage = `Failed to delete game: ${response.status} ${response.statusText}`;
      throw new GameApiError(errorMessage, response.status);
    }
  }

  /**
   * Get just the board state for a game
   */
  static async getBoard(gameId: string): Promise<Board> {
    const response = await fetch(`${API_BASE_URL}/games/${gameId}/board`);
    return handleResponse<Board>(response);
  }

  /**
   * Get game status summary
   */
  static async getGameStatus(gameId: string): Promise<GameStatus> {
    const response = await fetch(`${API_BASE_URL}/games/${gameId}/status`);
    return handleResponse<GameStatus>(response);
  }
}

export { GameApiError };