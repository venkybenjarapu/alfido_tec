3rd code
# temperature_converter.py

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def kelvin_to_celsius(k):
    return k - 273.15

def convert_temperature():
    print("🌡 Temperature Converter")
    print("Choose conversion type:")
    print("1. Celsius to Fahrenheit")
    print("2. Celsius to Kelvin")
    print("3. Fahrenheit to Celsius")
    print("4. Kelvin to Celsius")
    print("5. Exit")

    while True:
        choice = input("Enter your choice (1–5): ")

        if choice == '5':
            print("Exiting converter. Goodbye!")
            break

        try:
            temp = float(input("Enter temperature value: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue

        if choice == '1':
            result = celsius_to_fahrenheit(temp)
            print(f"{temp}°C = {result:.2f}°F")
        elif choice == '2':
            result = celsius_to_kelvin(temp)
            print(f"{temp}°C = {result:.2f}K")
        elif choice == '3':
            result = fahrenheit_to_celsius(temp)
            print(f"{temp}°F = {result:.2f}°C")
        elif choice == '4':
            result = kelvin_to_celsius(temp)
            print(f"{temp}K = {result:.2f}°C")
        else:
            print("Invalid choice. Please select between 1–5.")

if _name_ == "_main_":
    convert_temperature()