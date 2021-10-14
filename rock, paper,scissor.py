import random
user=0
computer=0
print ("*lets play game*","\U0001F60E")
print ("you have 5 set to play whith computer")
print ("if you are ready choose 1 and if you are not choose 2")
print ("1-yes","2-no")
agreement = input("tel me:")
if agreement == '1':
    for i in range(1,6):
     print("round:" ,+i )
     print("computer:",+computer)
     print("user:", +user)
     gamelist = ["1-rock","2-paper","3-scissor"]
     for x in gamelist:
      print(x)
     ch = input ("enter your choice:")
     pc = random.randint(1,3)
     print("pc number:",+pc)
     if pc==ch :
         print("equal")
     elif pc==1 and ch=='2':
         user += 1
     elif pc==1 and ch=='3':
         computer += 1
     elif pc==2 and ch=='1':
         computer += 1
     elif pc==2 and ch=='3':
         user += 1
     elif pc==3 and ch=='1':
        user += 1
     elif pc==3 and ch=='2':
        computer += 1

    else:
        if computer == user:
            print("equal") 
        elif computer > user:
            print("computer won")  
        elif user > computer:
            print ("user won")  
elif agreement == '2' :
    print("good bye")                                      
