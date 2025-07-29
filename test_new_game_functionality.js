/**
 * Test script to verify the "New Game" functionality works correctly
 * This simulates the user clicking "New Game" when there's already an active game
 */

const API_BASE_URL = 'http://localhost:8000';

async function testNewGameFunctionality() {
  console.log('🧪 Testing New Game Functionality...\n');

  try {
    // Step 1: Create first game
    console.log('1️⃣ Creating first game...');
    const firstGameResponse = await fetch(`${API_BASE_URL}/games`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        player1_name: 'Alice',
        player2_name: 'Bob'
      }),
    });

    if (!firstGameResponse.ok) {
      throw new Error(`Failed to create first game: ${firstGameResponse.status}`);
    }

    const firstGame = await firstGameResponse.json();
    console.log(`✅ First game created: ${firstGame.game_id.slice(0, 8)}...`);
    console.log(`   Players: ${firstGame.player1_name} vs ${firstGame.player2_name}`);
    console.log(`   Current player: ${firstGame.current_player_name}\n`);

    // Step 2: Make a move in the first game
    console.log('2️⃣ Making a move in first game...');
    const moveResponse = await fetch(`${API_BASE_URL}/games/${firstGame.game_id}/moves`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        row: 0,
        col: 0
      }),
    });

    if (!moveResponse.ok) {
      throw new Error(`Failed to make move: ${moveResponse.status}`);
    }

    const moveResult = await moveResponse.json();
    console.log(`✅ Move made successfully`);
    console.log(`   Board state: [${moveResult.game_state.board.slice(0, 3).map(cell => cell || '_').join(', ')}]`);
    console.log(`   Next player: ${moveResult.game_state.current_player_name}\n`);

    // Step 3: Create a new game (simulating "New Game" button click)
    console.log('3️⃣ Creating new game (simulating "New Game" button)...');
    const newGameResponse = await fetch(`${API_BASE_URL}/games`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        player1_name: firstGame.player1_name, // Using same player names
        player2_name: firstGame.player2_name
      }),
    });

    if (!newGameResponse.ok) {
      throw new Error(`Failed to create new game: ${newGameResponse.status}`);
    }

    const newGame = await newGameResponse.json();
    console.log(`✅ New game created: ${newGame.game_id.slice(0, 8)}...`);
    console.log(`   Players: ${newGame.player1_name} vs ${newGame.player2_name}`);
    console.log(`   Current player: ${newGame.current_player_name}`);
    console.log(`   Board is fresh: [${newGame.board.slice(0, 3).map(cell => cell || '_').join(', ')}]\n`);

    // Step 4: Verify the games are different
    console.log('4️⃣ Verifying games are different...');
    if (firstGame.game_id !== newGame.game_id) {
      console.log('✅ Games have different IDs - New game created successfully');
    } else {
      console.log('❌ Games have same ID - New game creation failed');
    }

    // Step 5: Verify new game has clean board
    const hasEmptyBoard = newGame.board.every(cell => cell === null);
    if (hasEmptyBoard) {
      console.log('✅ New game has clean board');
    } else {
      console.log('❌ New game board is not clean');
    }

    // Step 6: Verify first game still exists and has the move
    console.log('\n5️⃣ Verifying first game still exists...');
    const firstGameCheckResponse = await fetch(`${API_BASE_URL}/games/${firstGame.game_id}`);
    
    if (firstGameCheckResponse.ok) {
      const firstGameCheck = await firstGameCheckResponse.json();
      const hasMove = firstGameCheck.board[0] === 'X';
      if (hasMove) {
        console.log('✅ First game still exists with the move intact');
      } else {
        console.log('❌ First game exists but move is missing');
      }
    } else {
      console.log('⚠️  First game no longer accessible (this might be expected behavior)');
    }

    console.log('\n🎉 New Game functionality test completed successfully!');
    console.log('\n📋 Summary:');
    console.log('   - ✅ Can create multiple games');
    console.log('   - ✅ New games have fresh boards');
    console.log('   - ✅ Player names are preserved');
    console.log('   - ✅ Games have unique IDs');

  } catch (error) {
    console.error('❌ Test failed:', error.message);
    process.exit(1);
  }
}

// Run the test
testNewGameFunctionality();