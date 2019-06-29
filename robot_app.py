from toy_robot import ToyRobot
import numpy as np
import os

# clear screen
os.system('cls' if os.name == 'nt' else 'clear')

# CLI menu
main_menu = np.array(["PLACE", "MOVE", "LEFT", "RIGHT", "REPORT", "QUIT"])


def input_number(prompt):
    while True:
        try:
            num = float(input(prompt))
            break
        except ValueError:
            print(" ")
            pass
    return num


def display_menu(options):
    print(" ")
    for i in range(len(options)):
        print("{:d}. {:s}".format(i + 1, options[i]))

    option = 0
    while not (np.any(option == np.arange(len(options)) + 1)):
        option = input_number("Enter command: ")
        print(" ")
    return option


# Class global vars.
dir_list = ["NORTH", "SOUTH", "EAST", "WEST"]

if __name__ == "__main__":
    def define_place():
        global x, y, direction
        input_x, input_y, input_direction = input("Enter 'x', 'y' & 'direction' (x,y,direction): ").split(',')
        x = int(input_x)
        y = int(input_y)
        direction = input_direction.upper()
        return


    define_place()
    play = ToyRobot(x, y, direction)
    play.place(x, y, direction)

    while x in range(5) and y in range(5) and direction in dir_list:
        choice = display_menu(main_menu)
        if choice == 1:
            define_place()
            play = ToyRobot(x, y, direction)
            play.place(x, y, direction)
        elif choice == 2:
            play.move()
        elif choice == 3:
            play.left()
        elif choice == 4:
            play.right()
        elif choice == 5:
            print(play.report())
        elif choice == 6:
            break
        continue
