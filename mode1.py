from os import system

game = [0, 0, 0, 0, 0, 0, 0, 0, 0]
char_lookup = {0: "-", 1: "X", 2: "O"}
turn = 1


def cls():
    system("cls")


def game_draw():
    game_fancy = list(map(lambda x: char_lookup[x], game))
    print("[{0[0]}] [{0[1]}] [{0[2]}]          0 1 2".format(game_fancy))
    print("[{0[3]}] [{0[4]}] [{0[5]}]          3 4 5".format(game_fancy))
    print("[{0[6]}] [{0[7]}] [{0[8]}]          6 7 8".format(game_fancy))


def win_detection():
    to_check = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for lst in to_check:
        check = list(map(lambda x: game[x], lst))
        if (check[0] != 0) & (check[0] == check[1] == check[2]):
            return check[0]
    return 0


def prod(iterable):
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


class TicTacToeIndexError(Exception):
    pass


cls()
while True:
    print("It's {}'s turn".format(char_lookup[turn]))
    game_draw()

    try:
        move = int(input())
        if move not in range(9):
            raise ValueError
        if game[move] != 0:
            raise TicTacToeIndexError
        game[move] = turn

        won = win_detection()
        if won != 0:
            print("{} has won the game!".format(char_lookup[won]))
            input("Press enter")
            exit()

        if draw_detection():
            print("The game is a draw!")
            input("Press enter")
            exit()

        turn_swap()
        cls()

    except ValueError:
        # Invalid move
        cls()
        print("You may only enter whole numbers from 0 to 8.")
    except TicTacToeIndexError:
        # Field occupied
        cls()
        print("You may only tick into unoccupied fields.")
