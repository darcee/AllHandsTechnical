Feature: Tic-Tac-Toe Game
  As a player
  I want to play tic-tac-toe
  So that I can have fun competing against another player

  Scenario: Create a new game
    Given I want to start a new tic-tac-toe game
    When I create a new game
    Then the game should have an empty 3x3 board
    And the game should have a unique ID
    And it should be Player X's turn

  Scenario: Set custom player names
    Given I want to start a new tic-tac-toe game
    When I set player 1 name to "Alice" and player 2 name to "Bob"
    And I create a new game
    Then the game should show "Alice" as player X
    And the game should show "Bob" as player O
    And it should be Alice's turn

  Scenario: Player X makes the first move
    Given I have a new tic-tac-toe game
    When player X places their mark in position (0,0)
    Then the board should show X in position (0,0)
    And it should be Player O's turn

  Scenario: Player O makes a move
    Given I have a tic-tac-toe game with X in position (0,0)
    When player O places their mark in position (1,1)
    Then the board should show O in position (1,1)
    And it should be Player X's turn

  Scenario: Named players make moves
    Given I have a tic-tac-toe game with player names "Alice" and "Bob"
    When Alice places her mark in position (0,0)
    Then the board should show X in position (0,0)
    And it should be Bob's turn
    When Bob places his mark in position (1,1)
    Then the board should show O in position (1,1)
    And it should be Alice's turn

  Scenario: Player X wins with a horizontal line
    Given I have a tic-tac-toe game in progress
    And the board has X in positions (0,0) and (0,1)
    And it is player X's turn
    When player X places their mark in position (0,2)
    Then player X should win the game
    And the game should be over

  Scenario: Player O wins with a vertical line
    Given I have a tic-tac-toe game in progress
    And the board has O in positions (0,0) and (1,0)
    And it is player O's turn
    When player O places their mark in position (2,0)
    Then player O should win the game
    And the game should be over

  Scenario: Player X wins with a diagonal line
    Given I have a tic-tac-toe game in progress
    And the board has X in positions (0,0) and (1,1)
    And it is player X's turn
    When player X places their mark in position (2,2)
    Then player X should win the game
    And the game should be over

  Scenario: Named player wins the game
    Given I have a tic-tac-toe game with player names "Alice" and "Bob"
    And the board has X in positions (0,0) and (1,1)
    And it is Alice's turn
    When Alice places her mark in position (2,2)
    Then Alice should win the game
    And the game should be over

  Scenario: Game ends in a draw
    Given I have a tic-tac-toe game with a nearly full board
    And no player has won yet
    When the last empty position is filled
    Then the game should end in a draw
    And the game should be over

  Scenario: Invalid move - position already occupied
    Given I have a tic-tac-toe game with X in position (0,0)
    When player O tries to place their mark in position (0,0)
    Then the move should be rejected
    And it should be Player O's turn
    And the board should remain unchanged

  Scenario: Invalid move - out of turn
    Given I have a tic-tac-toe game
    And it is player X's turn
    When player O tries to place their mark in position (1,1)
    Then the move should be rejected
    And it should be Player X's turn
    And the board should remain unchanged

  Scenario: Invalid move - game already over
    Given I have a completed tic-tac-toe game with a winner
    When any player tries to make a move
    Then the move should be rejected
    And the game state should remain unchanged

  Scenario: Reset Game - create a empty board with the same setup
    Given I have a tic-tac-toe game in progress
    When I reset the game
    Then the board is cleared 
    And it is player X's turn  