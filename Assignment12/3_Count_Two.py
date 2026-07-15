def CountTwo(iNo):
    iCount = 0

    while iNo != 0:
        if (iNo % 10) == 2:
            iCount += 1

        iNo = iNo // 10

    return iCount


def main():
    iValue = int(input("Enter a number: "))
    iRet = CountTwo(iValue)
    print("Count of digit 2:", iRet)


main()