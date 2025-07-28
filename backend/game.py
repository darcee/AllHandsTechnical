"""
Tic-Tac-Toe Game Engine

A clean, minimal implementation of tic-tac-toe game logic that meets all BDD test requirements.
This module provides the core game functionality without any external dependencies.
"""

import uuid
from typing import Optional, List, Tuple, Union


class TicTacToeGame:
    """
    A complete tic-tac-toe game implementation with support for:
    - 3x3 game board
    - Turn-based gameplay
    - Win/draw detection
    - Move validation
    - Custom player names
    - Game reset functionality
    """
    
    def __init__(self, player1_name: str = "Player X", player2_name: str = "Player O"):
        """
        Initialize a new tic-tac-toe game.
        
        Args:
            player1_name: Name for player X (default: "Player X")
            player2_name: Name for player O (default: "Player O")
        """
        self.game_id = str(uuid.uuid4())
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.winner = None
        self.is_draw = False
        self.game_over = False
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.last_move_rejected = False
    
    def get_current_player_name(self) -> str:
        """Get the name of the current player."""
        return self.player1_name if self.current_player == 'X' else self.player2_name
    
    def get_player_name(self, symbol: str) -> str:
        """Get player name by symbol (X or O)."""
        return self.player1_name if symbol == 'X' else self.player2_name
    
    def make_move(self, row: int, col: int, player: Optional[str] = None) -> bool:
        """
        Attempt to make a move on the board.
        
        Args:
            row: Row index (0-2)
            col: Column index (0-2)
            player: Player symbol ('X' or 'O'). If None, uses current player.
            
        Returns:
            True if move was successful, False if rejected
        """
        self.last_move_rejected = False
        
        # Validate game state
        if self.game_over:
            self.last_move_rejected = True
            return False
        
        # Validate position bounds
        if not (0 <= row <= 2 and 0 <= col <= 2):
            self.last_move_rejected = True
            return False
        
        # Validate position is empty
        if self.board[row][col] is not None:
            self.last_move_rejected = True
            return False
        
        # Validate turn (if player specified)
        if player is not None and player != self.current_player:
            self.last_move_rejected = True
            return False
        
        # Make the move
        self.board[row][col] = self.current_player
        
        # Check for win
        if self._check_winner():
            self.winner = self.current_player
            self.game_over = True
        # Check for draw
        elif self._is_board_full():
            self.is_draw = True
            self.game_over = True
        else:
            # Switch turns
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        
        return True
    
    def make_move_by_name(self, row: int, col: int, player_name: str) -> bool:
        """
        Make a move using player name instead of symbol.
        
        Args:
            row: Row index (0-2)
            col: Column index (0-2)
            player_name: Name of the player making the move
            
        Returns:
            True if move was successful, False if rejected
        """
        # Determine player symbol from name
        if player_name == self.player1_name:
            player_symbol = 'X'
        elif player_name == self.player2_name:
            player_symbol = 'O'
        else:
            self.last_move_rejected = True
            return False
        
        return self.make_move(row, col, player_symbol)
    
    def get_board_state(self) -> List[List[Optional[str]]]:
        """Get a copy of the current board state."""
        return [row[:] for row in self.board]
    
    def get_position(self, row: int, col: int) -> Optional[str]:
        """Get the value at a specific board position."""
        if 0 <= row <= 2 and 0 <= col <= 2:
            return self.board[row][col]
        return None
    
    def is_game_over(self) -> bool:
        """Check if the game is over (win or draw)."""
        return self.game_over
    
    def get_winner(self) -> Optional[str]:
        """Get the winning player symbol, or None if no winner."""
        return self.winner
    
    def get_winner_name(self) -> Optional[str]:
        """Get the winning player name, or None if no winner."""
        if self.winner:
            return self.get_player_name(self.winner)
        return None
    
    def is_draw_game(self) -> bool:
        """Check if the game ended in a draw."""
        return self.is_draw
    
    def was_last_move_rejected(self) -> bool:
        """Check if the last move attempt was rejected."""
        return self.last_move_rejected
    
    def reset_game(self) -> None:
        """Reset the game to initial state, keeping the same player names."""
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.winner = None
        self.is_draw = False
        self.game_over = False
        self.last_move_rejected = False
        # Keep the same game_id and player names
    
    def set_board_state(self, positions: List[Tuple[int, int, str]]) -> None:
        """
        Set multiple board positions at once (for testing).
        
        Args:
            positions: List of (row, col, symbol) tuples
        """
        for row, col, symbol in positions:
            if 0 <= row <= 2 and 0 <= col <= 2 and symbol in ['X', 'O']:
                self.board[row][col] = symbol
    
    def set_current_player(self, player: str) -> None:
        """Set the current player (for testing)."""
        if player in ['X', 'O']:
            self.current_player = player
    
    def _check_winner(self) -> bool:
        """Check if there's a winner on the current board."""
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] is not None:
                return True
        
        # Check columns
        for col in range(3):
            if (self.board[0][col] == self.board[1][col] == self.board[2][col] 
                and self.board[0][col] is not None):
                return True
        
        # Check diagonals
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] 
            and self.board[0][0] is not None):
            return True
        
        if (self.board[0][2] == self.board[1][1] == self.board[2][0] 
            and self.board[0][2] is not None):
            return True
        
        return False
    
    def _is_board_full(self) -> bool:
        """Check if the board is completely filled."""
        for row in self.board:
            for cell in row:
                if cell is None:
                    return False
        return True
    
    def __str__(self) -> str:
        """String representation of the game board."""
        lines = []
        for row in self.board:
            line = " | ".join(cell if cell else " " for cell in row)
            lines.append(line)
        return "\n---------\n".join(lines)
    
    def __repr__(self) -> str:
        """Developer representation of the game."""
        return (f"TicTacToeGame(id={self.game_id[:8]}..., "
                f"current_player={self.current_player}, "
                f"game_over={self.game_over})")