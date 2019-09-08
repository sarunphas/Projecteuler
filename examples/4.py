import math
def checkpalin(number):
    b=str(number)
    c=b[::-1]
    return b==c
# print(checkpalin(9019))

d=[]
def palin():
    
    max=999*999
    min=99*99
    for i in range(max,min,-1):       
        if checkpalin(i):        
            d.append(i)
palin()           

# d=list
for number in d:
    center=math.floor(number**0.5)
    j=1
    while j<center and (center-j)>99:
        if number%(center-j)==0:
            break
    
        j=j+1
    if center-j>99 and number/(center-j)<999:
        print(number,center-j)
        break
       
print(number,(center-j))
print(number/(center-j))


    



