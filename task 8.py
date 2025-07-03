try:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is equal to {fahrenheit}°F")
    fahrenheit2 = float(input("Now enter temperature in Fahrenheit: "))
    celsius2 = (fahrenheit2 - 32) * 5/9
    print(f"{fahrenheit2}°F is equal to {celsius2:.2f}°C")
except ValueError:
    print("Invalid input. Please enter numeric values only.")