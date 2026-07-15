def CountDiff(iNo):
    iDigit=0
    iEvenSum=0
    iOddSum=0

    while iNo != 0:
        iDigit = iNo % 10
        if(iDigit % 2 ==0):
            iEvenSum = iEvenSum + iDigit
        else:
            iOddSum = iOddSum + iDigit
        
        iNo = iNo // 10
    
    return  iEvenSum - iOddSum
def main():
    iValue = int(input("Enter a number: "))
    iRet = CountDiff(iValue)
    print( iRet)


main()