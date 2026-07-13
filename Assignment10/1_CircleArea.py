def CircleArea(fRadius):
    iArea= 3.14 *fRadius*fRadius
    return iArea

def main():
    fValue=float(input("Enter a radius:"))
    dRet=CircleArea(fValue);
    print(f"Area of radius is: {dRet:.4f}")
    
main()