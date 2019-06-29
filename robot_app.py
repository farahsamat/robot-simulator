import os
from toy_robot import *

# Clear screen
os.system('cls' if os.name == 'nt' else 'clear')

# CLI menu
main_menu = ["PLACE", "MOVE", "LEFT", "RIGHT", "REPORT"]

# Class global vars.
if __name__ == "__main__":
    def define_place():
        global x, y, direction
        input_x, input_y, input_direction = input("Enter 'x', 'y' & 'direction' (x,y,direction): ").split(',')
        x = int(input_x)
        y = int(input_y)
        direction = input_direction.upper()
        return


    try:
        define_place()
        play = ToyRobot()
        play.place(x, y, direction)

        while x in range(5) and y in range(5) and direction in dir_list:
            choice = input("Choose command (PLACE/MOVE/LEFT/RIGHT/REPORT): ")
            if choice.upper() == main_menu[0]:
                define_place()
                play.place(x, y, direction)
            elif choice.upper() == main_menu[1]:
                play.move()
            elif choice.upper() == main_menu[2]:
                play.left()
            elif choice.upper() == main_menu[3]:
                play.right()
            elif choice.upper() == main_menu[4]:
                print(play.report())
            else:
                break
            continue
    except InputError:
        print("Invalid input")
    except ValueError:
        print("Invalid input")
