
def box():
    # User se size input lene ke liye
    a = int(input("Box ka size enter karein: "))
    b = "*"
    for i in range(a):
        for j in range(a):
            if i == 0 or i == a - 1 or j == 0 or j == a - 1:
                print(b, end=" ")
            else:
                print(" ", end=" ")
        print() 

# Function call
box()