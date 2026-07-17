iValue = int(input("Enter number : "))

def Pattern(iNo):
    for i in range(1,iNo+1):
        print(i,"*", end = " ")
        
Pattern(iValue)