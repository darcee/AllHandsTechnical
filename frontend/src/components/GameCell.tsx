/**
 * Individual cell component for the tic-tac-toe board
 */

import React from 'react';
import type { CellProps } from '../types';
import './GameCell.css';

export const GameCell: React.FC<CellProps> = ({
  value,
  onClick,
  disabled,
  isWinningCell = false,
}) => {
  return (
    <button
      className={`game-cell ${isWinningCell ? 'winning-cell' : ''} ${
        value ? `player-${value.toLowerCase()}` : ''
      }`}
      onClick={onClick}
      disabled={disabled}
      aria-label={value ? `Cell contains ${value}` : 'Empty cell'}
    >
      {value}
    </button>
  );
};