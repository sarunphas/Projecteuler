data=[i for i in range(2,21)]
print(data)

prime = [2]   

for i in range(len(data)):
    if i == 0:
        pass
    else:
        for j in range(0,i):
            print(data[i],data[j])
            
            if data[i]%data[j]==0:
                data[i] = data[i]/data[j]
    prime.append(data[i])            
ss=1
for i in data:
    ss=ss*(i)
print(ss)


            

                
