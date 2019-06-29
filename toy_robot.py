dir_list = ["NORTH", "SOUTH", "EAST", "WEST"]


class ToyRobot:
    def __init__(self, x=0, y=0, direction="NORTH"):
        self.x = x
        self.y = y
        self.direction = direction

    def place(self, input_x, input_y, input_direction):
        if input_x in range(5) and input_y in range(5) and input_direction in dir_list:
            try:
                self.x = input_x
                self.y = input_y
                self.direction = input_direction
            except NameError:
                return
        else:
            print("Invalid values")

    def move(self):
        if self.direction == "NORTH":
            if self.y < 4:
                self.y += 1
            else:
                return self.y
        elif self.direction == "SOUTH":
            if self.y > 0:
                self.y -= 1
            else:
                return self.y
        elif self.direction == "EAST":
            if self.x < 4:
                self.x += 1
            else:
                return self.x
        elif self.direction == "WEST":
            if self.x > 0:
                self.x -= 1
            else:
                return self.x
        else:
            return

    def left(self):
        if self.direction == "NORTH":
            self.direction = "WEST"
        elif self.direction == "SOUTH":
            self.direction = "EAST"
        elif self.direction == "EAST":
            self.direction = "NORTH"
        else:
            self.direction = "SOUTH"

    def right(self):
        if self.direction == "NORTH":
            self.direction = "EAST"
        elif self.direction == "SOUTH":
            self.direction = "WEST"
        elif self.direction == "EAST":
            self.direction = "SOUTH"
        else:
            self.direction = "NORTH"

    def report(self):
        return self.x, self.y, self.direction
