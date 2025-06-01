
def math_operations(a, b):
    sum_ = a + b
    difference = a - b
    product = a * b
    try:
        average = (a + b) / 2
    except ZeroDivisionError:
        average = "Undefined (division by zero)"
    return sum_, difference, product, average

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

except ValueError:
    print("⚠️ Invalid input! Please enter numbers only.")

sum_, difference, product, average = math_operations(a, b)

print("\nResults:")
print("Sum:", sum_)
print("Difference:", difference)
print("Product:", product)
print("Average:", average)
