pi_value = 22/7
history_list = [] # Purani calculations store karne ke liye

while True:
    q = int(input('''\nType of equation
                    1. Area of Square
                    2. Area of Triangle
                    3. Area of Rectangle
                    4. Area of Circle
                    5. Area of Ellipse
                    6. Show History
                    7. Exit
                    Enter your choice :- '''))
    
    result = 0
    
    if q == 1:
        s1 = float(input("Enter side 1: "))
        s2 = float(input("Enter side 2: "))
        result = s1 * s2
        print(f"Area of square: {result:.2f} sq units")
        
    elif q == 2:
        b = float(input("Enter base: "))
        h = float(input("Enter height: "))
        result = 0.5 * b * h
        print(f"Area of Triangle: {result:.2f} sq units")
        
    elif q == 3:
        rb = float(input("Enter base: "))
        rh = float(input("Enter height: "))
        result = rb * rh
        print(f"Area of Rectangle: {result:.2f} sq units")
        
    elif q == 4:
        r = float(input("Enter Radius: "))
        result = pi_value * r * r
        print(f"Area of Circle: {result:.2f} sq units")
        
    elif q == 5:
        a = float(input("Enter Axis a: "))
        b = float(input("Enter Axis b: "))
        result = pi_value * a * b
        print(f"Area of Ellipse: {result:.2f} sq units")
        
    elif q == 6:
        print("\n--- CALCULATION HISTORY ---")
        for item in history_list:
            print(item)
        continue # Wapas menu par jane ke liye
        
    elif q == 7:
        break
    else:
        print("Invalid choice!")
        continue

    # Result ko history mein save karna
    history_list.append(f"Area result: {result:.2f}")

print("Program closed. Goodbye!")