# simple_program.py

def greet(name):
    print(f"Hello, {name}! Welcome to Python programming.")

def add_numbers(a, b):
    return a + b

if __name__ == "__main__":
    # Greet the user
    greet("Alice")

    # Add two numbers
    num1 = 10
    num2 = 5
    result = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is {result}")