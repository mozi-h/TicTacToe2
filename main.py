from os import system


def cls():
    system("cls")


# Mode selection
cls()
while True:
    print("Select mode:\n1: 1 vs. 1 (human)\n2: Man v. Machine (unbeatable)")
    try:
        mode = int(input())

        if mode == 1:
            import mode1
            cls()
        elif mode == 2:
            import mode2
            pass
        else:
            cls()
            print(mode, "is not a valid mode.")
    except ValueError:
        cls()
        print("You may only enter numbers.")
