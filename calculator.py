# Simple calculator using lambda functions
add = lambda x, y: x + y
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
divide = lambda x, y: x / y if y != 0 else 'Error: Division by zero'


if __name__ == "__main__":
    print("Calculator app running!")
    print("Addition: 2 + 3 =", add(2, 3))
    print("Subtraction: 5 - 2 =", subtract(5, 2))
    print("Multiplication: 3 * 4 =", multiply(3, 4))
    print("Division: 10 / 2 =", divide(10, 2))
    print("Division by zero: 10 / 0 =", divide(10, 0))
