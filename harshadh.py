a=int(input("enter the number:"))
i=a
sum=0
while a>0:
    c=a%10
    sum=sum+c
    a=a//10
if i%sum==0:
    print("harshadh")   
else:
    print("no")    