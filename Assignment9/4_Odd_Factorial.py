def OddFactorial(iNo):
    if iNo < 0:
        iNo = -iNo  
    
    iFact = 1
    for i in range(1, iNo + 1):  
        if i % 2 != 0:           
            iFact = iFact *i
    return iFact

def main():
    iValue = int(input("Enter a number: "))
    iRet = OddFactorial(iValue)
    print("Even Factorial is:", iRet)

main()