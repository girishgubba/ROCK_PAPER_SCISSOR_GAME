print("Choices:")
print("1.ROCK")
print("2.PAPER")
print("3.SCISSOR")
n = int(input("Enter no.of Times You want to play:"))
i = 0
for i in range(1,n+1):
 p1 = int(input("Enter Person1 Choice:"))
 p2 = int(input("Enter Person2 Choice:"))
 if(p1 == p2):
    print("Play Again")
    continue
 elif((p1 == 1) & (p2 == 2)):
    print("Person2 Won")
 elif((p1 == 1) & (p2 == 3)):
    print("Person1 Won")
 elif((p1 == 2) & (p2 == 1)):
    print("Person1 Won")
 elif((p1 == 2) & (p2 == 3)):
    print("Person2 Won")
 elif((p1 == 3) & (p2 == 1)):
    print("Person2 Won")
 elif((p1 == 3) & (p2 == 2)):
    print("Person1 Won")
 elif((p1 == 2) & (p2 == 1)):
    print("Person1 Won")
 elif((p1 == 3) & (p2 == 1)):
    print("Person 2 Won")
 elif(p1,p2 != 1,2,3):
    print("Prefer the given choices")
print("Game Over")

