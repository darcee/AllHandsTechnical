# 🚀 Tic-Tac-Toe Game API Documentation

## Overview

This FastAPI-based REST API provides complete tic-tac-toe game functionality, integrating seamlessly with the standalone game engine. The API supports game creation, move management, state tracking, and game lifecycle operations.

## 🔗 Base URL

```
http://localhost:8000
```

## 📚 Interactive Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🎯 API Endpoints

### Health Check

#### `GET /`
Check if the API is running.

**Response:**
```json
{
  "message": "Tic-Tac-Toe Game API is running!",
  "version": "1.0.0",
  "docs": "/docs"
}
```

---

### Game Management

#### `POST /games` - Create New Game
Create a new tic-tac-toe game with optional custom player names.

**Request Body:**
```json
{
  "player1_name": "Alice",  // Optional, defaults to "Player X"
  "player2_name": "Bob"     // Optional, defaults to "Player O"
}
```

**Response (201 Created):**
```json
{
  "game_id": "uuid-string",
  "player1_name": "Alice",
  "player2_name": "Bob",
  "current_player": "X",
  "current_player_name": "Alice",
  "board": [
    [null, null, null],
    [null, null, null],
    [null, null, null]
  ],
  "winner": null,
  "winner_name": null,
  "is_draw": false,
  "is_game_over": false
}
```

#### `GET /games` - List All Games
Get a list of all active games.

**Response:**
```json
[
  {
    "game_id": "uuid-string",
    "player1_name": "Alice",
    "player2_name": "Bob",
    // ... full game state
  }
]
```

#### `GET /games/{game_id}` - Get Game State
Get the current state of a specific game.

**Parameters:**
- `game_id` (path): Unique game identifier

**Response:**
```json
{
  "game_id": "uuid-string",
  "player1_name": "Alice",
  "player2_name": "Bob",
  "current_player": "O",
  "current_player_name": "Bob",
  "board": [
    ["X", null, null],
    [null, null, null],
    [null, null, null]
  ],
  "winner": null,
  "winner_name": null,
  "is_draw": false,
  "is_game_over": false
}
```

#### `DELETE /games/{game_id}` - Delete Game
Remove a game from memory.

**Parameters:**
- `game_id` (path): Unique game identifier

**Response:** 204 No Content

---

### Gameplay

#### `POST /games/{game_id}/moves` - Make a Move
Make a move in the specified game.

**Parameters:**
- `game_id` (path): Unique game identifier

**Request Body:**
```json
{
  "row": 0,  // Row position (0-2)
  "col": 1   // Column position (0-2)
}
```

**Response:**
```json
{
  "success": true,
  "message": "Move successful at position (0, 1)",
  "game_state": {
    // Full game state after the move
    "game_id": "uuid-string",
    "current_player": "O",
    "current_player_name": "Bob",
    "board": [
      ["X", "X", null],
      [null, null, null],
      [null, null, null]
    ],
    "winner": null,
    "is_game_over": false
    // ... rest of game state
  }
}
```

**Error Response (Invalid Move):**
```json
{
  "success": false,
  "message": "Position (0, 1) is already occupied",
  "game_state": {
    // Current game state (unchanged)
  }
}
```

#### `POST /games/{game_id}/reset` - Reset Game
Reset the game to its initial state with empty board.

**Parameters:**
- `game_id` (path): Unique game identifier

**Response:**
```json
{
  "game_id": "uuid-string",
  "player1_name": "Alice",
  "player2_name": "Bob",
  "current_player": "X",
  "current_player_name": "Alice",
  "board": [
    [null, null, null],
    [null, null, null],
    [null, null, null]
  ],
  "winner": null,
  "winner_name": null,
  "is_draw": false,
  "is_game_over": false
}
```

---

### Game Information

#### `GET /games/{game_id}/board` - Get Board State
Get just the board state for a game.

**Parameters:**
- `game_id` (path): Unique game identifier

**Response:**
```json
[
  ["X", "O", "X"],
  ["O", "X", "O"],
  ["O", "X", null]
]
```

#### `GET /games/{game_id}/status` - Get Game Status
Get a summary of game status information.

**Parameters:**
- `game_id` (path): Unique game identifier

**Response:**
```json
{
  "game_id": "uuid-string",
  "current_player": "Alice",
  "winner": null,
  "is_draw": false,
  "is_game_over": false,
  "moves_made": 5
}
```

---

## 🎮 Game Flow Example

### 1. Create a Game
```bash
curl -X POST "http://localhost:8000/games" \
  -H "Content-Type: application/json" \
  -d '{"player1_name": "Alice", "player2_name": "Bob"}'
```

### 2. Make Moves
```bash
# Alice (X) plays at (0,0)
curl -X POST "http://localhost:8000/games/{game_id}/moves" \
  -H "Content-Type: application/json" \
  -d '{"row": 0, "col": 0}'

# Bob (O) plays at (1,1)
curl -X POST "http://localhost:8000/games/{game_id}/moves" \
  -H "Content-Type: application/json" \
  -d '{"row": 1, "col": 1}'
```

### 3. Check Game State
```bash
curl "http://localhost:8000/games/{game_id}"
```

### 4. Reset or Delete Game
```bash
# Reset
curl -X POST "http://localhost:8000/games/{game_id}/reset"

# Delete
curl -X DELETE "http://localhost:8000/games/{game_id}"
```

---

## 🚨 Error Responses

### 404 Not Found
```json
{
  "error": "HTTPException",
  "message": "Game with ID {game_id} not found",
  "status_code": 404
}
```

### 422 Validation Error
```json
{
  "detail": [
    {
      "loc": ["body", "row"],
      "msg": "ensure this value is greater than or equal to 0",
      "type": "value_error.number.not_ge"
    }
  ]
}
```

---

## 🔧 Running the API

### Start the Server
```bash
# Using the startup script
python3 start_api.py

# Or directly with uvicorn
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### Run Tests
```bash
# Run BDD tests (game engine)
python3 run_tests.py

# Run API integration tests
python3 test_api.py
```

### View Demo
Open `demo.html` in a web browser to see a working frontend example.

---

## 🏗️ Architecture

The API is built with:
- **FastAPI**: Modern, fast web framework
- **Pydantic**: Data validation and serialization
- **Game Engine**: Clean separation from `game.py` module
- **CORS Support**: Ready for frontend integration
- **Type Hints**: Full type safety throughout

### Key Features
- ✅ **RESTful Design** - Standard HTTP methods and status codes
- ✅ **Input Validation** - Automatic request/response validation
- ✅ **Error Handling** - Comprehensive error responses
- ✅ **Documentation** - Auto-generated OpenAPI docs
- ✅ **CORS Support** - Ready for web frontend integration
- ✅ **Type Safety** - Full type hints and validation

---

## 🚀 Next Steps

This API provides a solid foundation for:
- **Frontend Integration** - React, Vue.js, or vanilla JavaScript
- **Real-time Features** - WebSocket support for live gameplay
- **Persistence** - Database integration for game history
- **Authentication** - User accounts and game ownership
- **Multiplayer** - Room-based multiplayer functionality

The clean architecture makes it easy to extend and scale the application as needed.