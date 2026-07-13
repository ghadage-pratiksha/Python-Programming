def Display(num):
    for i in range(-num, num + 1):
        print(i, end=" ")

def main():
    iValue = int(input("Enter Number: "))
    Display(iValue)
main()
