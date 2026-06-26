class VehicleShop:
    def __init__(self, cycle, bike, car):
        # Initial stock setup
        self.cycle = cycle
        self.bike = bike
        self.car = car

    def display_stock(self):
        print(f"\n--- CURRENT STOCK ---")
        print(f"Cycles: {self.cycle} | Bikes: {self.bike} | Cars: {self.car}")
        print("---------------------")

    def rent_vehicle(self, vehicle_type, qty):
        # Validation: Check if quantity is positive
        if qty <= 0:
            print("Error: Please enter a quantity greater than zero.")
            return

        # Logic for Renting based on vehicle type
        if vehicle_type == 1: # Cycle
            if qty <= self.cycle:
                self.cycle -= qty
                print(f"Success! Total price: {qty * 100}. Remaining Cycles: {self.cycle}")
            else:
                print("Sorry, not enough Cycles in stock.")
        
        elif vehicle_type == 2: # Bike
            if qty <= self.bike:
                self.bike -= qty
                print(f"Success! Total price: {qty * 200}. Remaining Bikes: {self.bike}")
            else:
                print("Sorry, not enough Bikes in stock.")
        
        elif vehicle_type == 3: # Car
            if qty <= self.car:
                self.car -= qty
                print(f"Success! Total price: {qty * 300}. Remaining Cars: {self.car}")
            else:
                print("Sorry, not enough Cars in stock.")
        else:
            print("Invalid vehicle choice!")

# Object creation (Loop ke bahar taaki stock update rahe)
obj = VehicleShop(100, 80, 50)

while True:
    try:
        print("\n--- VEHICLE RENTAL SYSTEM ---")
        uc = int(input("1. Display Stock\n2. Rent Vehicle\n3. Exit\n-- "))
        
        if uc == 1:
            obj.display_stock()
            
        elif uc == 2:
            vehicle = int(input("Select vehicle:\n1. Cycle\n2. Bike\n3. Car\n-- "))
            request = int(input("Enter the quantity: "))
            obj.rent_vehicle(vehicle, request)
            
        elif uc == 3:
            print("Thank you for using our system!")
            break
        else:
            print("Invalid choice! Please try again.")
            
    except ValueError:
        print("Error: Please enter a valid number.")