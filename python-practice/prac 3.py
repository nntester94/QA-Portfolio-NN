

#def double(n):
    #return n * 2
#n =  int(input("Enter a number: "))

#result = double(n)
#print ("result:", result)

def greet(name,country = "uk" ):
    print("Hello,", name , "you are from" , country)

# Get input from the user
user_name = input("Enter your name: ")

# Call the function using the input
greet(user_name)