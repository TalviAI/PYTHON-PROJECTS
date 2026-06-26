print("Area of triangle (Heron's formula)")

a = int(input("Enter the a: "))
b = int(input("Enter the b: "))
c = int(input("Enter the c: "))

s = (a + b + c) / 2
# Heron's formula: sqrt(s * (s-a) * (s-b) * (s-c))
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

print(f"Area of triangle (Heron's formula): {area:.2f} m2")

input("Enter to Exit")