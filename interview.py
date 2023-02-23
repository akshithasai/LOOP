
# a=int(input("enter the number:"))
# b=int(input("enter the number:"))
# i=1
# sum=0
# while i<=b:
#     sum=sum+a
#     i=i+1
# print(sum)    



a=int(input("enter the number :"))
b=int(input("enter the number :"))
c=int(input("enterthe number :"))
i=1
while i>0:
    if a>b and a>c:
        if b>c:
            print(a,"max",b,"mid",c,"min")
        else:
            print(a,"max",c,"mid",b,"min")
    elif b>a and b>c:
        if a>c:
            print(b,"max",a,"mid" ,c,"min")
        else:
            print(b,"max", b,"mid",c,"min")
    elif c>a and c>b:
        if b>a:
            print(c,"max",b,"mid",a,"min")
        else:
            print(c,"max",a,"mid",b,"min")
    i=i-1



# i=1
# while i<=20:
#     if i%3==0 and i%5==0:
#         print("I LOVE YOU")
#     elif i%3==0:
#         print(i)
#     elif i%5==0:
#         print("LOVE")
#     else:
#         print("no")
#     i=i+1
