# a="akshitha"
# b=len(a)
# i=0
# while i<=b:
#     j=0
#     while j<=i:
#         print(a[j],end="")
#         j=j+1
#     i=i+1
#     print()    


# a="akshitha"
# b=len(a)
# i=0
# while i<=b:
#     k=1
#     while k<=b-i:
#         print(" ",end=" ")
#         k=k+1
#     j=i
#     while j>=0:
#         print(a[j],end=" ")
#         j=j+1
#     i=i+1
#     print()    


# i=1
# while i<=9:
#     k=1
#     while k<=9-i:
#         print(" ",end=" ")
#         k=k+2
#     j=1
#     while j<=i:
#         print(i,end=" ")
#         j=j+2
#     i=i+2
#     print()       



# i=10
# while i<=5:
#     j=10
#     while j<=5:
#         print(j,end=" ")
#         j=j+10
#     i=i+10
#     print()   
# 
#  
# a=int(input("enter the number"))
# i=10
# while i<=a*10:
#     j=i
#     while j<=i:
#         print(j,i,end=" ")
#         j=j+10
#     i=i+10
#     print()    

# a=int(input("enter the number:"))
# i=1
# while i<=5:
#     print(" ",end=" ")
#     j=i
#     while j>=1:
#         print(j*10,end=" ")
#         j=j-1
#     i=i+1
#     print()    



# a="akshitha"
# b=len(a)
# i=0
# while i<b:
#     j=0
#     while j<b-i:
#         print(a[j],end="")
#         j=j+1
#     i=i+1
#     print()  




# i=1
# while i<=10:
#     j=1
#     count=0
#     while j<=i:
#         if i%j==0:
#             count=count+1
#         j=j+1
#     if count==2:    
#          print(i)
#     i=i+1             
  

# i=1
# while i<=5:
#     print(" "*(5-i),end=" ")
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j=j+1
#     i=i+1
#     print()    


a=int(input("enter the number:"))
b=int(input("enter the number:"))
i=1
sum=0
while i<=b:
    sum=sum+a
    i=i+1
print(sum)    