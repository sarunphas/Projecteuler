a = [1,2]
i=2 
b=0
while b < 4000000:
    print(i)
    a.append(a[i-1]+a[i-2])
    
    b=a[i]
    b=b
    i=i+1
    
# print(a)

d=list(filter(lambda x: x%2==0,a))
print(sum(d))