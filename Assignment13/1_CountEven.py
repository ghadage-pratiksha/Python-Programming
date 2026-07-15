def CountEven(iNo):
    iCount = 0
    iDigit=0
    
    if iNo < 0:
        iNo = - iNo

    while iNo != 0:
        iDigit = iNo % 10
        if(iDigit % 2 == 0):
            iCount +=1
        iNo = iNo // 10

    return iCount


def main():
    iValue = int(input("Enter a number: "))
    iRet = CountEven(iValue)
    print( iRet)


main()