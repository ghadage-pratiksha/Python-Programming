def RectArea(iNo):
    SquareFeet=0.0929
    Square= SquareFeet*iNo
    return Square
    

def main():
    iValue=int(input("Enter a distance:"))
    dRet=RectArea(iValue);
    print(f"The distance in kilometer is: {dRet:.6f}")
    
main()