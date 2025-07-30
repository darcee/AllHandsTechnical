/**
 * Main Tic-Tac-Toe game component
 * Orchestrates all game functionality and UI components
 */

import React, { useState } from 'react';
import { useGame } from '../hooks';
import {
  GameBoard,
  PlayerInfo,
  GameControls,
  GameStatus,
  ErrorMessage,
} from './';
import './TicTacToe.css';

export const TicTacToe: React.FC = () => {
  const { game, loading, error, createGame, makeMove, resetGame, clearError } = useGame();
  const [player1Name, setPlayer1Name] = useState('Player X');
  const [player2Name, setPlayer2Name] = useState('Player O');
  const [showNameForm, setShowNameForm] = useState(false);

  const handleNewGame = async () => {
    if (showNameForm) {
      await createGame({ player1_name: player1Name, player2_name: player2Name });
      setShowNameForm(false);
    } else {
      // If there's an active game, start a new game with the same player names
      // If no active game, show the name form
      if (game) {
        // Use the current game's player names for the new game
        await createGame({ 
          player1_name: game.player1_name, 
          player2_name: game.player2_name 
        });
      } else {
        setShowNameForm(true);
      }
    }
  };

  const handleQuickStart = async () => {
    await createGame();
    setShowNameForm(false);
  };

  const handleCellClick = async (row: number, col: number) => {
    if (game && !game.is_game_over && !loading) {
      await makeMove(row, col);
    }
  };

  const handleResetGame = async () => {
    if (game) {
      await resetGame();
    }
  };

  return (
    <div className="tic-tac-toe">
      <header className="game-header">
        <h1>🎮 Tic-Tac-Toe</h1>
        <p>Challenge your friend to a classic game!</p>
      </header>

      {error && (
        <ErrorMessage error={error} onDismiss={clearError} />
      )}

      {!game && showNameForm && (
        <div className="name-form">
          <h3>Enter Player Names</h3>
          <div className="name-inputs">
            <div className="input-group">
              <label htmlFor="player1">Player X:</label>
              <input
                id="player1"
                type="text"
                value={player1Name}
                onChange={(e) => setPlayer1Name(e.target.value)}
                placeholder="Enter name for X"
                maxLength={20}
              />
            </div>
            <div className="input-group">
              <label htmlFor="player2">Player O:</label>
              <input
                id="player2"
                type="text"
                value={player2Name}
                onChange={(e) => setPlayer2Name(e.target.value)}
                placeholder="Enter name for O"
                maxLength={20}
              />
            </div>
          </div>
          <div className="form-buttons">
            <button
              className="start-button"
              onClick={handleNewGame}
              disabled={loading}
            >
              {loading ? 'Starting...' : 'Start Game'}
            </button>
            <button
              className="quick-start-button"
              onClick={handleQuickStart}
              disabled={loading}
            >
              Quick Start
            </button>
            <button
              className="cancel-button"
              onClick={() => setShowNameForm(false)}
            >
              Cancel
            </button>
          </div>
        </div>
      )}

      {game && (
        <div className="game-container">
          <PlayerInfo
            player1Name={game.player1_name}
            player2Name={game.player2_name}
            currentPlayer={game.current_player}
            currentPlayerName={game.current_player_name}
          />

          <GameStatus game={game} />

          <GameBoard
            board={game.board}
            onCellClick={handleCellClick}
            disabled={game.is_game_over || loading}
          />

          <GameControls
            onNewGame={handleNewGame}
            onResetGame={handleResetGame}
            gameId={game.game_id}
            isGameOver={game.is_game_over}
          />
        </div>
      )}

      {!game && !showNameForm && (
        <div className="welcome-screen">
          <div className="welcome-content">
            <h2>Welcome to Tic-Tac-Toe!</h2>
            <p>Ready to play? Click below to start a new game.</p>
            <button
              className="start-button large"
              onClick={handleNewGame}
              disabled={loading}
            >
              {loading ? 'Loading...' : 'New Game'}
            </button>
          </div>
        </div>
      )}

      <footer className="game-footer">
        <p>Built with React + TypeScript + FastAPI</p>
      </footer>
    </div>
  );
};
