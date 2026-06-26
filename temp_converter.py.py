def fahrenheit_to_celsius():
    f = float(input("Enter temperature in °F: "))
    c = (f - 32) * 5/9
    print(f"Temperature in Celsius: {c:.2f}°C")

def celsius_to_fahrenheit():
    c = float(input("Enter temperature in °C: "))
    f = (c * 9/5) + 32
    print(f"Temperature in Fahrenheit: {f:.2f}°F")

while True:
    print("\n--- TEMPERATURE CALCULATOR ---")
    print("1. Convert °F to °C")
    print("2. Convert °C to °F")
    print("3. Exit")
    
    choice = input("ENTER YOUR CHOICE: ")

    if choice == '1':
        fahrenheit_to_celsius()
    elif choice == '2':
        celsius_to_fahrenheit()
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice, please try again.")