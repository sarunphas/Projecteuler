import time
def factor(num):
    if num==2:
        return num
    i=2
    while i<=(num-1):        
        if num % i !=0:
            i+=1
            c=0                
        else:
            c=1
            break   
    if c==0:
        return num
  
number = 600851475143 
c=[]
i=2
while i<=number:
    if factor(i) is not None:
        if number%(factor(i))==0:
            number=number/i
            c.append(i)
    i=i+1
print(c)

# a=[2]
# for i in range(3,number):
#     if factor(i) is not None:     
#         a.append(factor(i))
# print(a)


# b=list(filter(lambda x: number%x==0,a)) 
# print(b)








            
           