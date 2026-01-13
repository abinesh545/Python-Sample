def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    if b==0:
        raise ValueError("Cannot Divide by Zero")
    return a//b
def modulo(a,b):
    return a%b
