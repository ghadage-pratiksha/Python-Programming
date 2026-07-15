def MultDigit(iNo):
    iMult = 1
    iDigit=0

    while iNo != 0:
        iDigit = iNo % 10
        iMult = iMult * iDigit
        iNo = iNo // 10

    return iMult


def main():
    iValue = int(input("Enter a number: "))
    iRet = MultDigit(iValue)
    print( iRet)


main()