from calc_art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


print(logo)
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide

}


def calculate():
    num1 = float(input("first number: "))
    for sym in operations:
        print(sym)
    cont = True

    while cont:
        oper = input("Pick an operation : ")
        num2 = float(input("Next number: "))
        calc_fn = operations[oper]
        result = calc_fn(num1, num2)
        print(f"{num1} {oper} {num2} = {result}")
        if input(f"enter y to continue with {result} or n to start new Calculation") == 'y':
            num1 = result
        else:
            cont = False
            calculate()


calculate()
