def FactorialDiff(iNo):
    if iNo < 0:
        iNo = -iNo  
    
    iFact1 = 1
    iFact2 = 1
    for i in range(1, iNo +1):  
        if i % 2 == 0:           
            iFact1 = iFact1 *i
    for i in range(1, iNo +1):  
        if i % 2 != 0:           
            iFact2 = iFact2 *i
    iSum = iFact1- iFact2;
    return iSum;

def main():
    iValue = int(input("Enter a number: "))
    iRet = FactorialDiff(iValue)
    print("Factorial Diffrence is:", iRet)

main()