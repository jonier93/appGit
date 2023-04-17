class View:
    def __init__(self):
        print("Enter the option: \n" 
                "1. Add \n"
                "2. Substract \n" 
                "3. Multiply \n"
                "4. Divide \n")
        self.option = input()
        print("Enter the number 1: ")
        self.num1 = input()
        print("Enter the number 2: ")
        self.num2 = input()
    