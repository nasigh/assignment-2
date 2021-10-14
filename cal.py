import math
while True:
    print("1.Sum +++")
    print("2.Sub ---")
    print("3.Multiplication ***")
    print("4.Division ///")
    print("5.Sin")
    print("6.Cos")
    print("7.Tan")
    print("8.Cot")
    print("9.Log")
    print("10.Exit")

    op= int(input())

    #print("Enter Numbers:")
   # Number1 = int(input("Number 1 Is :"))
    #Number2 = int(input("Number 2 Is :"))
    if 1 <= op <= 4:
        print("Enter Numbers:")
        Number1 = int(input("Number 1 Is :"))
        Number2 = int(input("Number 2 Is :"))
        if op == 1:   
            print(Number1 + Number2)  
        elif op == 2:
            print(Number1 - Number2)   
        elif op == 3:
            print(Number1 * Number2)   
        elif op == 4:
            if Number2 != 0:
                print(Number1 / Number2)
            else: 
                print("WRONG")
    elif 5 <= op <= 8 :
        if op == 5:
            Degree = int(input("Enter Your Degree :"))
            print("Sin ",Degree," Is ", float(math.sin(90 * math.pi / 180)))
        elif op == 6:
            Degree = int(input("Enter Your Degree :"))
            print("Cos ",Degree," Is ", float(math.cos(90 * math.pi / 180)))    
        elif op == 7:
            Degree = int(input("Enter Your Degree :"))
            print("Tan ",Degree," Is ", float(math.tan(90 * math.pi / 180)))
        elif op == 8:
            Degree = int(input("Enter Your Degree :"))
            print("Cot ",Degree," Is ", float(math.atan(90 * math.pi / 180)))
    elif op == 9:
            Number = int(input("Enter Your Number :"))
            Basis = int(input("Enter Your Basis :"))
            print("Log ",Number," In The Basis ",Basis," Is ", float(math.log(Number,Basis)))
    elif op == 10:
        print("Good Luck")
        break