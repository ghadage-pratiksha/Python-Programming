def oddDisplay(iNo):
    for i in range(1, iNo+1):
        if i % 2 !=0:
            print(i , end=" ")

def main():
    iValue=int(input("Enter a number:"))
    oddDisplay(iValue)
main()