def MultipleDisplay(iNo):
    for i in range(1, 6):
        mul = i * iNo
        print(mul, end=" ")

def main():
    iValue = int(input("Enter a number: "))
    MultipleDisplay(iValue)
main()
