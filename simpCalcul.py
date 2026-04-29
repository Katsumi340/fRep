def operations() :
    import operator
    import math
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }
    expression = input()
    for op in ops :
        if op in expression :
            a, b = expression.split(op)
            result = ops[op](float(a), float(b))
            print("result: ", result, "\n")
            break
    else :
        print("unvalid command")
while True :
    print("This is a calculatorrrrrrrrrrrr")
    print("If you want to Exit press 0, or every key to continue:")
    Exit = input("?:")
    if Exit == "0" :
        print("Goodbye")
        break
    else :
        print("Put your operation: ")
    calculator = operations()




