dir_list = ["NORTH", "SOUTH", "EAST", "WEST"]

class ToyRobot:
    def __init__(self,x,y,direction):
        self.x = x
        self.y = y
        self.direction = direction

    def place(self, input_x, input_y, input_direction):
        if input_x>=0 and input_x<5 and input_y>=0 and input_y<5 and input_direction in dir_list:
            try:
                self.x = input_x
                self.y = input_y
                self.direction = input_direction
            except NameError:
                return
        else:
            print ("Invalid values")



    def move(self):
        if self.direction=="NORTH":
            self.y+=1
        elif self.direction=="SOUTH":
            self.self.y-=1
        elif self.direction=="EAST":
            self.x+=1
        elif self.direction=="WEST":
            self.x-=1
        else:
            return

    def left(self):
        if self.direction=="NORTH":
            self.direction="WEST"
        elif self.direction=="SOUTH":
            self.direction="EAST"
        elif self.direction=="EAST":
            self.direction="NORTH"
        else:
            self.direction="SOUTH"
        return

    def right(self):
        if self.direction=="NORTH":
            self.direction="EAST"
        elif self.direction=="SOUTH":
            self.direction="WEST"
        elif self.direction=="EAST":
            self.direction="SOUTH"
        else:
            self.direction="NORTH"
        return

    def report(self):
        print (str(self.x),str(self.y),self.direction)
        return
