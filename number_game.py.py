import random
score=0
com_scor=0
i=0
while i<5:
    com_no=random.randint(1,10)
    user_no=int(input("chosse you no(1 to 10):  "))
    if com_no>user_no:
        com_scor+=1
        print("YOU LOSS")
        print("computer no is ",com_no)
    elif com_no<user_no:
        score+=1
        print("computer no is ",com_no)     
    else:
        print(com_no)
    i+=1

if score<com_scor:
    print("YOU LOSS")
    print("computer score",com_scor)
elif score>com_scor:
    print("YOU WIN")
    print("your score",score)
else:
    print("DRAW")

