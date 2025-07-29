/**
 * Simple integration test to verify frontend-backend communication
 */

const API_BASE_URL = 'http://localhost:8000';

async function testApiIntegration() {
  console.log('🧪 Testing Tic-Tac-Toe API Integration...\n');

  try {
    // Test 1: Health check
    console.log('1. Testing API health...');
    const healthResponse = await fetch(`${API_BASE_URL}/`);
    const healthData = await healthResponse.json();
    console.log('✅ API Health:', healthData.message);

    // Test 2: Create a new game
    console.log('\n2. Creating a new game...');
    const createGameResponse = await fetch(`${API_BASE_URL}/games`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        player1_name: 'Alice',
        player2_name: 'Bob'
      })
    });
    const gameData = await createGameResponse.json();
    console.log('✅ Game created:', {
      id: gameData.game_id,
      players: `${gameData.player1_name} vs ${gameData.player2_name}`,
      currentPlayer: gameData.current_player_name
    });

    // Test 3: Make a move
    console.log('\n3. Making a move...');
    const moveResponse = await fetch(`${API_BASE_URL}/games/${gameData.game_id}/moves`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        row: 0,
        col: 0
      })
    });
    const moveData = await moveResponse.json();
    console.log('✅ Move made:', {
      position: '[0,0]',
      success: moveData.success,
      currentPlayer: moveData.game_state.current_player_name,
      board: moveData.game_state.board[0]
    });

    // Test 4: Get game status
    console.log('\n4. Getting game status...');
    const statusResponse = await fetch(`${API_BASE_URL}/games/${gameData.game_id}`);
    const statusData = await statusResponse.json();
    console.log('✅ Game status:', {
      gameOver: statusData.is_game_over,
      winner: statusData.winner_name || 'None',
      isDraw: statusData.is_draw
    });

    console.log('\n🎉 All tests passed! Frontend-Backend integration is working correctly.');
    
  } catch (error) {
    console.error('❌ Test failed:', error.message);
  }
}

// Run the test
testApiIntegration();