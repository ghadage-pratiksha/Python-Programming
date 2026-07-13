iValue = int(input("Enter the kilometers you travelled : "))

def TouristBill(iKilometers):
    if(iKilometers < 100):
        iKilometers = iKilometers * 25
        print(iKilometers)
    elif(iKilometers > 100):
        iSum1 = 100 * 25
        iKilometers = iKilometers - 100
        iSum2 = iKilometers * 15
        iCharge = iSum1 + iSum2
        print(iCharge)
        
    
TouristBill(iValue)