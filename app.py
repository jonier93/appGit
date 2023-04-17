#Hi
class Calculator:    
    num1 = 0
    num2 = 0

    def setNum1():
        global num1
        print("Enter the number 1: ")
        num1 = input()                

    def setNum2():    
        global num2    
        print("Enter the number 2: ")
        num2 = input()

    def getNum1():
        global num1
        return num1
    
    def getNum2():
        global num2
        return num2    

    def add(num1, num2):
        result = int(num1) + int(num2)
        print("The operation result is: ", result)
    
    def substraction(num1, num2):
        result = int(num1) - int(num2)
        print("The operation result is: ", result)
    
    def multiply(num1, num2):
        result = int(num1) * int(num2)
        print("The operation result is: ", result)
    
    def divide(num1, num2):
        result = int(num1) / int(num2)
        print("The operation result is: ", result)

    setNum1()
    setNum2()
    add(getNum1(), getNum2())
    substraction(getNum1(), getNum2())
    multiply(getNum1(), getNum2())
    divide(getNum1(), getNum2())

