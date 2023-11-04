def Div(fNumber,sNumber):
    if fNumber % sNumber == 0:
        print(f"Result: {True}")
    else:
        print(f"Result: {False}")
    return fNumber % sNumber
print(Div(45,6))