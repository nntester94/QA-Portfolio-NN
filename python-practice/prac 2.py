def math_operations(a, b):
    sum_ = a + b
    difference = a - b
    product = a * b
    average = (a + b) / 2
    return sum_, difference, product, average

while True:
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        sum_, difference, product, average = math_operations(a, b)

        print("\n✅ Results:")
        print("Sum:", sum_)
        print("Difference:", difference)
        print("Product:", product)
        print("Average:", average)

    except ValueError:
        print("❌ Invalid input! Please enter numeric values only.")
        continue  # Ask again

    # Ask if the user wants to try again
    again = input("\nDo you want to try again? (yes/no): ").strip().lower()
    if again != "yes":
        print("👋 Exiting... Have a great day!")
        break
