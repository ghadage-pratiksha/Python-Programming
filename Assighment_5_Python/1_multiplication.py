iValue = int(input("Enter a number : "))
# iMult = 1
# i = 0;

def MultFact(iNo):
    iMult = 1
    i = 1
    for i in range(1,iNo):
        if(iNo % i == 0):
            print(i)
            iMult = iMult * i
    return iMult
    
Ans = MultFact(iValue)
print("Multiplication of factors is : ",Ans)