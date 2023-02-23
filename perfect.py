a=int(input("enter the number:"))
i=1
sum=0
while i<a:
    if a%i==0:
        sum=sum+i
        print(i)
    i=i+1
if sum==a:
    print("perfect",a)
else:
    print("no",a)            
