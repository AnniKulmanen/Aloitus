# questions.py tests can be found here
# ------------------------------------

import questions

# Test if conversion to integer as expected
def test_ask_user_integer(monkeypatch): # Simulate user input using Monkeypathc library
    user_input = '100'
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    question = questions.Question('Anna kokonaisluku')
    assert question.ask_user_integer(False) == (100, 'OK', 0, 'Conversion successful') 
    
# Test if conversion to float works as expected
def test_ask_user_float(monkeypatch): 
    user_input = '1.5'
    # Use anonymous function to create input from variable
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    question = questions.Question('Anna liukuluku') 
    assert question.ask_user_float(False) == (1.5, 'OK', 0, 'Conversion successful') 

# Test an error condition when user adds a unit to a floating point number
def test_ask_user_float2(monkeypatch):
    user_input = '1.5v'
    # Use anonymous function to create input from variable
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    question = questions.Question('Anna kokonaisluku') 
    assert question.ask_user_float(False) == (0, 'Error', 1, "could not convert string to float: '1.5v'")
    
# Test an error condition when users uses comma instead of dot as decimal separator
def test_ask_user_float3(monkeypatch):
    user_input = '74,6'
    # Use anonymous function to create input from variable
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    question = questions.Question('Anna kokonaisluku')
    assert question.ask_user_float(False) == (0, 'Error', 1, "could not convert string to float: '74,6'")

# Test conversion to boolean: case Y
def test_ask_user_boolean(monkeypatch): 
    user_input = 'y'
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    question = questions.Question('Haluatko jatkaa') 
    assert question.ask_user_boolean('Y', 'N', False) == (True, 'OK', 0, 'Conversion successful')

# Test conversion to boolean: case N
def test_ask_user_boolean2(monkeypatch): 
    user_input = 'n'
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    question = questions.Question('Haluatko jatkaa') 
    assert question.ask_user_boolean('Y', 'N', False) == (False, 'OK', 0, 'Conversion successful')

# Test an error condition
def test_ask_user_boolean3(monkeypatch): 
    user_input = 'v'
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    question = questions.Question('Haluatko jatkaa') 
    assert question.ask_user_boolean('Y', 'N', False) == ('N/A', 'Error', 1, 'unable to convert to boolean')

# Change methods to static or class methods and test again 