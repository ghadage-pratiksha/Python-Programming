def income_tax(income):

    if income <= 500000:
        return 0
    elif income <= 1000000:
        return income * 0.10
    elif income <= 2000000:
        return income * 0.20
    else:
        return income * 0.30


def main():
    income = int(input("Enter Gross Income: "))
    tax = income_tax(income)
    print("Tax Amount =", tax)


main()