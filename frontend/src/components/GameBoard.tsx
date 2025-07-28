/**
 * Game board component containing 3x3 grid of cells
 */

import React from 'react';
import type { GameBoardProps } from '../types';
import { GameCell } from './GameCell';
import './GameBoard.css';

export const GameBoard: React.FC<GameBoardProps> = ({
  board,
  onCellClick,
  disabled,
  winningCells = [],
}) => {
  const isWinningCell = (row: number, col: number): boolean => {
    return winningCells.some(([winRow, winCol]) => winRow === row && winCol === col);
  };

  return (
    <div className="game-board" role="grid" aria-label="Tic-tac-toe game board">
      {board.map((row, rowIndex) =>
        row.map((cell, colIndex) => (
          <GameCell
            key={`${rowIndex}-${colIndex}`}
            value={cell}
            onClick={() => onCellClick(rowIndex, colIndex)}
            disabled={disabled || cell !== null}
            isWinningCell={isWinningCell(rowIndex, colIndex)}
          />
        ))
      )}
    </div>
  );
};