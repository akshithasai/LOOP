a=int(input("enter the number:"))
while a>0:
    b=a%10
    if b%2==0 and b%6==0 and b%8==0:
        print("it divisible by 2,6,8")
    elif b%6==0:
        print("it is divisible by 6 only")
    else:
        print("the last digit is not divisible by 2,6,8")        