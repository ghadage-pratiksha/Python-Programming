def display(iNo, frequency):
    for i in range(1, frequency + 1):
        print(iNo)

def main():
    iValue = int(input("Enter Number: "))
    iCount = int(input("Enter Frequency: "))
    display(iValue, iCount)

main()
