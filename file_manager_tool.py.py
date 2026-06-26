import os

while True:
    try:
        i = int(input("\n--- FILE MANAGER ---\n1. Create File\n2. Read File\n3. Append Data\n4. Delete File\n5. Exit\nChoice: "))
        
        if i == 1:
            file_name = input("Enter file name: ")
            with open(file_name, "w") as f:
                for d in range(1, 4): # Example ke liye 3 entries
                    data = input(f"Enter name {d}: ")
                    f.write(data + "\n")
            print("File created successfully.")

        elif i == 2:
            file_name = input("Enter file name to read: ")
            if os.path.exists(file_name):
                with open(file_name, "r") as f:
                    print("\n--- CONTENT ---")
                    print(f.read())
            else:
                print("Error: File not found!")

        elif i == 3:
            file_name = input("Enter file name to update: ")
            data = input("Enter new data: ")
            with open(file_name, "a") as f:
                f.write(data + "\n")
            print("Data added.")

        elif i == 4:
            file_name = input("Enter file name to delete: ")
            if os.path.exists(file_name):
                os.remove(file_name)
                print("File deleted.")
            else:
                print("File does not exist.")

        elif i == 5:
            break
        else:
            print("Invalid choice!")
            
    except Exception as e:
        print(f"An error occurred: {e}")