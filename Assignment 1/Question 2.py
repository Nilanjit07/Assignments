def start_calculator():
    def add(number1, number2):
        return number1 + number2
    def subtract(number1, number2):
        return number1 - number2
    def multiple(number1, number2):
        return number1 * number2
    def divide(number1, number2):
        if(number2!=0):
            return number1 / number2
    start = True
    mathematical_operations = {
        "+": add,
        "-": subtract,
        "*": multiple,
        "/": divide,
    }
    while start:
        number1 = float(input("What's the first number?:"))
        for operation in mathematical_operations:
            print(operation)
        symbol = input("What's the mathematical operation? Choose one from the list above: ")
        if symbol not in mathematical_operations:
            continue
        number2 = float(input("What's the second number?:"))
        operation = mathematical_operations[symbol]
        result = operation(number1, number2)
        if({symbol} == "/"):
            if(number2!=0):
                print(f"{number1} {symbol} {number2} = {result}")
            else:
                print("Value is Infinity.")
        else:
            print(f"{number1} {symbol} {number2} = {result}")
        another_operation = True
        while another_operation:
            symbol = input("Pick another operation to perform on the current result, type 's' to start "
                           "over, or type 'q' to quit.").lower()
            if symbol == "q":
                start = False
                break
            elif symbol == "s":
                start = True
                another_operation = False
            elif symbol not in mathematical_operations:
                continue
            else:
                operation = mathematical_operations[symbol]
                number2 = float(input("What's the second number?:"))
                result = operation(result, number2)
                print(result)
if __name__ == "__main__":
    start_calculator()
