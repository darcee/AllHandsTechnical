/**
 * Debug script to check board state
 */

const API_BASE_URL = 'http://localhost:8000';

async function debugBoardState() {
  console.log('🔍 Debugging board state...\n');

  try {
    // Create a new game
    const game = await fetch(`${API_BASE_URL}/games`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        player1_name: 'Alice',
        player2_name: 'Bob'
      }),
    }).then(r => r.json());

    console.log('New game created:');
    console.log('Game ID:', game.game_id);
    console.log('Board:', JSON.stringify(game.board));
    console.log('Board length:', game.board.length);
    console.log('Board cells:');
    game.board.forEach((cell, index) => {
      console.log(`  [${index}]: ${cell === null ? 'null' : `"${cell}"`} (type: ${typeof cell})`);
    });

    // Check if all cells are null
    const allNull = game.board.every(cell => cell === null);
    console.log('\nAll cells null?', allNull);

    // Check for any non-null values
    const nonNullCells = game.board.filter(cell => cell !== null);
    console.log('Non-null cells:', nonNullCells);

  } catch (error) {
    console.error('❌ Debug failed:', error.message);
  }
}

debugBoardState();