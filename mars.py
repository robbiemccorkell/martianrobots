from itertools import islice

from grid import Grid
from position import Position
from robot import Robot

fileInput = open('input.txt')

gridSize = [int(i) for i in (fileInput.readline().split())]
grid = Grid(gridSize)

while True:
	nextRobotInput = list(islice(fileInput, 3))
	if not nextRobotInput:
		break
	
	robotPosition = Position(*nextRobotInput[0].split())
	robotInstructions = nextRobotInput[1]

	grid.processRobot(Robot(robotPosition), robotInstructions)

	if grid.lastRobotLost:
		print(grid.lastRobotPosition, ' LOST')
	else:
		print(grid.lastRobotPosition)