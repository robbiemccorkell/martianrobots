#Martian Robots

Red Badger developer tech test https://travis-ci.org/robbiemccorkell/martianrobots.svg?branch=master

##Intro

This implementation is written in python and parses input from a .txt file defined as a command-line parameter. It processes the instructions in this file, and outputs the result to the terminal's standard output.

Unit tests are provided using python's built in framework [unittest](https://docs.python.org/2/library/unittest.html), and integration tests are provided by [behave](http://pythonhosted.org/behave/). Example input from the brief is provided in input.txt. All input is assumed to be valid.

##Usage

To run the program navigate to the root directory and run
```bash
python mars.py input.txt
```

To run the unit tests run
```bash
python -m unittest unit-tests
```

And to run the integration tests simply run
```bash
behave
```

##Requirements
Requirements are listed within requirements.txt to be installed with pip
```bash
pip install -r requirements.txt
```
These requirements include
* Python 2.7
* [mock](https://pypi.python.org/pypi/mock) - A python mocking library
* [behave](http://pythonhosted.org/behave/) - BDD integration testing for python