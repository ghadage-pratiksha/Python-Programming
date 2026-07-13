iValue = int(input("Enter a number : "))
# iMult = 1
# i = 0;

def FactDiff(iNo):
    # iMult = 1
    i = 1
    iSumFact = 0
    iSumNonFact = 0
    iDiff = 0
    for i in range(1,iNo):
        if(iNo % i == 0):
            # print(i)
            iSumFact = iSumFact + i
        elif(iNo % i != 0):
            iSumNonFact = iSumNonFact + i
    
    iDiff = iSumFact - iSumNonFact
    return iDiff

iRet = FactDiff(iValue)
print("Diffrence is : ",iRet)