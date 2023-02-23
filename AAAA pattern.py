# i=1
# while i<=5:
#     j=1
#     while j<=5:
#         if i==1 or j==1 and i==5 or j==5:
#             print("A",end=" ")
#         elif i==j==3:
#             print("c",end=" ")
#         else:
#             print("B",end=" ")
#         j=j+1
#     i=i+1
#     print()                


# i=1
# while i<=5:
#         if i==1 or i==5:
#             print("*"*5,end=" ")
#         else:
#             print("*"+" "*7+" ")  
#         i=i+1
#         # print()           


# i=0
# while i<5:
#     if i==0 or i==4:
#         print("* "*5)
#     else:
#         print("*"+" "*7+"")
#     i=i+1



i=1
while i<=5:
    j=1
    while j<=5:
        if i==1 or j==1 and i==2 or j==1 and i==3 or j==1 and i==4 or j==1 and i==5 or j==1 and j==2 or i==5 and j==3 or i==5 and j==4 or i==5 and j==5 or i==5 and j==5 or i==2 and j==5 or i==3 and j==5 or i==4 and j==5 or i==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")  
        j=j+1
    i=i+1
    print()          