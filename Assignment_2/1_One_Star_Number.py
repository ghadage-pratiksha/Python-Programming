def Display(iNo):
    iCnt = 0
    while iCnt < iNo:
        print("*", end=" ")
        iCnt += 1

def main():
    iValue = int(input("Enter number: "))
    Display(iValue)

main()
