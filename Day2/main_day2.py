from operations import add


def main():
    while True:
        print("1. Add")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            first_number = float(input("Enter first number: "))
            second_number = float(input("Enter second number: "))
            result = add(first_number, second_number)
            print("Result:", result)
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
