from random import randint

#create empty list for board
board = []

#add 5 rows and columns of "O"s and append to board
for x in range(0, 5):
  board.append(["O"] * 5)
  
#Seperate Os with a single space
def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

#generate random battleship location
def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

#Limit to 4 turns and receive user input
for turn in range(4):
  print "Turn", turn + 1
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))

#if guess equals battleship location, congrat the user
  if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"
    break
#if guess is outside of board range, return error message and prompt another guess    
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print "Oops, that's not even in the ocean."
#if guess is the same as one already made, return error message and prompt another guess      
    elif board[guess_row][guess_col] == "X":
      print( "You guessed that one already." )
#otherwise, let the user know they missed your battleship
    else:
      print "You missed my battleship!"
      board[guess_row][guess_col] = "X"
#if max guesses have been met, let user know the game is over
    if (turn == 3):
      print "Game Over"
    print_board(board)
