def chk_zero(iNo: int):
	while iNo != 0:
        	if (iNo % 10) == 0:
            	return True
        	iNo = iNo // 10
	return False


def main():
    iValue = int(input("Enter number: "))
    bRet = chk_zero(iValue)

    if bRet:
        print("It Contains Zero")
    else:
        print("There is no Zero")

main()
