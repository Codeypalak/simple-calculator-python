historyfile = "history.txt"

def show_history():
    file = open(historyfile, "r")
    lines = file.readlines()

    if len(lines) == 0:
        print("no history found")
    else:
        for line in reversed(lines):
            print(line.strip())

    file.close()


def clear_history():
    file = open(historyfile, 'w')
    file.close()
    print("clear history!")


def save_to_history(equation, result):
    file = open(historyfile, "a")
    file.write(equation + "=" + str(result) + "\n")
    file.close()


def calculate(user_input):
    user_input = user_input.split()

    if len(user_input) != 3:
        print("invalid input.Use format(e.g: 8 + 8)")
        return

    num1 = float(user_input[0])
    op = user_input[1]
    num2 = float(user_input[2])

    if op == "+":
        result = num1 + num2

    elif op == "-":
        result = num1 - num2

    elif op == "*":
        result = num1 * num2

    elif op == "/":
        if num2 == 0:
            print("cannot divide by zero")
            return
        result = num1 / num2

    else:
        print("invalid operation")
        return

    if int(result) == result:
        result = int(result)

    print("Result:", result)
    save_to_history("".join(user_input), result)


def main():
    print("---simple calculator(type-history,clear, or exit)")

    while True:
        user_input = input("enter calculation(+ - * /): ")

        if user_input == "exit":
            print("goodbye!")
            break

        elif user_input == "history":
            show_history()

        elif user_input == "clear":
            clear_history()

        else:
            calculate(user_input)


main()