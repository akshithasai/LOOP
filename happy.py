a=int(input("enter the number:"))
i=a
while i>=10:
    sum=0
    while i>0:
        b=a%10
        sum=sum+b**2
        i=i//10
    i=sum
if sum==1:
    print("happy") 
else:
    print("no")           
