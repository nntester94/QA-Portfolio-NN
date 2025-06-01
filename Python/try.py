
try:
    result = 10 / 0
    number = int(input("enter a num:   "))
    print(number)

except ZeroDivisionError:
    print("divided by zero")
except ValueError as err:
    print("err")