def chk_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

def main():
    iValue = int(input("Enter number: "))
    bRet = chk_even(iValue)

    if bRet:
        print("Number is Even")
    else:
        print("Number is Odd")

if __name__ == "__main__":
    main()
