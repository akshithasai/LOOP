# i=1
# while i<=5:
#     k=1
#     while k<=5-i:
#         print(" ",end=" ")
#         k=k+1
#     j=i
#     while j>=1:
#         print(j,end=" ")
#         j=j-1
#     i=i+1
#     print()        


i=1
while i<=5:
    j=i
    while j<=5:
        print(i,end=" ")
        k=1
        while k<=5:
            print(k+1,end=" ")
            k=k+1
        j=j+1
    i=i+1
    print()        