import random
#def sumNumb(str):return sum(map(lambda x: int(x),str)) print(sumNumb("12"))
    
def sumNum(number):
    return number//10+number%10

def luna(cardNumber):
    evenNumbers = cardNumber[::2]
    oddNumbers = list(cardNumber[1::2])
    sumOddNumbers = 0
    for i in oddNumbers:
        sumOddNumbers+=int(i)
    k = 0
    summ = 0
    for i in evenNumbers:
        k = int(i)*2
        summ+=sumNum(k)
    return(summ+sumOddNumbers)%10 

def generateCardNumber():
    result = '4'
    for i in range(2,16):
        random.seed()
        result+=str(random.randint(1,9))
        if(i%4 == 0):
            result+=' '
    #print(result)
    for i in range(0,9):
        if(luna((result+str(i)).replace(" ",'')) == 0):
            result+=str(i)
            return result
        

cardNumber = input("Put you card number to check: ").replace(" ",'')
if(len(cardNumber)!=16 or not cardNumber.isdigit()):
    print("Incorrect card number!")
    exit()
else:
    if(luna(cardNumber) == 0):
        print("Incorrect card number!")
    else:
        print("Correct card number!")
print(generateCardNumber())

input()