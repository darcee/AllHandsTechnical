# Tic-Tac-Toe Game - Backend

A comprehensive tic-tac-toe game implementation using **Behavior-Driven Development (BDD)** methodology with FastAPI backend.

## 🎯 Overview

This backend implementation follows the **BDD-Spec-Partner** principles:
- **Safety-First**: Comprehensive test coverage before implementation
- **Collaborative Workflow**: Clear, readable scenarios in business language  
- **Explicit Approval**: Each scenario explicitly defines expected behavior

## 🧪 BDD Test Suite

### Test Coverage
- **14 comprehensive scenarios** covering all game functionality
- **74 step definitions** with complete validation
- **100% passing tests** with comprehensive edge case handling

### Scenarios Include:
- ✅ Game creation and initialization
- ✅ Custom player names ("Alice" vs "Bob")
- ✅ Turn-based move mechanics
- ✅ Win detection (horizontal, vertical, diagonal)
- ✅ Draw condition handling
- ✅ Invalid move validation
- ✅ Game reset functionality

## 🚀 Quick Start

### Prerequisites
```bash
python3 -m pip install -r requirements.txt
```

### Running Tests
```bash
# Method 1: Using test runner
python3 run_tests.py

# Method 2: Direct behave command
behave

# Method 3: Specific scenario
behave --name="Game ends in a draw"
```

### Expected Output
```
1 feature passed, 0 failed, 0 skipped
14 scenarios passed, 0 failed, 0 skipped
74 steps passed, 0 failed, 0 skipped, 0 undefined
```

## 🎮 Game Features

### Core Functionality
- 3x3 game board with unique game IDs
- Turn-based gameplay (X goes first)
- Complete move validation
- Win condition detection for all patterns
- Draw condition detection
- Game reset capability

### Advanced Features
- **Custom Player Names**: Support for personalized player names
- **Named Player Tracking**: Turn management with custom names
- **Personalized Announcements**: Win messages with player names
- **Comprehensive Validation**: Position occupied, out of turn, game over checks

## 📁 Project Structure

```
backend/
├── features/
│   ├── tic-tac-toe.feature          # BDD scenarios in Gherkin
│   └── steps/
│       └── tic_tac_toe_steps.py     # Step definitions
├── game.py                          # Core game engine
├── main.py                          # FastAPI application
├── start_api.py                     # API server startup script
├── test_api.py                      # API integration tests
├── demo.html                        # Interactive API demo
├── requirements.txt                  # Dependencies
├── run_tests.py                     # BDD test runner script
├── API_DOCUMENTATION.md            # Complete API documentation
├── BDD_IMPLEMENTATION_SUMMARY.md   # Detailed BDD documentation
└── README.md                       # This file
```

## 🎮 Game Engine

The `game.py` module contains the core tic-tac-toe game logic, completely separated from the BDD test framework:

### Key Features
- **Clean Architecture** - Pure Python game logic without external dependencies
- **Complete API** - All methods needed for full game functionality
- **Type Hints** - Modern Python with comprehensive type annotations
- **Comprehensive Validation** - All edge cases and error conditions handled
- **Reusable Design** - Can be imported and used in any Python application

### Core Classes
- `TicTacToeGame` - Main game engine with complete tic-tac-toe functionality

### Usage Example
```python
from game import TicTacToeGame

# Create a new game
game = TicTacToeGame("Alice", "Bob")

# Make moves
game.make_move(0, 0)  # Alice (X) plays center
game.make_move(1, 1)  # Bob (O) plays center

# Check game state
print(f"Current player: {game.get_current_player_name()}")
print(f"Winner: {game.get_winner_name()}")
print(f"Game over: {game.is_game_over()}")
```

## 🚀 FastAPI REST API

The `main.py` module provides a complete REST API built with FastAPI that integrates seamlessly with the game engine:

### Key Features
- **RESTful Design** - Standard HTTP methods and status codes
- **Auto Documentation** - Interactive Swagger UI and ReDoc
- **Input Validation** - Automatic request/response validation with Pydantic
- **CORS Support** - Ready for frontend integration
- **Error Handling** - Comprehensive error responses
- **Type Safety** - Full type hints throughout

### Quick Start
```bash
# Start the API server
python3 start_api.py

# View interactive documentation
# http://localhost:8000/docs

# Run API tests
python3 test_api.py

# Try the demo
# Open demo.html in your browser
```

### API Endpoints
- `POST /games` - Create new game
- `GET /games/{id}` - Get game state  
- `POST /games/{id}/moves` - Make a move
- `POST /games/{id}/reset` - Reset game
- `DELETE /games/{id}` - Delete game
- `GET /games/{id}/board` - Get board state
- `GET /games/{id}/status` - Get game status

See [API_DOCUMENTATION.md](API_DOCUMENTATION.md) for complete endpoint details.

## 🔧 Dependencies

- `behave==1.2.6` - BDD testing framework
- `fastapi==0.115.13` - Modern web framework for APIs
- `uvicorn==0.34.3` - ASGI server for FastAPI
- `pydantic==2.11.5` - Data validation and serialization
- `requests==2.31.0` - HTTP client for API testing

## 🎯 Game Logic

The `TicTacToeGame` class implements:
- **Board Management**: 3x3 matrix with None/X/O values
- **Turn Control**: Alternating player turns with validation
- **Win Detection**: Checks rows, columns, and diagonals
- **Draw Detection**: Full board with no winner
- **Move Validation**: Position, turn, and game state checks
- **Custom Names**: Player name support throughout gameplay

## 🔄 Next Steps

This BDD foundation enables:
1. **FastAPI REST API** - Web service endpoints
2. **Frontend Integration** - React/Vue.js interface
3. **Database Layer** - Game state persistence
4. **Real-time Play** - WebSocket multiplayer
5. **User Management** - Authentication system

## 📊 BDD Methodology

Following **Gherkin syntax** for clear business requirements:

```gherkin
Scenario: Named player wins the game
  Given I have a tic-tac-toe game with player names "Alice" and "Bob"
  And the board has X in positions (0,0) and (1,1)
  And it is Alice's turn
  When Alice places her mark in position (2,2)
  Then Alice should win the game
  And the game should be over
```

## 🏆 Achievement

✅ **Complete BDD implementation** with 100% passing tests  
✅ **Comprehensive game logic** with all edge cases covered  
✅ **Ready for API integration** with FastAPI framework  
✅ **Production-ready foundation** following best practices