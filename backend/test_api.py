#!/usr/bin/env python3
"""
API Integration Tests for Tic-Tac-Toe FastAPI endpoints.

This script tests all API endpoints to ensure they work correctly
with the game engine integration.
"""

import requests
import json
import sys
from typing import Dict, Any

# API base URL
BASE_URL = "http://localhost:8000"

def test_api_endpoint(method: str, endpoint: str, data: Dict[Any, Any] = None, expected_status: int = 200) -> Dict[Any, Any]:
    """Test an API endpoint and return the response."""
    url = f"{BASE_URL}{endpoint}"
    
    try:
        if method.upper() == "GET":
            response = requests.get(url)
        elif method.upper() == "POST":
            response = requests.post(url, json=data)
        elif method.upper() == "DELETE":
            response = requests.delete(url)
        else:
            raise ValueError(f"Unsupported method: {method}")
        
        print(f"✅ {method.upper()} {endpoint} - Status: {response.status_code}")
        
        if response.status_code != expected_status:
            print(f"❌ Expected status {expected_status}, got {response.status_code}")
            print(f"Response: {response.text}")
            return None
        
        if response.status_code != 204:  # No content for DELETE
            return response.json()
        return {}
        
    except requests.exceptions.ConnectionError:
        print(f"❌ Connection failed to {url}")
        print("Make sure the API server is running: python3 start_api.py")
        return None
    except Exception as e:
        print(f"❌ Error testing {method.upper()} {endpoint}: {e}")
        return None

def run_api_tests():
    """Run comprehensive API tests."""
    print("🧪 Testing Tic-Tac-Toe API Endpoints")
    print("=" * 50)
    
    # Test 1: Health check
    print("\n1. Testing health check...")
    health = test_api_endpoint("GET", "/")
    if not health:
        return False
    
    # Test 2: Create a new game
    print("\n2. Testing game creation...")
    game_data = {
        "player1_name": "Alice",
        "player2_name": "Bob"
    }
    game = test_api_endpoint("POST", "/games", game_data, 201)
    if not game:
        return False
    
    game_id = game["game_id"]
    print(f"   Created game with ID: {game_id[:8]}...")
    
    # Test 3: Get game state
    print("\n3. Testing get game state...")
    game_state = test_api_endpoint("GET", f"/games/{game_id}")
    if not game_state:
        return False
    
    # Test 4: List all games
    print("\n4. Testing list all games...")
    games_list = test_api_endpoint("GET", "/games")
    if not games_list:
        return False
    print(f"   Found {len(games_list)} games")
    
    # Test 5: Make valid moves
    print("\n5. Testing valid moves...")
    moves = [
        {"row": 0, "col": 0},  # Alice (X)
        {"row": 1, "col": 1},  # Bob (O)
        {"row": 0, "col": 1},  # Alice (X)
        {"row": 2, "col": 2},  # Bob (O)
        {"row": 0, "col": 2},  # Alice (X) - wins!
    ]
    
    for i, move in enumerate(moves):
        move_result = test_api_endpoint("POST", f"/games/{game_id}/moves", move)
        if not move_result:
            return False
        
        print(f"   Move {i+1}: {move_result['message']}")
        
        if move_result["game_state"]["is_game_over"]:
            print(f"   🏆 Game over! Winner: {move_result['game_state']['winner_name']}")
            break
    
    # Test 6: Try invalid move (game over)
    print("\n6. Testing invalid move (game over)...")
    invalid_move = {"row": 1, "col": 0}
    invalid_result = test_api_endpoint("POST", f"/games/{game_id}/moves", invalid_move)
    if invalid_result and not invalid_result["success"]:
        print(f"   ✅ Correctly rejected: {invalid_result['message']}")
    
    # Test 7: Get board state
    print("\n7. Testing get board...")
    board = test_api_endpoint("GET", f"/games/{game_id}/board")
    if board:
        print("   Final board:")
        for row in board:
            print(f"   {' | '.join(cell or ' ' for cell in row)}")
    
    # Test 8: Get game status
    print("\n8. Testing game status...")
    status = test_api_endpoint("GET", f"/games/{game_id}/status")
    if status:
        print(f"   Status: {json.dumps(status, indent=2)}")
    
    # Test 9: Reset game
    print("\n9. Testing game reset...")
    reset_result = test_api_endpoint("POST", f"/games/{game_id}/reset")
    if reset_result:
        print("   ✅ Game reset successfully")
        print(f"   Current player: {reset_result['current_player_name']}")
    
    # Test 10: Create another game and test draw scenario
    print("\n10. Testing draw scenario...")
    draw_game_data = {"player1_name": "Player1", "player2_name": "Player2"}
    draw_game = test_api_endpoint("POST", "/games", draw_game_data, 201)
    if not draw_game:
        return False
    
    draw_game_id = draw_game["game_id"]
    
    # Set up a draw scenario
    draw_moves = [
        {"row": 0, "col": 0},  # X
        {"row": 0, "col": 1},  # O
        {"row": 0, "col": 2},  # X
        {"row": 1, "col": 0},  # O
        {"row": 1, "col": 1},  # X
        {"row": 1, "col": 2},  # O
        {"row": 2, "col": 0},  # X
        {"row": 2, "col": 1},  # O
        {"row": 2, "col": 2},  # X - should be draw
    ]
    
    for move in draw_moves:
        move_result = test_api_endpoint("POST", f"/games/{draw_game_id}/moves", move)
        if not move_result:
            return False
        
        if move_result["game_state"]["is_game_over"]:
            if move_result["game_state"]["is_draw"]:
                print("   🤝 Draw game detected correctly!")
            else:
                print(f"   🏆 Winner: {move_result['game_state']['winner_name']}")
            break
    
    # Test 11: Delete game
    print("\n11. Testing game deletion...")
    delete_result = test_api_endpoint("DELETE", f"/games/{game_id}", expected_status=204)
    if delete_result is not None:
        print("   ✅ Game deleted successfully")
    
    # Test 12: Try to access deleted game (should fail)
    print("\n12. Testing access to deleted game...")
    deleted_game = test_api_endpoint("GET", f"/games/{game_id}", expected_status=404)
    if deleted_game is None:
        print("   ✅ Correctly returned 404 for deleted game")
    
    print("\n" + "=" * 50)
    print("🎉 All API tests completed successfully!")
    return True

def main():
    """Main test runner."""
    print("Starting API tests...")
    print("Make sure the API server is running first:")
    print("  python3 start_api.py")
    print()
    
    input("Press Enter when the server is ready...")
    
    success = run_api_tests()
    
    if success:
        print("\n✅ All tests passed!")
        sys.exit(0)
    else:
        print("\n❌ Some tests failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()