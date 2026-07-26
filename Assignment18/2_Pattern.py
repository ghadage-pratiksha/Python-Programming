def Pattern(iRow, iCol):
    for i in range(iRow,0,-1):
        for j in range(iCol):
            if(j<i):
                print("*", end=" ")
            else:
                print("#",end=" ")
        print()
            
def main():
    iValue1=int(input("Enter a number of rows:"))
    iValue2=int(input("Enter a number of columns:"))
    
    Pattern(iValue1,iValue2);
main()