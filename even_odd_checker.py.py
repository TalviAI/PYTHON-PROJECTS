while True:
    try:
        # User se input lena
        n1 = int(input("\nEnter a number (or enter '0' to exit): "))
        
        # Exit condition add karna (Optional)
        if n1 == 0:
            print("Exiting...")
            break
            
        # Logic check
        if n1 % 2 == 0:
            print(f"{n1} is even (Sum/Sam number)")
        else:
            print(f"{n1} is odd (Visham number)")
            
    except ValueError:
        print("Invalid input! Please enter a valid integer.")