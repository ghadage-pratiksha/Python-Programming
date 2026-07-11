def check(num):
    if num % 5 == 0:
        return True
    else:
        return False

value = int(input("Enter number: "))
ret = check(value)

if ret:
    print("Divisible by 5")
else:
    print("Not divisible by 5")
