def Pattern(iValue):
    if iValue < 0:
        iValue = -iValue  
    
    
    for i in range(iValue):
        print("$ *", end=" ")   

def main():
    iValue = int(input("Enter a number: "))
    Pattern(iValue)

main()
