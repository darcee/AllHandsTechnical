# AllHandsTechnical - Tic-Tac-Toe Project

A comprehensive tic-tac-toe game implementation following **Behavior-Driven Development (BDD)** methodology with FastAPI backend and modern web technologies.

## 🎯 Project Overview

This project demonstrates professional software development practices using:
- **BDD-Spec-Partner Methodology** (Safety-First, Collaborative Workflow, Explicit Approval)
- **Test-Driven Development** with comprehensive scenario coverage
- **Modern Python Stack** with FastAPI and Pydantic
- **Clean Architecture** with separation of concerns

## 📁 Project Structure

```
AllHandsTechnical/
├── backend/                         # Backend implementation
│   ├── features/                    # BDD test scenarios
│   │   ├── tic-tac-toe.feature     # Gherkin scenarios
│   │   └── steps/                  # Step definitions
│   │       └── tic_tac_toe_steps.py # BDD step definitions
│   ├── game.py                    # Core game engine
│   ├── requirements.txt            # Python dependencies
│   ├── run_tests.py               # Test runner script
│   ├── BDD_IMPLEMENTATION_SUMMARY.md # Detailed docs
│   └── README.md                  # Backend documentation
├── BDD_spec.md                    # BDD specification document
└── README.md                      # This file
```

## 🧪 BDD Implementation Status

### ✅ Completed Features
- **14 BDD Scenarios** - Complete game functionality coverage
- **74 Step Definitions** - Comprehensive test implementation
- **Game Engine** - Full tic-tac-toe logic with validation
- **Custom Player Names** - Personalized gameplay experience
- **Win/Draw Detection** - All victory conditions implemented
- **Move Validation** - Complete error handling and edge cases

### 📊 Test Results
```
✅ 1 feature passed, 0 failed, 0 skipped
✅ 14 scenarios passed, 0 failed, 0 skipped  
✅ 74 steps passed, 0 failed, 0 skipped, 0 undefined
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip package manager

### Setup & Run Tests
```bash
# Clone the repository
git clone https://github.com/darcee/AllHandsTechnical.git
cd AllHandsTechnical/backend

# Install dependencies
pip install -r requirements.txt

# Run BDD tests
python3 run_tests.py
# or
behave
```

## 🎮 Game Features

### Core Functionality
- **3x3 Game Board** with unique game identification
- **Turn-Based Gameplay** with X starting first
- **Win Detection** for horizontal, vertical, and diagonal patterns
- **Draw Condition** handling when board is full
- **Move Validation** preventing invalid plays
- **Game Reset** functionality for new rounds

### Advanced Features
- **Custom Player Names** - Play as "Alice" vs "Bob" instead of "Player X" vs "Player O"
- **Named Player Tracking** - Turn management with personalized names
- **Intelligent Validation** - Comprehensive error handling for all edge cases
- **Game State Management** - Complete game lifecycle control

## 🎯 BDD-Spec-Partner Principles

### 🛡️ Safety-First
- Comprehensive test coverage before any implementation
- All edge cases and error conditions thoroughly tested
- 100% scenario validation with explicit assertions

### 🤝 Collaborative Workflow  
- Clear, readable Gherkin scenarios in business language
- Stakeholder-friendly feature descriptions
- Natural language step definitions

### ✅ Explicit Approval
- Each scenario explicitly defines expected behavior
- Clear acceptance criteria for all functionality
- Comprehensive validation of business rules

## 🔧 Technology Stack

### Backend
- **Python 3.12** - Modern Python runtime
- **Behave 1.2.6** - BDD testing framework
- **FastAPI 0.115.13** - High-performance web framework
- **Uvicorn 0.34.3** - ASGI server for production
- **Pydantic 2.11.5** - Data validation and serialization

### Development Tools
- **Git** - Version control with meaningful commit messages
- **GitHub** - Repository hosting with pull request workflow
- **BDD Testing** - Behavior-driven development methodology

## 📈 Development Roadmap

### Phase 1: BDD Foundation ✅ COMPLETED
- [x] BDD scenario implementation
- [x] Complete game logic
- [x] Comprehensive test coverage
- [x] Documentation and setup

### Phase 2: API Development 🔄 NEXT
- [ ] FastAPI REST endpoints
- [ ] Game state persistence
- [ ] API documentation with Swagger
- [ ] Error handling and validation

### Phase 3: Frontend Integration 📋 PLANNED
- [ ] React/Vue.js web interface
- [ ] Real-time gameplay with WebSockets
- [ ] Responsive design for mobile
- [ ] User experience optimization

### Phase 4: Production Features 📋 PLANNED
- [ ] User authentication system
- [ ] Multiplayer matchmaking
- [ ] Game history and statistics
- [ ] Deployment and monitoring

## 🏆 Key Achievements

- ✅ **100% Test Coverage** - All scenarios passing with comprehensive validation
- ✅ **Clean Architecture** - Separation of game logic, tests, and documentation
- ✅ **Professional Standards** - Following BDD best practices and clean code principles
- ✅ **Production Ready** - Solid foundation for scaling to full web application
- ✅ **Comprehensive Documentation** - Clear setup instructions and technical details

## 🤝 Contributing

This project follows professional development practices:
1. **Feature Branches** - All development in dedicated branches
2. **Pull Requests** - Code review process with detailed descriptions
3. **BDD First** - All features start with behavior scenarios
4. **Test Coverage** - Maintain 100% scenario coverage
5. **Documentation** - Keep README and docs updated

## 📄 License

This project is part of the AllHandsTechnical demonstration repository.

---

**Built with ❤️ using BDD methodology and modern Python practices**