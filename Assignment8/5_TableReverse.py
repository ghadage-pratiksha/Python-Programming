def TableReverse(num):
    if num < 0:
       num =- num
    for i in range(10, 0):
            iMul= i * num
            print(iMul, end=" ")

def main():
    iValue = int(input("Enter Number: "))
    TableReverse(iValue)
    
main()