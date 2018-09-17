from os import system

game = [0, 0, 0, 0, 0, 0, 0, 0, 0]
char_lookup = {0: "-", 1: "X", 2: "O"}
turn = 1
not_turn = [0, 2, 1]

to_check = [  # Combinations of fiels a player needs to own to win
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
]


def cls():
    system("cls")


def game_draw():
    """Prints the battlefield and an index lookup."""
    game_fancy = list(map(lambda x: char_lookup[x], game))
    print("[{0[0]}] [{0[1]}] [{0[2]}]          0 1 2".format(game_fancy))
    print("[{0[3]}] [{0[4]}] [{0[5]}]          3 4 5".format(game_fancy))
    print("[{0[6]}] [{0[7]}] [{0[8]}]          6 7 8".format(game_fancy))


def win_detection():
    """Returns a player's number if they won. 0 otherwise."""
    for lst in to_check:
        check = list(map(lambda x: game[x], lst))
        if (check[0] != 0) & (check[0] == check[1] == check[2]):
            return check[0]
    return 0


def prod(iterable):
    """Returns the product of all values of the iterable."""
    out = 1
    for product in iterable:
        out *= product
    return out


def draw_detection():
    return prod(game) != 0


def turn_swap():
    global turn
    if turn == 1:
        turn = 2
    else:
        turn = 1


## AI Functions ##
def close_to_winning(player):
    """
    Checks if player is one move away from winning.
    Returns the index on the move neccecary to win. None wotherwise.
    """
    for lst in to_check:
        # Get occupieing player of field with index x
        # if (the player to look for occupies row) & (row is almost claimed) & (missing spot is unclaimed)
        check = list(map(lambda x: game[x], lst))
        if (check[0] == player) & (check[0] == check[1]) & (check[2] == 0):
            return lst[2]
        elif (check[1] == player) & (check[1] == check[2]) & (check[0] == 0):
            return lst[0]
        elif (check[0] == player) & (check[0] == check[2]) & (check[1] == 0):
            return lst[1]
    return None


def choose_prefered():
    """
    Returns the first available prefered index.
    """
    prefer = [4, 0, 2, 6, 8, 1, 3, 5, 7]
    for index in prefer:
        if not game[index]:
            return index


class TicTacToeIndexError(Exception):
    pass


cls()
## Main Loop ##
while True:
    print("It's {}'s turn".format(char_lookup[turn]))

    if turn == 1:
        # AI's turn
        winning = close_to_winning(turn)
        if winning:
            move = winning
        else:
            winning = close_to_winning(not_turn[turn])
            if winning:
                move = winning
            else:
                move = choose_prefered()

        game[move] = turn
    else:
        # Human's turn
        
        while True:
            game_draw()

            try:
                # Get human move, raise error if neccecary
                move = int(input())
                if move not in range(9):
                    raise ValueError
                if game[move] != 0:
                    raise TicTacToeIndexError
                game[move] = turn

                cls()
                break

            except ValueError:
                # Invalid move
                cls()
                print("You may only enter whole numbers from 0 to 8.")
            except TicTacToeIndexError:
                # Field occupied
                cls()
                print("You may only tick into unoccupied fields.")
        
    turn_swap()
    # Win / Draw detection
    won = win_detection()
    if won != 0:
        game_draw()
        print("{} has won the game!".format(char_lookup[won]))
        input("Press enter")
        exit()

    if draw_detection():
        game_draw()
        print("The game is a draw!")
        input("Press enter")
        exit()
