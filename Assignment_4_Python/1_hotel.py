def calculate_bill(amount):

    if amount >= 1500:
        discount = amount * 0.15
    elif amount >= 500:
        discount = amount * 0.10
    else:
        discount = 0

    return amount - discount, discount


def main():
    bill = int(input("Enter Bill Amount: "))

    final_bill, discount = calculate_bill(bill)

    print("Discount =", discount)
    print("Amount to Pay =", final_bill)
    print("Thank You... Visit Again!!")


main()