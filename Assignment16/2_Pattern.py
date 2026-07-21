def Pattern(iRow, iCol):
    for i in range(iRow):
        ch='A'
        ch1='a'
        for j in range(iCol):
            if(i% 2==0):
                print(ch, end=" ")
                ch=chr(ord(ch)+1)
            else:
                print(ch1, end=" ")
                ch1=chr(ord(ch1)+1)
        print()
def main():
    iValue1=int(input("Enter a number of rows:"))
    iValue2=int(input("Enter a number of columns:"))
    
    Pattern(iValue1,iValue2);
    
main()






























