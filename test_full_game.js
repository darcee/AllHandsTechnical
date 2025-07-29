#!/usr/bin/env node

const API_BASE_URL = 'http://localhost:8000';

async function testFullGame() {
  console.log('🎮 Testing Full Tic-Tac-Toe Game Flow...\n');

  try {
    // 1. Create a new game
    console.log('1. Creating a new game...');
    const createResponse = await fetch(`${API_BASE_URL}/games`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        player1_name: 'Alice',
        player2_name: 'Bob'
      })
    });
    
    const gameData = await createResponse.json();
    console.log('✅ Game created:', {
      id: gameData.game_id,
      players: `${gameData.player1_name} vs ${gameData.player2_name}`,
      currentPlayer: gameData.current_player_name
    });

    const gameId = gameData.game_id;

    // 2. Play a complete game
    const moves = [
      { row: 0, col: 0, player: 'Alice' }, // X
      { row: 0, col: 1, player: 'Bob' },   // O
      { row: 1, col: 1, player: 'Alice' }, // X
      { row: 0, col: 2, player: 'Bob' },   // O
      { row: 2, col: 2, player: 'Alice' }  // X - Diagonal win!
    ];

    console.log('\n2. Playing the game...');
    for (let i = 0; i < moves.length; i++) {
      const move = moves[i];
      console.log(`\n   Move ${i + 1}: ${move.player} plays at (${move.row}, ${move.col})`);
      
      const moveResponse = await fetch(`${API_BASE_URL}/games/${gameId}/moves`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          row: move.row,
          col: move.col
        })
      });

      const moveData = await moveResponse.json();
      
      if (moveData.success) {
        console.log('   ✅ Move successful');
        console.log('   Board state:');
        moveData.game_state.board.forEach((row, idx) => {
          console.log(`   ${row.map(cell => cell || '_').join(' | ')}`);
          if (idx < 2) console.log('   ---------');
        });
        
        if (moveData.game_state.is_game_over) {
          console.log(`\n🎉 Game Over!`);
          if (moveData.game_state.winner) {
            console.log(`   Winner: ${moveData.game_state.winner_name} (${moveData.game_state.winner})`);
          } else if (moveData.game_state.is_draw) {
            console.log('   Result: Draw!');
          }
          break;
        } else {
          console.log(`   Next player: ${moveData.game_state.current_player_name}`);
        }
      } else {
        console.log('   ❌ Move failed:', moveData.message);
      }
    }

    // 3. Get final game status
    console.log('\n3. Getting final game status...');
    const statusResponse = await fetch(`${API_BASE_URL}/games/${gameId}`);
    const statusData = await statusResponse.json();
    
    console.log('✅ Final status:', {
      gameOver: statusData.is_game_over,
      winner: statusData.winner_name || 'None',
      isDraw: statusData.is_draw
    });

    console.log('\n🎉 Full game test completed successfully!');
    
  } catch (error) {
    console.error('❌ Test failed:', error.message);
  }
}

testFullGame();