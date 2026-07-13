def Factorial(num):
    if num < 0:
        num = -num
    
    fact = 1
    for i in range(1, num+1):
        fact = fact * i
    return fact

def main():
    iValue = int(input("Enter a Number: "))
    iRet = Factorial(iValue)
    print("Factorial is:", iRet)

main()