from position import Position

class Robot:
	def __init__(self, position):
		self.position = position

	def processInstruction(self, instruction, lostPositions):
		if instruction == 'R':
			self.position.rotateClockwise()
		elif instruction == 'L':
			self.position.rotateAnticlockwise()
		elif instruction == 'F':
			if self.position not in lostPositions:
				self.position.moveForward()