def Pattern(iRow, iCol):
    iNo=1;
    for i in range(iRow):
        for j in range(iCol):
                print(iNo, end=" ")
                iNo+=1
        print()
def main():
    iValue1=int(input("Enter a number of rows:"))
    iValue2=int(input("Enter a number of columns:"))
    
    Pattern(iValue1,iValue2);
    
main()


























