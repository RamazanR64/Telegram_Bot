# # Name input
# name = input("Как вас зовут? ").strip()
# if name:
#     print("Hello," + name + "!")
# else:
#     print("You dont enter the name")
#
# # Odd Even
# while True:
#     try:
#         number = int(input("Input number:"))
#         break
#     except ValueError:
#         print("Error, enter number")
#
# if number % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")


# Calculator
def get_numbers():
    while True:
        try:
            number1 = float(input("Введите первое число:"))
            number2 = float(input("Введите второе число:"))
            return number1, number2
        except ValueError:
            print("Error: enter number")


def calculate(number1, number2, operation):
    if operation == "+":
        return number1 + number2
    elif operation == "-":
        return number1 - number2
    elif operation == "*":
        return number1 * number2
    elif operation == "/":
        if number2 != 0:
            return number1 / number2
        else:
            return "Ошибка, делить на ноль нельзя!"
    else:
        return "Неизвестный оператор"


def get_operator():
    while True:
        operation = input("Input operator (+, -, *, /)").strip()
        if operation in ["+", "-", "*", "/"]:
            return operation
        else:
            print("Error: enter correct operator (+, -, *, /)")


while True:
    number1, number2 = get_numbers()

    operation = get_operator()

    result = calculate(number1, number2, operation)

    print(f"Result: {result}")

    again = input("Do you want make"
                  " some new operations? "
                  "(yes/no):").strip().lower()
    if again != "yes":
        print("Goodbye!")
        break
