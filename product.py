a=int(input("enter the number :"))
product=1
while a>0:
    b=a%10
    product=product*b
    a=a//10
print(product)    