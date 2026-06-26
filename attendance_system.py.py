    
import csv


with open("aman.csv", "w", newline='') as fh:
    stuwriter = csv.writer(fh)
    stuwriter.writerow(["roll no", "name", "attendence"])
    
    # Adjusted range to handle clear student numbering
    num_students = 2
    for i in range(1, num_students + 1):
        print(f"--- Student Record {i} ---")
        rollno = i
        name = input("Enter name: ").strip()
        attendance = input("Enter attendance (A-Absent, P-Present): ").strip().upper()
        
        stuwriter.writerow([rollno, name, attendance])

print("Record inserted successfully.")