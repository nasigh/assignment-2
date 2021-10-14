import random
print("Welcome")
while (True):
    User = int(input("Please Enter Your Number :"))
    PC1 = random.randint(1, 2)
    PC2 = random.randint(1, 2)
    if PC1 == PC2 and PC2 != User :
        print("YOU WIN ","\U0001F91A","\U0001F91A","\U0001F590")
    elif PC2 == User and User != PC1 :
        print("COMPUTER 1 IS WINNER ","\U0001F590","\U0001F91A","\U0001F91A")
    elif PC1 == User and User != PC2 :
        print("COMPUTER 2 IS WINNER ","\U0001F91A","\U0001F590","\U0001F91A")
    elif PC1 == PC2 == User:
        print("EQUAL","\U0001F91A","\U0001F91A","\U0001F91A")
    elif User !=1 or User !=2 :
        print("Wrong","\U0001F611","\U0001F611","\U0001F611")