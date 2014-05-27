from itertools import islice

from grid import Grid
from position import Position

fileInput = open('input.txt')

gridSize = map(int, fileInput.readline().split())
grid = Grid(gridSize)

while True:
	nextRobotInput = list(islice(fileInput, 3))
	if not nextRobotInput:
		break
	
	robotPosition = Position(*nextRobotInput[0].split())
	robotInstructions = nextRobotInput[1]

	grid.processRobot(robotPosition, robotInstructions)