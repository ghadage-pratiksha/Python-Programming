def RangesumEven(start, end):
    if start > end:
        print("Invalid Range")
    
    total = 0
    for num in range(start, end + 1):
        if num % 2 == 0:
            total = total + num
    return total


def main():
    start = int(input("Enter starting point: "))
    end = int(input("Enter ending point: "))
    
    result = RangesumEven(start, end)
    print("Addition is", result)
    
main()
