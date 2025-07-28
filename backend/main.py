"""
FastAPI application for Tic-Tac-Toe Game API.

This module provides REST API endpoints for the tic-tac-toe game,
integrating with the standalone game engine from game.py.
"""

from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional, Dict, List, Tuple
import uuid
from game import TicTacToeGame

# Initialize FastAPI app
app = FastAPI(
    title="Tic-Tac-Toe Game API",
    description="A REST API for playing tic-tac-toe games with support for custom player names and game management",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory game storage (use database in production)
games: Dict[str, TicTacToeGame] = {}

# Pydantic models for request/response validation
class CreateGameRequest(BaseModel):
    """Request model for creating a new game."""
    player1_name: Optional[str] = Field(default="Player X", description="Name for player 1 (X)")
    player2_name: Optional[str] = Field(default="Player O", description="Name for player 2 (O)")

class MakeMoveRequest(BaseModel):
    """Request model for making a move."""
    row: int = Field(ge=0, le=2, description="Row position (0-2)")
    col: int = Field(ge=0, le=2, description="Column position (0-2)")

class GameResponse(BaseModel):
    """Response model for game state."""
    game_id: str
    player1_name: str
    player2_name: str
    current_player: str
    current_player_name: str
    board: List[List[Optional[str]]]
    winner: Optional[str]
    winner_name: Optional[str]
    is_draw: bool
    is_game_over: bool

class MoveResponse(BaseModel):
    """Response model for move results."""
    success: bool
    message: str
    game_state: GameResponse

class ErrorResponse(BaseModel):
    """Response model for errors."""
    error: str
    message: str

# Helper function to convert game to response model
def game_to_response(game: TicTacToeGame) -> GameResponse:
    """Convert a TicTacToeGame instance to a GameResponse model."""
    return GameResponse(
        game_id=game.game_id,
        player1_name=game.player1_name,
        player2_name=game.player2_name,
        current_player=game.current_player,
        current_player_name=game.get_current_player_name(),
        board=game.get_board_state(),
        winner=game.get_winner(),
        winner_name=game.get_winner_name(),
        is_draw=game.is_draw_game(),
        is_game_over=game.is_game_over()
    )

# API Endpoints

@app.get("/", summary="API Health Check")
async def root():
    """Health check endpoint."""
    return {
        "message": "Tic-Tac-Toe Game API is running!",
        "version": "1.0.0",
        "docs": "/docs"
    }

@app.post("/games", response_model=GameResponse, status_code=status.HTTP_201_CREATED, summary="Create New Game")
async def create_game(request: CreateGameRequest):
    """
    Create a new tic-tac-toe game.
    
    - **player1_name**: Name for player 1 (plays as X)
    - **player2_name**: Name for player 2 (plays as O)
    
    Returns the initial game state with a unique game ID.
    """
    game = TicTacToeGame(request.player1_name, request.player2_name)
    games[game.game_id] = game
    
    return game_to_response(game)

@app.get("/games", response_model=List[GameResponse], summary="List All Games")
async def list_games():
    """
    Get a list of all active games.
    
    Returns an array of all games currently in memory.
    """
    return [game_to_response(game) for game in games.values()]

@app.get("/games/{game_id}", response_model=GameResponse, summary="Get Game State")
async def get_game(game_id: str):
    """
    Get the current state of a specific game.
    
    - **game_id**: Unique identifier for the game
    
    Returns the current game state including board, players, and status.
    """
    if game_id not in games:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Game with ID {game_id} not found"
        )
    
    return game_to_response(games[game_id])

@app.post("/games/{game_id}/moves", response_model=MoveResponse, summary="Make a Move")
async def make_move(game_id: str, request: MakeMoveRequest):
    """
    Make a move in the specified game.
    
    - **game_id**: Unique identifier for the game
    - **row**: Row position (0-2)
    - **col**: Column position (0-2)
    
    Returns the move result and updated game state.
    """
    if game_id not in games:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Game with ID {game_id} not found"
        )
    
    game = games[game_id]
    
    # Attempt to make the move
    success = game.make_move(request.row, request.col)
    
    if success:
        message = f"Move successful at position ({request.row}, {request.col})"
        if game.is_game_over():
            if game.get_winner():
                message += f". {game.get_winner_name()} wins!"
            elif game.is_draw_game():
                message += ". Game ends in a draw!"
    else:
        # Determine why the move failed
        if game.is_game_over():
            message = "Game is already over"
        elif game.get_position(request.row, request.col) is not None:
            message = f"Position ({request.row}, {request.col}) is already occupied"
        else:
            message = "Invalid move"
    
    return MoveResponse(
        success=success,
        message=message,
        game_state=game_to_response(game)
    )

@app.post("/games/{game_id}/reset", response_model=GameResponse, summary="Reset Game")
async def reset_game(game_id: str):
    """
    Reset the specified game to its initial state.
    
    - **game_id**: Unique identifier for the game
    
    Returns the reset game state with an empty board.
    """
    if game_id not in games:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Game with ID {game_id} not found"
        )
    
    game = games[game_id]
    game.reset_game()
    
    return game_to_response(game)

@app.delete("/games/{game_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete Game")
async def delete_game(game_id: str):
    """
    Delete the specified game.
    
    - **game_id**: Unique identifier for the game
    
    Removes the game from memory.
    """
    if game_id not in games:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Game with ID {game_id} not found"
        )
    
    del games[game_id]
    return None

@app.get("/games/{game_id}/board", response_model=List[List[Optional[str]]], summary="Get Game Board")
async def get_board(game_id: str):
    """
    Get just the board state for the specified game.
    
    - **game_id**: Unique identifier for the game
    
    Returns a 3x3 array representing the current board state.
    """
    if game_id not in games:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Game with ID {game_id} not found"
        )
    
    return games[game_id].get_board_state()

@app.get("/games/{game_id}/status", summary="Get Game Status")
async def get_game_status(game_id: str):
    """
    Get a summary of the game status.
    
    - **game_id**: Unique identifier for the game
    
    Returns key status information about the game.
    """
    if game_id not in games:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Game with ID {game_id} not found"
        )
    
    game = games[game_id]
    
    return {
        "game_id": game.game_id,
        "current_player": game.get_current_player_name(),
        "winner": game.get_winner_name(),
        "is_draw": game.is_draw_game(),
        "is_game_over": game.is_game_over(),
        "moves_made": sum(1 for row in game.board for cell in row if cell is not None)
    }

# Error handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Custom HTTP exception handler."""
    return {
        "error": exc.__class__.__name__,
        "message": exc.detail,
        "status_code": exc.status_code
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )