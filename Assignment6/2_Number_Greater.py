cValue=int(input("Enter a number:"))

def ChkGreater(cValue):
    if(cValue >= 100):
        return  True
    else:
        return False
        
bRet = False
bRet = ChkGreater(cValue)
if(bRet==True):
    print("Greater")
else:
    print("Smaller")