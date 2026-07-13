def RectArea(fWidth,fHeight):
    iArea= fWidth*fHeight
    return iArea

def main():
    fValue1=float(input("Enter a width:"))
    fValue2=float(input("Enter a height:"))
    dRet=RectArea(fValue1,fValue2);
    print(f"Area of radius is: {dRet:.4f}")
    
main()