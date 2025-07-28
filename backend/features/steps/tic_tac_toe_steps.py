"""
Step definitions for tic-tac-toe BDD tests.
Uses the game.py module for clean separation of concerns.
"""

from behave import given, when, then
import sys
import os

# Add the backend directory to the path so we can import game.py
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from game import TicTacToeGame


# Given steps - Set up initial game state

@given('I want to start a new tic-tac-toe game')
def step_want_new_game(context):
    """Initialize context for creating a new game."""
    context.player1_name = "Player X"
    context.player2_name = "Player O"

@given('I have a new tic-tac-toe game')
def step_have_new_game(context):
    """Create a new game instance."""
    context.game = TicTacToeGame()

@given('I have a tic-tac-toe game')
def step_have_game(context):
    """Create a new game instance."""
    context.game = TicTacToeGame()

@given('I have a tic-tac-toe game with X in position ({row:d},{col:d})')
def step_game_with_x_position(context, row, col):
    """Create a game with X already placed."""
    context.game = TicTacToeGame()
    context.game.make_move(row, col)

@given('I have a tic-tac-toe game with player names "{player1}" and "{player2}"')
def step_game_with_player_names(context, player1, player2):
    """Create a game with custom player names."""
    context.game = TicTacToeGame(player1, player2)

@given('I have a tic-tac-toe game in progress')
def step_game_in_progress(context):
    """Create a game in progress."""
    context.game = TicTacToeGame()

@given('the board has X in positions ({row1:d},{col1:d}) and ({row2:d},{col2:d})')
def step_board_has_x_positions(context, row1, col1, row2, col2):
    """Set X positions on the board."""
    context.game.set_board_state([(row1, col1, 'X'), (row2, col2, 'X')])

@given('the board has O in positions ({row1:d},{col1:d}) and ({row2:d},{col2:d})')
def step_board_has_o_positions(context, row1, col1, row2, col2):
    """Set O positions on the board."""
    context.game.set_board_state([(row1, col1, 'O'), (row2, col2, 'O')])

@given('it is player X\'s turn')
def step_player_x_turn(context):
    """Set current player to X."""
    context.game.set_current_player('X')

@given('it is player O\'s turn')
def step_player_o_turn(context):
    """Set current player to O."""
    context.game.set_current_player('O')

@given('it is {player_name}\'s turn')
def step_named_player_turn(context, player_name):
    """Set current player by name."""
    if player_name == context.game.player1_name:
        context.game.set_current_player('X')
    elif player_name == context.game.player2_name:
        context.game.set_current_player('O')

@given('I have a tic-tac-toe game with a nearly full board')
def step_nearly_full_board(context):
    """Create a game with a nearly full board for draw testing."""
    context.game = TicTacToeGame()
    # Set up a board that will result in a draw
    # X | O | X
    # O | X | O  
    # O | X | _  (last position empty - filling with O will result in draw)
    context.game.set_board_state([
        (0, 0, 'X'), (0, 1, 'O'), (0, 2, 'X'),
        (1, 0, 'O'), (1, 1, 'X'), (1, 2, 'O'),
        (2, 0, 'O'), (2, 1, 'X')
    ])
    context.game.set_current_player('O')  # O's turn to fill last position

@given('no player has won yet')
def step_no_winner_yet(context):
    """Verify no player has won."""
    assert context.game.get_winner() is None

@given('I have a completed tic-tac-toe game with a winner')
def step_completed_game_with_winner(context):
    """Create a completed game with a winner."""
    context.game = TicTacToeGame()
    # Set up a winning board for X
    context.game.set_board_state([
        (0, 0, 'X'), (0, 1, 'X'), (0, 2, 'X'),  # X wins horizontally
        (1, 0, 'O'), (1, 1, 'O')
    ])
    context.game.winner = 'X'
    context.game.game_over = True


# When steps - Actions taken during the game

@when('I set player 1 name to "{player1}" and player 2 name to "{player2}"')
def step_set_player_names(context, player1, player2):
    """Set custom player names."""
    context.player1_name = player1
    context.player2_name = player2

@when('I create a new game')
def step_create_new_game(context):
    """Create a new game with the configured player names."""
    context.game = TicTacToeGame(context.player1_name, context.player2_name)

@when('player X places their mark in position ({row:d},{col:d})')
def step_player_x_places_mark(context, row, col):
    """Player X makes a move."""
    context.move_result = context.game.make_move(row, col, 'X')

@when('player O places their mark in position ({row:d},{col:d})')
def step_player_o_places_mark(context, row, col):
    """Player O makes a move."""
    context.move_result = context.game.make_move(row, col, 'O')

@when('{player_name} places her mark in position ({row:d},{col:d})')
def step_named_player_places_mark_her(context, player_name, row, col):
    """Named player (female) makes a move."""
    context.move_result = context.game.make_move_by_name(row, col, player_name)

@when('{player_name} places his mark in position ({row:d},{col:d})')
def step_named_player_places_mark_his(context, player_name, row, col):
    """Named player (male) makes a move."""
    context.move_result = context.game.make_move_by_name(row, col, player_name)

@when('player O tries to place their mark in position ({row:d},{col:d})')
def step_player_o_tries_move(context, row, col):
    """Player O attempts a move (may be invalid)."""
    context.board_before = context.game.get_board_state()
    context.move_result = context.game.make_move(row, col, 'O')

@when('the last empty position is filled')
def step_fill_last_position(context):
    """Fill the last empty position on the board."""
    # Find the last empty position and fill it
    for row in range(3):
        for col in range(3):
            if context.game.get_position(row, col) is None:
                context.move_result = context.game.make_move(row, col)
                return

@when('any player tries to make a move')
def step_any_player_tries_move(context):
    """Any player attempts to make a move on completed game."""
    context.board_before = context.game.get_board_state()
    context.move_result = context.game.make_move(0, 0)  # Try any position

@when('I reset the game')
def step_reset_game(context):
    """Reset the game to initial state."""
    context.game.reset_game()


# Then steps - Verify expected outcomes

@then('the game should have an empty 3x3 board')
def step_verify_empty_board(context):
    """Verify the board is empty."""
    board = context.game.get_board_state()
    for row in board:
        for cell in row:
            assert cell is None, f"Expected empty board, but found {cell}"

@then('the game should have a unique ID')
def step_verify_unique_id(context):
    """Verify the game has a unique identifier."""
    assert hasattr(context.game, 'game_id')
    assert context.game.game_id is not None
    assert len(context.game.game_id) > 0

@then('it should be Player X\'s turn')
def step_verify_player_x_turn(context):
    """Verify it's Player X's turn."""
    assert context.game.current_player == 'X'

@then('it should be Player O\'s turn')
def step_verify_player_o_turn(context):
    """Verify it's Player O's turn."""
    assert context.game.current_player == 'O'

@then('it should be {player_name}\'s turn')
def step_verify_named_player_turn(context, player_name):
    """Verify it's the named player's turn."""
    current_name = context.game.get_current_player_name()
    assert current_name == player_name, f"Expected {player_name}'s turn, but it's {current_name}'s turn"

@then('the game should show "{player_name}" as player X')
def step_verify_player_x_name(context, player_name):
    """Verify player X has the correct name."""
    assert context.game.player1_name == player_name

@then('the game should show "{player_name}" as player O')
def step_verify_player_o_name(context, player_name):
    """Verify player O has the correct name."""
    assert context.game.player2_name == player_name

@then('the board should show X in position ({row:d},{col:d})')
def step_verify_x_position(context, row, col):
    """Verify X is at the specified position."""
    assert context.game.get_position(row, col) == 'X'

@then('the board should show O in position ({row:d},{col:d})')
def step_verify_o_position(context, row, col):
    """Verify O is at the specified position."""
    assert context.game.get_position(row, col) == 'O'

@then('player X should win the game')
def step_verify_player_x_wins(context):
    """Verify player X won the game."""
    assert context.game.get_winner() == 'X'

@then('player O should win the game')
def step_verify_player_o_wins(context):
    """Verify player O won the game."""
    assert context.game.get_winner() == 'O'

@then('{player_name} should win the game')
def step_verify_named_player_wins(context, player_name):
    """Verify the named player won the game."""
    winner_name = context.game.get_winner_name()
    assert winner_name == player_name, f"Expected {player_name} to win, but {winner_name} won"

@then('the game should be over')
def step_verify_game_over(context):
    """Verify the game is over."""
    assert context.game.is_game_over()

@then('the game should end in a draw')
def step_verify_draw(context):
    """Verify the game ended in a draw."""
    assert context.game.is_draw_game()

@then('the move should be rejected')
def step_verify_move_rejected(context):
    """Verify the last move was rejected."""
    assert context.game.was_last_move_rejected()

@then('the board should remain unchanged')
def step_verify_board_unchanged(context):
    """Verify the board state hasn't changed."""
    current_board = context.game.get_board_state()
    assert current_board == context.board_before, "Board state changed when it shouldn't have"

@then('the game state should remain unchanged')
def step_verify_game_state_unchanged(context):
    """Verify the game state hasn't changed."""
    current_board = context.game.get_board_state()
    assert current_board == context.board_before, "Game state changed when it shouldn't have"
    assert context.game.is_game_over(), "Game should still be over"

@then('the board is cleared')
def step_verify_board_cleared(context):
    """Verify the board has been cleared."""
    board = context.game.get_board_state()
    for row in board:
        for cell in row:
            assert cell is None, f"Expected cleared board, but found {cell}"

@then('it is player X\'s turn')
def step_verify_x_turn_after_reset(context):
    """Verify it's player X's turn after reset."""
    assert context.game.current_player == 'X'