def Pattern(iRow, iCol):
    for i in range(iRow):
        ch='A'
        for j in range(iCol):
            print(ch, end=" ")
            ch=chr(ord(ch)+1)
        print()
def main():
    iValue1=int(input("Enter a number of rows:"))
    iValue2=int(input("Enter a number of columns:"))
    
    Pattern(iValue1,iValue2);
    
main()
