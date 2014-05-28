from behave import *
import mars

@given('valid input stored in "{inputFileName}"')
def step_impl(context, inputFileName):
	context.inputFileName = inputFileName

@when('I process the input')
def step_impl(context):
	context.output = mars.readInput(context.inputFileName)

@then('I should see the output')
def step_impl(context):
	output = context.stdout_capture.getvalue().strip()
	expected = context.text

	assert output == expected, "Got %s" % output