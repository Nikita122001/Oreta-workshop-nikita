try:
    def add_numbers(a, b):
    
        return a + b 
    num1 = float(input("a: "))
    num2 = float(input("b: "))

    result = add_numbers(num1, num2)

    print(result)
except ValueError:
    print("Invalid input")
