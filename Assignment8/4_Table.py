def Table(iNo):
    if (iNo < 0):
        iNo = - iNo
    for i in range(1,11):
        iMul= i*iNo
        print(iMul, end=" ")
def main():
    iValue=int(input("Enter a number:"))
    Table(iValue)
main()