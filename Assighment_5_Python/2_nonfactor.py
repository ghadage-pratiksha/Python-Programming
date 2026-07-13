iValue = int(input("Enter a number : "))
# iMult = 1
# i = 0;

def NonFact(iNo):
    # iMult = 1
    i = 1
    for i in range(1,iNo):
        if(iNo % i != 0):
            print(i)

NonFact(iValue)