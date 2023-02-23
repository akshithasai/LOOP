a=int(input("enter the number:"))
i=1
count=0
while i<=a:
    if a%1==0 and a%i==0:
        count=count+1
    i=i+1
if count!=2:
    print("composite")
else:
    print("no")            
