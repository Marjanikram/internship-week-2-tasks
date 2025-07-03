user_input = input("Enter any value: ")

try:
    val = int(user_input)
    print("You entered an integer.")
except ValueError:
    try:
        val = float(user_input)
        print("You entered a float.")
    except ValueError:
        val = user_input
        print("You entered a string.")

print("Python guesses the type as:", type(val))
