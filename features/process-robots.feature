Feature: Process Robots
	Given valid input the program should process the mars robots and give the expected output

	Scenario: One Robot
		Given valid input stored in "features/one-robot-input.txt"
		When I process the input 
		Then I should see the output
		"""
		1 1 E
		"""

	Scenario: Lost Robot
		Given valid input stored in "features/lost-robot-input.txt"
		When I process the input 
		Then I should see the output
		"""
		1 1 E
		3 3 N LOST
		"""

	Scenario: Blocked Robot
		Given valid input stored in "features/blocked-robot-input.txt"
		When I process the input
		Then I should see the output
		"""
		1 1 E
		3 3 N LOST
		2 3 S
		"""