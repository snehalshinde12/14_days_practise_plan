#!/usr/bin/env python3
import sys


def calculate(a, operator, b):
    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b
    if operator == "/":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    if operator == "**":
        return a ** b
    raise ValueError("Unsupported operator")


def main():
    if len(sys.argv) == 4:
        try:
            first = float(sys.argv[1])
            operator = sys.argv[2]
            second = float(sys.argv[3])
        except ValueError:
            print("Please enter valid numbers.")
            return
    else:
        try:
            first = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /, **): ")
            second = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            return

    try:
        result = calculate(first, operator, second)
        print(f"Result: {result}")
    except ZeroDivisionError as error:
        print(error)
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()
