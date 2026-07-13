def percentage(iValue1, iValue2):
    if total == 0:
        return 0
    return (iValue2 / iValue1) * 100

def main():
    iValue1 = int(input("Enter total marks: "))
    ivalue2 = int(input("Enter obtained marks: "))
    result = percentage(iValue1, iValue2)
    print("Your percentage is", result)

main()
