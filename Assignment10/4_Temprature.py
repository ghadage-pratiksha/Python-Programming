fValue = float(input("Enter the temperature in Fahrenheit : "))

def FhtoCs(iTemp):
    celcius = (iTemp - 32) * (5/9)
    return celcius
    
dRet = FhtoCs(fValue)
print("Converted temperature : ",dRet)