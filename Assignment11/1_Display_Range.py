def RangeDisplay(iStart, iEnd):
    if iStart < 0:
        iStart = - iStart
    if iStart > iEnd:
        print("Invalid Range")
        return
    for i in range(iStart, iEnd + 1):
        print(i, end=" ")

def main():
    iValue1 = int(input("Enter a starting point: "))
    iValue2 = int(input("Enter an ending point: "))
    RangeDisplay(iValue1, iValue2)

main()
