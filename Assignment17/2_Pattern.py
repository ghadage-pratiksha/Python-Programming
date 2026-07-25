def Pattern(iRow, iCol):
    for i in range(iRow):

        iNo1 = 2
        iNo2 = 1

        for j in range(iCol):

            if(i % 2 != 0):
                print(iNo1, end=" ")
                iNo1 = iNo1 + 2
            else:
                print(iNo2, end=" ")
                iNo2 = iNo2 + 2

        print()

def main():
    iValue1 = int(input("Enter number of rows : "))
    iValue2 = int(input("Enter number of columns : "))

    Pattern(iValue1, iValue2)

main()

