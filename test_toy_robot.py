import unittest

from toy_robot import ToyRobot, InputError


class ToyRobotTest(unittest.TestCase):
    def test_init_sets_correct_default_attributes(self):
        robot = ToyRobot()
        self.assertEqual(robot.x, 0)
        self.assertEqual(robot.y, 0)
        self.assertEqual(robot.direction, "NORTH")

    def test_init_sets_correct_non_default_attributes(self):
        robot = ToyRobot(4, 2, "EAST")
        self.assertEqual(robot.x, 4)
        self.assertEqual(robot.y, 2)
        self.assertEqual(robot.direction, "EAST")

    def test_place_with_valid_coordinates_and_direction_places_robot_in_valid_place(self):
        robot = ToyRobot()
        robot.place(3, 3, "NORTH")
        self.assertEqual(robot.x, 3)
        self.assertEqual(robot.y, 3)
        self.assertEqual(robot.direction, "NORTH")

    def test_place_with_invalid_coordinates_raises_error(self):
        robot = ToyRobot()
        with self.assertRaises(InputError):
            robot.place(6, 3, "WEST")

    def test_place_with_invalid_direction_raises_error(self):
        robot = ToyRobot()
        with self.assertRaises(InputError):
            robot.place(0, 3, "DOWN")

    def test_move_robot_adds_1_step_towards_north(self):
        robot = ToyRobot(0, 3, "NORTH")
        robot.move()
        self.assertEqual(robot.x, 0)
        self.assertEqual(robot.y, 4)
        self.assertEqual(robot.direction, "NORTH")

    def test_move_robot_adds_1_step_towards_south(self):
        robot = ToyRobot(0, 3, "SOUTH")
        robot.move()
        self.assertEqual(robot.x, 0)
        self.assertEqual(robot.y, 2)
        self.assertEqual(robot.direction, "SOUTH")

    def test_move_robot_adds_1_step_towards_east(self):
        robot = ToyRobot(0, 3, "EAST")
        robot.move()
        self.assertEqual(robot.x, 1)
        self.assertEqual(robot.y, 3)
        self.assertEqual(robot.direction, "EAST")

    def test_move_robot_adds_1_step_towards_west(self):
        robot = ToyRobot(1, 3, "WEST")
        robot.move()
        self.assertEqual(robot.x, 0)
        self.assertEqual(robot.y, 3)
        self.assertEqual(robot.direction, "WEST")

    def test_move_prevents_robot_from_falling_north(self):
        robot = ToyRobot(0, 4, "NORTH")
        robot.move()
        self.assertEqual(robot.x, 0)
        self.assertEqual(robot.y, 4)
        self.assertEqual(robot.direction, "NORTH")

    def test_move_prevents_robot_from_falling_south(self):
        robot = ToyRobot(2, 0, "SOUTH")
        robot.move()
        self.assertEqual(robot.x, 2)
        self.assertEqual(robot.y, 0)
        self.assertEqual(robot.direction, "SOUTH")

    def test_move_prevents_robot_from_falling_east(self):
        robot = ToyRobot(4, 4, "EAST")
        robot.move()
        self.assertEqual(robot.x, 4)
        self.assertEqual(robot.y, 4)
        self.assertEqual(robot.direction, "EAST")

    def test_move_prevents_robot_from_falling_west(self):
        robot = ToyRobot(0, 4, "WEST")
        robot.move()
        self.assertEqual(robot.x, 0)
        self.assertEqual(robot.y, 4)
        self.assertEqual(robot.direction, "WEST")

    def test_left_rotates_robot_90_degrees_to_the_left_when_facing_north(self):
        robot = ToyRobot(1, 1, "NORTH")
        robot.left()
        self.assertEqual(robot.x, 1)
        self.assertEqual(robot.y, 1)
        self.assertEqual(robot.direction, "WEST")

    def test_left_rotates_robot_90_degrees_to_the_left_when_facing_south(self):
        robot = ToyRobot(1, 1, "SOUTH")
        robot.left()
        self.assertEqual(robot.x, 1)
        self.assertEqual(robot.y, 1)
        self.assertEqual(robot.direction, "EAST")

    def test_left_rotates_robot_90_degrees_to_the_left_when_facing_east(self):
        robot = ToyRobot(1, 1, "EAST")
        robot.left()
        self.assertEqual(robot.x, 1)
        self.assertEqual(robot.y, 1)
        self.assertEqual(robot.direction, "NORTH")

    def test_left_rotates_robot_90_degrees_to_the_left_when_facing_west(self):
        robot = ToyRobot(1, 1, "WEST")
        robot.left()
        self.assertEqual(robot.x, 1)
        self.assertEqual(robot.y, 1)
        self.assertEqual(robot.direction, "SOUTH")

    def test_right_rotates_robot_90_degrees_to_the_right_when_facing_north(self):
        robot = ToyRobot(4, 4, "NORTH")
        robot.right()
        self.assertEqual(robot.x, 4)
        self.assertEqual(robot.y, 4)
        self.assertEqual(robot.direction, "EAST")

    def test_right_rotates_robot_90_degrees_to_the_right_when_facing_south(self):
        robot = ToyRobot(4, 4, "SOUTH")
        robot.right()
        self.assertEqual(robot.x, 4)
        self.assertEqual(robot.y, 4)
        self.assertEqual(robot.direction, "WEST")

    def test_right_rotates_robot_90_degrees_to_the_right_when_facing_east(self):
        robot = ToyRobot(4, 4, "EAST")
        robot.right()
        self.assertEqual(robot.x, 4)
        self.assertEqual(robot.y, 4)
        self.assertEqual(robot.direction, "SOUTH")

    def test_right_rotates_robot_90_degrees_to_the_right_when_facing_west(self):
        robot = ToyRobot(4, 4, "WEST")
        robot.right()
        self.assertEqual(robot.x, 4)
        self.assertEqual(robot.y, 4)
        self.assertEqual(robot.direction, "NORTH")

    def test_report(self):
        robot = ToyRobot(0, 4, "EAST")
        x, y, direction = robot.report()
        self.assertEqual(x, 0)
        self.assertEqual(y, 4)
        self.assertEqual(direction, "EAST")

