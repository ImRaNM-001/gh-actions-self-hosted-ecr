from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 13)['result'] == 15

def test_subtract():
    assert subtract(5, 18)['result'] == -13

def test_multiply():
    assert multiply(3, 4)['result'] == 12

def test_divide():
    assert divide(90, 2)['result'] == 45.0
    assert divide(10, 0)['result'] == 'Error: Division by zero not feasible'
