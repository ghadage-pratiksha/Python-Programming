def Display(iNo):
    while iNo > 0:
        print("*", end=" ")
        iNo -= 1

def main():
    iValue = int(input("Enter number: "))
    Display(iValue)

main()
