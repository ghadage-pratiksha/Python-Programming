def CountFour(iNo):
    iCount = 0

    while iNo != 0:
        if (iNo % 10) == 4:
            iCount += 1

        iNo = iNo // 10

    return iCount


def main():
    iValue = int(input("Enter a number: "))
    iRet = CountFour(iValue)
    print("Count of digit 4:", iRet)


main()