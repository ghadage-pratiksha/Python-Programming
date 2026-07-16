def Pattern(iRow, iCol):
    for i in range(1, iRow + 2):   
        for j in range(iCol):
            print(i, end=" ")
        print()

def main():
    iValue1 = int(input("Enter number of rows: "))
    iValue2 = int(input("Enter number of columns: "))
    Pattern(iValue1, iValue2)
main()
