/**
 * Component displaying player information and current turn
 */

import React from 'react';
import type { PlayerInfoProps } from '../types';
import './PlayerInfo.css';

export const PlayerInfo: React.FC<PlayerInfoProps> = ({
  player1Name,
  player2Name,
  currentPlayer,
  currentPlayerName,
}) => {
  return (
    <div className="player-info">
      <div className="players">
        <div className={`player ${currentPlayer === 'X' ? 'active' : ''}`}>
          <span className="player-symbol player-x">X</span>
          <span className="player-name">{player1Name}</span>
        </div>
        <div className="vs">VS</div>
        <div className={`player ${currentPlayer === 'O' ? 'active' : ''}`}>
          <span className="player-symbol player-o">O</span>
          <span className="player-name">{player2Name}</span>
        </div>
      </div>
      <div className="current-turn">
        <span>Current Turn: </span>
        <span className={`current-player player-${currentPlayer.toLowerCase()}`}>
          {currentPlayerName}
        </span>
      </div>
    </div>
  );
};