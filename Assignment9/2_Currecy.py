def DollarToINR(iNo):
    iCurrency= iNo* 70
    return iCurrency

def main():
    iValue=int(input("Enter a number of USD:"));
    iRet= DollarToINR(iValue)
    print("Value of INR is :",iRet)
main()