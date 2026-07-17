def RangeDisplayEven(iStart, iEnd):
    if iStart < 0:
        iStart = - iStart
    if iStart > iEnd:
        print("Invalid Range")
    for i in range(iStart, iEnd + 1):
        if i % 2 == 0:
            print(i, end=" ")

def main():
    iValue1 = int(input("Enter a starting point: "))
    iValue2 = int(input("Enter an ending point: "))
    RangeDisplayEven(iValue1, iValue2)

main()