def Display(iNo):
    if iNo < 0:
        iNo = - iNo
    
    for i in range( iNo):
        print("*" ,end=" ")
        
    for i in range(iNo):
        print("#", end=" ")
        
def main():
    iValue=int(input("Enter a number:"))
    Display(iValue)
    
main()