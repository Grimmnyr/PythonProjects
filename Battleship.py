from random import randint
import random
board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return random.randint(0, len(board) - 1)
def random_col(board):
    return random.randint(0, len(board[0]) - 1)
ship_row = random_row(board)
ship_col = random_col(board)
ship1 = ship_row, ship_col
def random_row2(board):
    return random.randint(0, len(board) - 1)
def random_col2(board):
    return random.randint(0, len(board[0]) - 1)
ship_row2 = random_row2(board)
ship_col2 = random_col2(board)
ship2= ship_row2, ship_col2
if ship1 == ship2:
    ship_row2 = random_row2(board)
    ship_col2 = random_row2(board)
# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
for turn in range(4):
    guess_row = input("Guess Row:") - 1
    guess_col = input("Guess Col:") - 1

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if (guess_row < 0 or guess_row > len(board) -1) or (guess_col < 0 or guess_col > len(board[0])-1):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        elif guess_row == ship_row2 and guess_col == ship_col2:
            print "Congratulations! You sunk my battleship!"
            break            
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
            print_board(board)
    if turn == 3:
        print "Game Over"
    # Print (turn + 1) here!
    print turn + 1