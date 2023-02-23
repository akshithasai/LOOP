a=int(input("enter the number:"))
i=a
sum=0
while i>0:
    b=i%10
    sum=sum*10+b
    i=i//10
if sum==a:
    print("polidrame")
else:
    print("no")        