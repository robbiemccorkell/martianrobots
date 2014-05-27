import copy

from robot import Robot

class Grid:
	def __init__(self, size):
		self.size = size
		self.lostPositions = []
		self.lastRobotLost = False

	def processRobot(self, robot, robotInstructions):
		self.lastRobotLost = False
		for instruction in robotInstructions:
			lastKnownPos = copy.deepcopy(robot.position)
			robot.processInstruction(instruction, self.lostPositions)
			if (self.isOutOfBounds(robot.position)):
				self.lastRobotLost = True
				self.lostPositions.append(lastKnownPos)
				break

		if self.lastRobotLost:
			self.lastRobotPosition = lastKnownPos
		else:
			self.lastRobotPosition = robot.position

	def isOutOfBounds(self, position):
		return position.xPos > self.size[0] or position.yPos > self.size[1]