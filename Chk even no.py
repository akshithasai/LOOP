# for i in range(99,1000):
#     b=str(i)
#     c=int(b)
#     if int(b[0])%2==0 and int(b[1])%2==0 and int(b[2])%2==0:
#         print(i)
#     i=i+1  



n1=int(input())
n2=int(input())
for n in range(n1,n2+1):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                break
            else:
                print(n)