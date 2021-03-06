import argparse
from itertools import islice

from grid import Grid
from position import Position
from robot import Robot

def readInput(path):
	fileInput = open(path)

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
			print "%s LOST" % grid.lastRobotPosition
		else:
			print grid.lastRobotPosition


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Drive robots around a grid')
	parser.add_argument('file', metavar='file', type=str, help='a .txt input file to parse')
	args = parser.parse_args()

	readInput(args.file)