/**
 * Game control buttons component
 */

import React from 'react';
import type { GameControlsProps } from '../types';
import './GameControls.css';

export const GameControls: React.FC<GameControlsProps> = ({
  onNewGame,
  onResetGame,
  gameId,
  isGameOver,
}) => {
  return (
    <div className="game-controls">
      <button
        className="control-button new-game"
        onClick={onNewGame}
        aria-label="Start a new game"
      >
        New Game
      </button>
      
      {gameId && (
        <button
          className="control-button reset-game"
          onClick={onResetGame}
          aria-label="Reset current game"
        >
          Reset Game
        </button>
      )}
      
      {gameId && (
        <div className="game-info">
          <span className="game-id">Game ID: {gameId.slice(0, 8)}...</span>
          {isGameOver && (
            <span className="game-status">Game Over</span>
          )}
        </div>
      )}
    </div>
  );
};