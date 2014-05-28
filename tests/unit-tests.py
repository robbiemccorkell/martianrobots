import unittest
from unittest.mock import MagicMock
from position import Position
from robot import Robot
from grid import Grid

class PositionTestCase(unittest.TestCase):

	def setUp(self):
		self.position = Position('3', '2', 'N')

	def test_initPosition(self):
		self.assertEqual(self.position.xPos, 3)
		self.assertEqual(self.position.yPos, 2)
		self.assertEqual(self.position.bearingIndex, 0)

	def test_moveForward(self):
		self.position.moveForward()

		self.assertEqual(self.position, Position(3, 3, 'N'))

	def test_rotate(self):
		self.position.rotateClockwise()
		self.position.rotateClockwise()
		self.position.rotateAnticlockwise()

		self.assertEqual(self.position, Position(3, 2, 'E'))

	def test_chainedCommands(self):
		self.position.rotateAnticlockwise()
		self.position.moveForward()
		self.position.rotateAnticlockwise()
		self.position.moveForward()

		self.assertEqual(self.position, Position(2, 1, 'S'))

	def test_toString(self):
		self.assertEqual(str(self.position), '3 2 N')



class RobotTestCase(unittest.TestCase):

	def setUp(self):
		self.position = Position('3', '2', 'N')
		self.position.rotateClockwise = MagicMock()
		self.position.rotateAnticlockwise = MagicMock()
		self.position.moveForward = MagicMock()

		self.robot = Robot(self.position)

	def test_initRobot(self):
		self.assertEqual(self.robot.position, self.position)


	def test_rotation(self):
		self.robot.processInstruction('R', [])
		self.robot.processInstruction('R', [])
		self.robot.processInstruction('L', [])

		self.position.rotateClockwise.assert_called()
		self.position.rotateAnticlockwise.assert_called()
		self.assertEqual(self.position.rotateClockwise.call_count, 2)

	def test_movement(self):
		self.robot.processInstruction('F', [])

		self.position.moveForward.assert_called()

	def test_lostPosition(self):
		self.robot.processInstruction('F', [self.position])

		self.assertFalse(self.robot.position.moveForward.called)



class GridTestCase(unittest.TestCase):

	def setUp(self):
		self.robot = Robot(Position('3', '2', 'N'))
		self.robot.processInstruction = MagicMock()

		self.grid = Grid([3,2])

	def test_initGrid(self):
		self.assertEqual(self.grid.size, [3,2])

	def test_isOutOfBounds(self):
		outOfBounds = self.grid.isOutOfBounds(Position('4', '2', 'N'))

		self.assertTrue(outOfBounds)

	def test_processRobotInstruction(self):
		self.grid.processRobot(self.robot, 'RFRF')

		self.assertEqual(self.robot.processInstruction.call_count, 4)

	def test_robotOutOfBounds(self):
		self.robot.position = Position(4, 2, 'N')

		self.grid.processRobot(self.robot, 'F')

		self.assertTrue(self.grid.lastRobotLost)
		self.assertEqual(len(self.grid.lostPositions), 1)


if __name__ == '__main__':
    unittest.main()