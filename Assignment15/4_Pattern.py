def Pattern(iRow, iCol):
    for i in range(iRow):
        for j in range(iCol):
            if j % 2 == 0:
                print("*", end=" ")
            else:
                print("#", end=" ")
        print()

def main():
    iValue1 = int(input("Enter number of rows: "))
    iValue2 = int(input("Enter number of columns: "))
    Pattern(iValue1, iValue2)

main()
