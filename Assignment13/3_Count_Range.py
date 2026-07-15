def CountRange(iNo):
    iCount = 0
    iDigit=0
    

    while iNo != 0:
        iDigit = iNo % 10
        if(iDigit < 7 and iDigit > 3):
            iCount +=1
        iNo = iNo // 10

    return iCount


def main():
    iValue = int(input("Enter a number: "))
    iRet = CountRange(iValue)
    print( iRet)


main()