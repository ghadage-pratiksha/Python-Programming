Value=int(input("Enter a number:"))

def ChkEqual(cValue1, cValue2):
    if cValue1 == cValue2 :
        return True
    else:
        return False
        
bRet= False      
bRet = ChkEqual(Value)

if(bRet == True):
    print("Equal")
else:
    print("Not Equal")