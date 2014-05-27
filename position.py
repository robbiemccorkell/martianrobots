class Position:
	compass = ['N', 'E', 'S', 'W']

	def __init__(self, xPos, yPos, bearing):
		self.xPos = int(xPos)
		self.yPos = int(yPos)
		self.bearingIndex = self.compass.index(bearing)

	def moveForward(self):
		if self.compass[self.bearingIndex] == 'N':
			self.translate([0,1])
		elif self.compass[self.bearingIndex] == 'E':
			self.translate([1,0])
		elif self.compass[self.bearingIndex] == 'S':
			self.translate([0,-1])
		elif self.compass[self.bearingIndex] == 'W':
			self.translate([-1,0])

	def translate(self, vector):
		self.xPos += vector[0]
		self.yPos += vector[1]

	def rotateClockwise(self):
		self.bearingIndex += 1
		self.bearingIndex = self.bearingIndex % len(self.compass)

	def rotateAnticlockwise(self):
		self.bearingIndex -= 1
		self.bearingIndex = self.bearingIndex % len(self.compass)

	def __str__(self):
		return '{0} {1} {2}'.format(self.xPos, self.yPos, self.compass[self.bearingIndex])

	def __eq__(self, other):
		return self.xPos == other.xPos \
			and self.yPos == other.yPos \
			and self.bearingIndex == other.bearingIndex