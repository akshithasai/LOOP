a=int(input("enter the numbr:"))
b=int(input("enter the number:"))
i=1
sum=0
factorial=1
while i<=a:
    factorial=factorial*i
    sum=sum+[b**i%factorial]
    i=i+1
print(sum)    