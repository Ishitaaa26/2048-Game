# imports
import random, time, sys
#from getkey import getkey

# -------------------------------------------------------
print("\033[1m")
# colour things
reset = "\033[0m"
bold = "\033[1m"

red = "\033[91m"
green = "\033[92m"
purple = "\033[95m"
white = "\033[97m"
orange = "\033[38;2;255;164;0m"
pink = "\033[38;2;255;192;203m"
black = "\033[38;2;0;0;0m"
grey = "\033[38;2;220;220;220m"

# background and grid colours
bg = "\033[44m"
grid = "\033[93m"

sys.stdout.write(reset + "\033[1m" + grid + bg)

# -------------------------------------------------------

# all the different numbers
empty = "┃     ┃"
num2 = "┃" + grid + "  2  " + grid + "┃"
num4 = "┃" + green + "  4  " + grid + "┃"
num8 = "┃" + purple + "  8  " + grid + "┃"
num16 = "┃" + white + "  16 " + grid + "┃"
num32 = "┃" + red + "  32 " + grid + "┃"
num64 = "┃" + orange + "  64 " + grid + "┃"
num128 = "┃" + purple + " 128 " + grid + "┃"
num256 = "┃" + pink + " 256 " + grid + "┃"
num512 = "┃" + black + " 512 " + grid + "┃"
num1024 = "┃" + grey + "1024 " + grid + "┃"
num2048 = "┃" + green + "2048 " + grid + "┃"


# -------------------------------------------------------

# functions


def clear():
    sys.stdout.write("\033[2J\033[H")


def prtScreen():
    global screen
    global score
    clear()
    sys.stdout.write("Score: " + str(score) + "\n")
    for row in screen:
        rows = ""
        for elem in row:
            rows += elem
        sys.stdout.write(rows + "\n")
    time.sleep(0.01)


# -------------------------------------------------------

# indexes of the rows (can't remember where they are used)
row1 = 1
row2 = 4
row3 = 7
row4 = 10

# -------------------------------------------------------

# play the game
play = "y"
while play == "y":

    # resets screen for each loop
    screen = [
        [
            "┏━━━━━┓",
            "┏━━━━━┓",
            "┏━━━━━┓",
            "┏━━━━━┓",
        ],
        [
            "┃     ┃",
            "┃     ┃",
            "┃     ┃",
            "┃     ┃",
        ],
        [
            "┗━━━━━┛",
            "┗━━━━━┛",
            "┗━━━━━┛",
            "┗━━━━━┛",
        ],
        [
            "┏━━━━━┓",
            "┏━━━━━┓",
            "┏━━━━━┓",
            "┏━━━━━┓",
        ],
        [
            "┃     ┃",
            "┃     ┃",
            "┃     ┃",
            "┃     ┃",
        ],
        [
            "┗━━━━━┛",
            "┗━━━━━┛",
            "┗━━━━━┛",
            "┗━━━━━┛",
        ],
        [
            "┏━━━━━┓",
            "┏━━━━━┓",
            "┏━━━━━┓",
            "┏━━━━━┓",
        ],
        [
            "┃     ┃",
            "┃     ┃",
            "┃     ┃",
            "┃     ┃",
        ],
        [
            "┗━━━━━┛",
            "┗━━━━━┛",
            "┗━━━━━┛",
            "┗━━━━━┛",
        ],
        [
            "┏━━━━━┓",
            "┏━━━━━┓",
            "┏━━━━━┓",
            "┏━━━━━┓",
        ],
        [
            "┃     ┃",
            "┃     ┃",
            "┃     ┃",
            "┃     ┃",
        ],
        [
            "┗━━━━━┛",
            "┗━━━━━┛",
            "┗━━━━━┛",
            "┗━━━━━┛",
        ],
    ]

    # initialises variables
    moved = True
    move = True

    score = 0

    ended = False

    numbers = [1, 4, 7, 10]
    randX = random.randint(0, 3)
    randY = random.choice(numbers)
    screen[randY][randX] = num2

    # -------------------------------------------------------

    # chooses random square for a new 2
    while not ended:
        if moved == True or move == True:
            randX = random.randint(0, 3)
            randY = random.choice(numbers)
            while screen[randY][randX] != empty:
                randX = random.randint(0, 3)
                randY = random.choice(numbers)

            screen[randY][randX] = num2

        prtScreen()

        move = False
        moved = False

        # gets the key pressed
        keyPress = getkey().lower()

        # -------------------------------------------------------

        # actual game played
        if keyPress == "d":
            for loops in range(3):
                for row in [1, 4, 7, 10]:
                    for i in range(len(screen[row]) - 2, -1, -1):
                        if screen[row][i + 1] == empty and screen[row][i] != empty:
                            screen[row][i + 1] = screen[row][i]
                            screen[row][i] = empty
                            move = True
                        elif screen[row][i] == screen[row][i + 1]:
                            if screen[row][i] == num2:
                                screen[row][i] = empty
                                screen[row][i + 1] = num4
                                score += 4
                                moved = True
                            elif screen[row][i] == num4:
                                screen[row][i] = empty
                                screen[row][i + 1] = num8
                                score += 8
                                moved = True
                            elif screen[row][i] == num8:
                                screen[row][i] = empty
                                screen[row][i + 1] = num16
                                score += 16
                                moved = True
                            elif screen[row][i] == num16:
                                screen[row][i] = empty
                                screen[row][i + 1] = num32
                                score += 32
                                moved = True
                            elif screen[row][i] == num32:
                                screen[row][i] = empty
                                screen[row][i + 1] = num64
                                score += 64
                                moved = True
                            elif screen[row][i] == num64:
                                screen[row][i] = empty
                                screen[row][i + 1] = num128
                                score += 128
                                moved = True
                            elif screen[row][i] == num128:
                                screen[row][i] = empty
                                screen[row][i + 1] = num256
                                score += 256
                                moved = True
                            elif screen[row][i] == num256:
                                screen[row][i] = empty
                                screen[row][i + 1] = num512
                                score += 512
                                moved = True
                            elif screen[row][i] == num512:
                                screen[row][i] = empty
                                screen[row][i + 1] = num1024
                                score += 1024
                                moved = True
                            elif screen[row][i] == num1024:
                                screen[row][i] = empty
                                screen[row][i + 1] = num2048
                                score += 2048
                                moved = True

        elif keyPress == "a":
            for loops in range(3):
                for row in [1, 4, 7, 10]:
                    for i in range(1, len(screen[row])):
                        if screen[row][i - 1] == empty and screen[row][i] != empty:
                            screen[row][i - 1] = screen[row][i]
                            screen[row][i] = empty
                            move = True
                        elif screen[row][i] == screen[row][i - 1]:
                            if screen[row][i] == num2:
                                screen[row][i] = empty
                                screen[row][i - 1] = num4
                                score += 4
                                moved = True
                            elif screen[row][i] == num4:
                                screen[row][i] = empty
                                screen[row][i - 1] = num8
                                score += 8
                                moved = True
                            elif screen[row][i] == num8:
                                screen[row][i] = empty
                                screen[row][i - 1] = num16
                                score += 16
                                moved = True
                            elif screen[row][i] == num16:
                                screen[row][i] = empty
                                screen[row][i - 1] = num32
                                score += 32
                                moved = True
                            elif screen[row][i] == num32:
                                screen[row][i] = empty
                                screen[row][i - 1] = num64
                                score += 64
                                moved = True
                            elif screen[row][i] == num64:
                                screen[row][i] = empty
                                screen[row][i - 1] = num128
                                score += 128
                                moved = True
                            elif screen[row][i] == num128:
                                screen[row][i] = empty
                                screen[row][i - 1] = num256
                                score += 256
                                moved = True
                            elif screen[row][i] == num256:
                                screen[row][i] = empty
                                screen[row][i - 1] = num512
                                score += 512
                                moved = True
                            elif screen[row][i] == num512:
                                screen[row][i] = empty
                                screen[row][i - 1] = num1024
                                score += 1024
                                moved = True
                            elif screen[row][i] == num1024:
                                screen[row][i] = empty
                                screen[row][i - 1] = num2048
                                score += 2048
                                moved = True

        elif keyPress == "s":
            for loops in range(3):
                for row in [7, 4, 1]:
                    moved = False
                    for i in range(len(screen[row])):
                        if screen[row + 3][i] == empty and screen[row][i] != empty:
                            screen[row + 3][i] = screen[row][i]
                            screen[row][i] = empty
                            move = True
                        elif screen[row][i] == screen[row + 3][i]:
                            if screen[row][i] == num2:
                                screen[row][i] = empty
                                screen[row + 3][i] = num4
                                score += 4
                                moved = True
                            elif screen[row][i] == num4:
                                screen[row][i] = empty
                                screen[row + 3][i] = num8
                                score += 8
                                moved = True
                            elif screen[row][i] == num8:
                                screen[row][i] = empty
                                screen[row + 3][i] = num16
                                score += 16
                                moved = True
                            elif screen[row][i] == num16:
                                screen[row][i] = empty
                                screen[row + 3][i] = num32
                                score += 32
                                moved = True
                            elif screen[row][i] == num32:
                                screen[row][i] = empty
                                screen[row + 3][i] = num64
                                score += 64
                                moved = True
                            elif screen[row][i] == num64:
                                screen[row][i] = empty
                                screen[row + 3][i] = num128
                                score += 128
                                moved = True
                            elif screen[row][i] == num128:
                                screen[row][i] = empty
                                screen[row + 3][i] = num256
                                score += 256
                                moved = True
                            elif screen[row][i] == num256:
                                screen[row][i] = empty
                                screen[row + 3][i] = num512
                                score += 512
                                moved = True
                            elif screen[row][i] == num512:
                                screen[row][i] = empty
                                screen[row + 3][i] = num1024
                                score += 1025
                                moved = True
                            elif screen[row][i] == num1024:
                                screen[row][i] = empty
                                screen[row + 3][i] = num2048
                                score += 2048
                                moved = True

        elif keyPress == "w":
            for loops in range(3):
                for row in [4, 7, 10]:
                    moved = False
                    for i in range(len(screen[row])):
                        if screen[row - 3][i] == empty and screen[row][i] != empty:
                            screen[row - 3][i] = screen[row][i]
                            screen[row][i] = empty
                            move = True
                        elif screen[row][i] == screen[row - 3][i]:
                            if screen[row][i] == num2:
                                screen[row][i] = empty
                                screen[row - 3][i] = num4
                                score += 4
                                moved = True
                            elif screen[row][i] == num4:
                                screen[row][i] = empty
                                screen[row - 3][i] = num8
                                score += 8
                                moved = True
                            elif screen[row][i] == num8:
                                screen[row][i] = empty
                                screen[row - 3][i] = num16
                                score += 16
                                moved = True
                            elif screen[row][i] == num16:
                                screen[row][i] = empty
                                screen[row - 3][i] = num32
                                score += 32
                                moved = True
                            elif screen[row][i] == num32:
                                screen[row][i] = empty
                                screen[row - 3][i] = num64
                                score += 64
                                moved = True
                            elif screen[row][i] == num64:
                                screen[row][i] = empty
                                screen[row - 3][i] = num128
                                score += 128
                                moved = True
                            elif screen[row][i] == num128:
                                screen[row][i] = empty
                                screen[row - 3][i] = num256
                                score += 256
                                moved = True
                            elif screen[row][i] == num256:
                                screen[row][i] = empty
                                screen[row - 3][i] = num512
                                score += 512
                                moved = True
                            elif screen[row][i] == num512:
                                screen[row][i] = empty
                                screen[row - 3][i] = num1024
                                score += 1024
                                moved = True
                            elif screen[row][i] == num1024:
                                screen[row][i] = empty
                                screen[row - 3][i] = num2048
                                score += 2048
                                moved = True

        # -------------------------------------------------------

        prtScreen()

        # checks for a win

        for rows in [1, 4, 7, 10]:
            for i in screen[rows]:
                if i == num2048:
                    ended = True
                    play = input(
                        "Congratualtions!\nYou have won!!\n\nPlay again? (y/n)").lower()
                    while play not in ["y", "n"]:
                        clear()
                        prtScreen()
                        play = input(
                            "Congratualtions!\nYou have won!!\n\nPlay again? (y/n)").lower()

        # -------------------------------------------------------

        # checks for loss (hopefully)
        spaces = False
        for rows in [1, 4, 7, 10]:
            for i in range(len(screen[rows])):
                if screen[rows][i] == empty:
                    spaces = True

        loss = False
        if not spaces:
            loss = True
            for rows in [1, 4, 7, 10]:
                for i in range(len(screen[rows])):
                    if rows != 1 and screen[rows][i] == screen[rows - 3][i]:
                        loss = False
                    if rows != 10 and screen[rows][i] == screen[rows + 3][i]:
                        loss = False
                    if i != 0 and screen[rows][i] == screen[rows][i - 1]:
                        loss = False
                    if i != 3 and screen[rows][i] == screen[rows][i + 1]:
                        loss = False

        if loss:
            ended = True
            play = input("Oh Well\nYou Lost :(\n\nPlay again? (y/n)").lower()
            while play not in ["y", "n"]:
                clear()
                prtScreen()
                play = input("Oh Well\nYou Lost :(\n\nPlay again? (y/n)").lower()

clear()
print("BYE!!!")