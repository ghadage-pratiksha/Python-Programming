def Number(iNo):
    if iNo < 50:
        print("Small")
    elif iNo <= 100:   
        print("Medium")
    else:              
        print("Large")

def main():
    iValue = int(input("Enter Number: "))
    Number(iValue)

main()
