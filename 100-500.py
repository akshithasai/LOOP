# oddsum=0
# evensum=0
# i=100
# while i<=500:
#     if i%2==0:
#         evensum=evensum+i
#     if i%2!=0:
#         oddsum=oddsum+i
#     i=i+1
# print(evensum) 
# print(oddsum)       




a=int(input("enter the number:"))
i=1
count=0
while i<=a:
    if a%i==0 and a%1==0:
        count=count+1
    i=i+1
if count==2:
    print("prime")
else:
    print("noo")           
    