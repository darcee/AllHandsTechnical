/**
 * Custom React hook for managing tic-tac-toe game state
 */

import { useState, useCallback } from 'react';
import { GameApiService, GameApiError } from '../services';
import type { GameState, CreateGameRequest, MakeMoveRequest } from '../types';

interface UseGameReturn {
  game: GameState | null;
  loading: boolean;
  error: string | null;
  createGame: (request?: CreateGameRequest) => Promise<void>;
  makeMove: (row: number, col: number) => Promise<void>;
  resetGame: () => Promise<void>;
  refreshGame: () => Promise<void>;
  clearError: () => void;
}

export function useGame(): UseGameReturn {
  const [game, setGame] = useState<GameState | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const clearError = useCallback(() => {
    setError(null);
  }, []);

  const handleError = useCallback((err: unknown) => {
    console.error('Game API Error:', err);
    if (err instanceof GameApiError) {
      setError(err.message);
    } else if (err instanceof Error) {
      setError(err.message);
    } else {
      setError('An unexpected error occurred');
    }
  }, []);

  const createGame = useCallback(async (request: CreateGameRequest = {}) => {
    try {
      setLoading(true);
      setError(null);
      
      const gameResponse = await GameApiService.createGame(request);
      setGame({ ...gameResponse, loading: false });
    } catch (err) {
      handleError(err);
    } finally {
      setLoading(false);
    }
  }, [handleError]);

  const makeMove = useCallback(async (row: number, col: number) => {
    if (!game?.game_id) {
      setError('No active game');
      return;
    }

    try {
      setLoading(true);
      setError(null);

      const moveRequest: MakeMoveRequest = { row, col };
      const moveResponse = await GameApiService.makeMove(game.game_id, moveRequest);
      
      if (moveResponse.success) {
        setGame({ ...moveResponse.game_state, loading: false });
      } else {
        setError(moveResponse.message);
      }
    } catch (err) {
      handleError(err);
    } finally {
      setLoading(false);
    }
  }, [game?.game_id, handleError]);

  const resetGame = useCallback(async () => {
    if (!game?.game_id) {
      setError('No active game to reset');
      return;
    }

    try {
      setLoading(true);
      setError(null);

      const gameResponse = await GameApiService.resetGame(game.game_id);
      setGame({ ...gameResponse, loading: false });
    } catch (err) {
      handleError(err);
    } finally {
      setLoading(false);
    }
  }, [game?.game_id, handleError]);

  const refreshGame = useCallback(async () => {
    if (!game?.game_id) {
      setError('No active game to refresh');
      return;
    }

    try {
      setLoading(true);
      setError(null);

      const gameResponse = await GameApiService.getGame(game.game_id);
      setGame({ ...gameResponse, loading: false });
    } catch (err) {
      handleError(err);
    } finally {
      setLoading(false);
    }
  }, [game?.game_id, handleError]);

  return {
    game,
    loading,
    error,
    createGame,
    makeMove,
    resetGame,
    refreshGame,
    clearError,
  };
}