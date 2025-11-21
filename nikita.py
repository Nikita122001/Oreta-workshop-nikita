try:
    number = float(input("enter the statement temp"))
    f = (number*9/5) + 32
    print(f)
except ValueError:
    print("Invalid input")

