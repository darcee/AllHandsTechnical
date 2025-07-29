/**
 * Component displaying game status and results
 */

import React from 'react';
import type { GameState } from '../types';
import './GameStatus.css';

interface GameStatusProps {
  game: GameState;
}

export const GameStatus: React.FC<GameStatusProps> = ({ game }) => {
  const getStatusMessage = (): string => {
    if (game.winner) {
      return `🎉 ${game.winner_name} wins!`;
    }
    if (game.is_draw) {
      return "🤝 It's a draw!";
    }
    return `🎮 ${game.current_player_name}'s turn`;
  };

  const getStatusClass = (): string => {
    if (game.winner) return 'winner';
    if (game.is_draw) return 'draw';
    return 'playing';
  };

  return (
    <div className={`game-status ${getStatusClass()}`}>
      <div className="status-message">
        {getStatusMessage()}
      </div>
      
      {game.is_game_over && (
        <div className="game-over-info">
          <p>Game Over!</p>
          <p>Start a new game or reset to play again.</p>
        </div>
      )}
      
      {game.loading && (
        <div className="loading-indicator">
          <div className="spinner"></div>
          <span>Processing...</span>
        </div>
      )}
    </div>
  );
};