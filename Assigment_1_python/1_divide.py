def Divide(iNo1, iNo2):
    if iNo2 == 0:
        return -1
    return iNo1 / iNo2


def main():
    iValue1 = 15
    iValue2 = 5
    iRet = Divide(iValue1, iValue2)
    print("Division is", iRet)


main()