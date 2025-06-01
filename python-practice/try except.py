
def valid_input():
    while True:
       try:
           num = int(input("Enter a number: "))
           print(f"Thankyou! You entered:{num}")
           break
       except ValueError:
           print("That's not a number, try again!")

valid_input()

