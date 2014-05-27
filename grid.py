import copy

from robot import Robot

class Grid:
	def __init__(self, size):
		self.size = size
		self.lostPositions = []

	def processRobot(self, robotPosition, robotInstructions):
		robot = Robot(robotPosition)

		isLost = False
		for instruction in robotInstructions:
			lastKnownPos = copy.deepcopy(robot.position)
			robot.processInstruction(instruction, self.lostPositions)
			if (self.isOutOfBounds(robot.position)):
				isLost = True
				self.lostPositions.append(lastKnownPos)
				break

		if isLost:
			print str(lastKnownPos) + ' LOST'
		else:
			print robot.position

	def isOutOfBounds(self, position):
		return position.xPos > self.size[0] or position.yPos > self.size[1]