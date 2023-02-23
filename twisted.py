
# a=int(input("enter the number:"))
# i=1
# count=0
# while i<=a:
#     if a%1==0 and a%i==0:
#         count=count+1
#     i=i+1
# if count==2:
#     j=0
#     while a>0:
#         b=a%10
#         j=j*10+b
#         a=a//10
#     k=1
#     c=0
#     while k<=j:
#         if j%k==0:
#             c=c+1
#         k=k+1
#     if c==2:
#         print("twested")
#     else:
#         print(" prime but not twested") 
# else:
#     print("not prime")                               


a=int(input())
i=2
c=0
if a!=0:
    r=a%10
    r1=a//10
    t=r*10+r1
print(t)
while i<a:
    if a%i==0:
        c=1
    i=i+1
if c==0:
    print("prime")
else:
    print("not ")