pi_value = 22/7

# Har shape ke liye alag function
def sphere_area():
    r = float(input("Enter Radius: "))
    print(f"Surface Area of Sphere: {4 * pi_value * r * r:.2f} m2")

def cuboid_area():
    l = float(input("Enter Length: "))
    w = float(input("Enter Width: "))
    h = float(input("Enter Height: "))
    print(f"Surface Area of Cuboid: {2 * (l*w + l*h + w*h):.2f} m2")

def cylinder_area():
    r = float(input("Enter Radius: "))
    h = float(input("Enter Height: "))
    print(f"Surface Area of Cylinder: {2 * pi_value * r * (r + h):.2f} m2")

def cone_area():
    r = float(input("Enter Radius: "))
    h = float(input("Enter Height: "))
    l = (r**2 + h**2)**0.5
    print(f"Area of Cone: {pi_value * r * (r + l):.2f} m2")

# MENU Function
def show_menu():
    print("\n--- 3D SHAPE CALCULATOR MENU ---")
    print("1. Area of Sphere")
    print("2. Area of Cuboid")
    print("3. Area of Cylinder")
    print("4. Area of Cone")
    print("5. Exit")

# Main Loop
while True:
    show_menu()
    choice = int(input("ENTER YOUR CHOICE (1-5): "))

    if choice == 1: sphere_area()
    elif choice == 2: cuboid_area()
    elif choice == 3: cylinder_area()
    elif choice == 4: cone_area()
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.")