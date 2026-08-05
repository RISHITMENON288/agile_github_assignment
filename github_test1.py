# github_test.py - Version 1

def greet(name):
    return f"Hello, {name}! Welcome to Git version control."

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

name = input("Enter your name: ")
print(greet(name))

print("\n--- Simple Calculator ---")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")