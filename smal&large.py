# largest=smallest=0
# count=1
# while count<=10:
#     a=int(input("enter the number:"))
#     if count==1:
#         largest=smallest=0
#     if a>largest:
#         largest=a
#     if a<smallest:
#         smallest=a
#         count=count+1
#     else: 
#         print("the largest no:" ,largest) 
#         print("the smallest no:" ,smallest)          


i=1
while i<=10:
    count=0
    j=1
    while j<=i:
        if i%j==0:
            count=count+1
        j=j+1
    if count==2:
        print(i)
    i=i+1            