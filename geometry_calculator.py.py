import math

def calculate_area():
    print("\n--- GEOMETRY AREA CALCULATOR ---")
    print("1. Square")
    print("2. Triangle")
    print("3. Rectangle")
    print("4. Circle")
    print("5. Ellipse")
    print("6. Exit")
    
    choice = input("\nEnter your choice (1-6): ")

    if choice == '1':
        s = float(input("Enter side: "))
        print(f"Area: {s * s} sq units")
    
    elif choice == '2':
        b = float(input("Enter base: "))
        h = float(input("Enter height: "))
        print(f"Area: {0.5 * b * h} sq units")
        
    elif choice == '3':
        l = float(input("Enter length: "))
        w = float(input("Enter width: "))
        print(f"Area: {l * w} sq units")
        
    elif choice == '4':
        r = float(input("Enter radius: "))
        print(f"Area: {math.pi * r * r:.2f} sq units")
        
    elif choice == '5':
        a = float(input("Enter axis a: "))
        b = float(input("Enter axis b: "))
        print(f"Area: {math.pi * a * b:.2f} sq units")
        
    elif choice == '6':
        print("Exiting...")
        return False
    else:
        print("Invalid choice!")
    return True

# Main Loop
while True:
    if not calculate_area():
        break