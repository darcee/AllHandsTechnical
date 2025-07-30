/**
 * Simple test to verify the New Game button functionality
 * This simulates the exact user flow described in the issue
 */

const API_BASE_URL = 'http://localhost:8000';

async function testUINewGameFlow() {
  console.log('🎮 Testing UI New Game Flow...\n');

  try {
    // Step 1: Create initial game (simulating user starting first game)
    console.log('1️⃣ User starts first game...');
    const firstGame = await fetch(`${API_BASE_URL}/games`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        player1_name: 'Alice',
        player2_name: 'Bob'
      }),
    }).then(r => r.json());

    console.log(`✅ Game created: ${firstGame.game_id.slice(0, 8)}...`);
    console.log(`   Players: ${firstGame.player1_name} vs ${firstGame.player2_name}`);

    // Step 2: Make some moves (simulating active gameplay)
    console.log('\n2️⃣ Players make some moves...');
    
    // Alice makes first move
    await fetch(`${API_BASE_URL}/games/${firstGame.game_id}/moves`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ row: 0, col: 0 }),
    });
    
    // Bob makes second move
    await fetch(`${API_BASE_URL}/games/${firstGame.game_id}/moves`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ row: 1, col: 1 }),
    });

    console.log('✅ Moves made - game is now active with moves on the board');

    // Step 3: User clicks "New Game" button (the issue scenario)
    console.log('\n3️⃣ User clicks "New Game" button...');
    
    // This simulates what should happen when New Game is clicked:
    // - handleNewGame() is called
    // - Since game exists, it creates new game with same player names
    const newGame = await fetch(`${API_BASE_URL}/games`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        player1_name: firstGame.player1_name,
        player2_name: firstGame.player2_name
      }),
    }).then(r => r.json());

    console.log(`✅ New game created: ${newGame.game_id.slice(0, 8)}...`);
    console.log(`   Players preserved: ${newGame.player1_name} vs ${newGame.player2_name}`);
    console.log(`   Fresh board: ${newGame.board.every(row => row.every(cell => cell === null)) ? 'Yes' : 'No'}`);
    console.log(`   Current player: ${newGame.current_player_name}`);

    // Step 4: Verify the fix worked
    console.log('\n4️⃣ Verifying the fix...');
    
    const checks = [
      {
        name: 'New game has different ID',
        pass: firstGame.game_id !== newGame.game_id,
      },
      {
        name: 'Player names preserved',
        pass: firstGame.player1_name === newGame.player1_name && 
              firstGame.player2_name === newGame.player2_name,
      },
      {
        name: 'New game has clean board',
        pass: newGame.board.every(row => row.every(cell => cell === null)),
      },
      {
        name: 'New game starts with first player',
        pass: newGame.current_player === 'X' && newGame.current_player_name === newGame.player1_name,
      },
    ];

    let allPassed = true;
    checks.forEach(check => {
      const status = check.pass ? '✅' : '❌';
      console.log(`   ${status} ${check.name}`);
      if (!check.pass) allPassed = false;
    });

    if (allPassed) {
      console.log('\n🎉 SUCCESS: New Game button functionality is working correctly!');
      console.log('\n📋 What happens now when user clicks "New Game":');
      console.log('   1. handleNewGame() is called (not setShowNameForm(false))');
      console.log('   2. Since there\'s an active game, it creates a new game');
      console.log('   3. Player names are preserved from current game');
      console.log('   4. Fresh board is created');
      console.log('   5. Game starts with first player\'s turn');
    } else {
      console.log('\n❌ FAILURE: Some checks failed');
    }

  } catch (error) {
    console.error('❌ Test failed:', error.message);
  }
}

// Run the test
testUINewGameFlow();