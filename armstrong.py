a=int(input("enter the number:"))
l=len(str(a))
i=a
sum=0
while a>0:
    b=(a%10)**l
    sum=sum+b
    a=a//10
if sum==i:
    print("armstrong")
else:
    print("no")        