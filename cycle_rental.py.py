class CycleShop:
    def __init__(self, stock):
        self.stock = stock  # Initial stock set karna

    def display_cycle(self):
        print(f"\nTotal cycles currently available: {self.stock}")

    def rent_for_cycle(self, qty):
        if qty <= 0:
            print("Please enter a positive value greater than zero.")
        elif qty > self.stock:
            print(f"Sorry, only {self.stock} cycles are available.")
        else:
            self.stock -= qty  # Stock ko update karna
            print(f"Total price: {qty * 100}")
            print(f"Remaining cycles: {self.stock}")

# Object bahar banaya taaki stock update rahe
obj = CycleShop(100)

while True:
    try:
        uc = int(input("\n--- CYCLE RENTAL SYSTEM ---\n1. Display Stock\n2. Rent Cycle\n3. Exit\nChoose: "))
        if uc == 1:
            obj.display_cycle()
        elif uc == 2:
            request = int(input("Enter quantity to rent: "))
            obj.rent_for_cycle(request)
        elif uc == 3:
            print("Thank you for visiting!")
            break
        else:
            print("Invalid choice, please try again.")
    except ValueError:
        print("Please enter a valid number.")