import unittest

from toy_robot import ToyRobot


class ToyRobotTest(unittest.TestCase):
    def setUp(self):
        return

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
        robot.place(6, 3, "WEST")
        self.assertRaises(NameError)

    def test_place_with_invalid_direction_raises_error(self):
        robot = ToyRobot()
        robot.place(0, 3, "DOWN")
        self.assertRaises(NameError)

    def test_move_robot_add_1_step_towards_direction(self):
        robot = ToyRobot(0, 3, "EAST")
        robot.move()
        self.assertEqual(robot.x, 1)
        self.assertEqual(robot.y, 3)
        self.assertEqual(robot.direction, "EAST")

    def test_move_prevent_robot_from_falling(self):
        robot = ToyRobot(0, 4, "NORTH")
        robot.move()
        self.assertEqual(robot.x, 0)
        self.assertEqual(robot.y, 4)
        self.assertEqual(robot.direction, "NORTH")

    def test_left_rotate_robot_90_degrees_to_the_left(self):
        robot = ToyRobot(1, 1, "SOUTH")
        robot.left()
        self.assertEqual(robot.x, 1)
        self.assertEqual(robot.y, 1)
        self.assertEqual(robot.direction, "EAST")

    def test_right_rotate_robot_90_degrees_to_the_right(self):
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

