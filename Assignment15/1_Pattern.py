def Pattern(iRows, iCol):
    for i in range(1, iRows+1):
        for j in range(1,iCol+1):
            print("*", end=" ")
        print()


def main():
    iValue1=int(input(" Enter number of rows :"))
    iValue2=int(input("Enter number of columns:"))
    Pattern(iValue1,iValue2)
main()