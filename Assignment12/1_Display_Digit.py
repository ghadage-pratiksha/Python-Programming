def DisplayDigit(iNo):
    iDigit=0
    if iNo < 0:
         iNo = - iNo
    while(iNo != 0):
        iDigit = iNo % 10
        print(iDigit)
        iNo = iNo // 10
def main():
     iValue=int(input("Enter a number:"));
     DisplayDigit(iValue)
main()