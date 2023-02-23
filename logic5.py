# a=int(input("enter the number:"))
# b=int(input("enter the number:"))
# i=1
# sum=0
# while i<=b:
#     sum=sum+a
#     i=i+1
# print(sum)    


# # a=["hello"]
# print(list("hello"))



# L = ['a', ['bb', 'cc'], 'd']
# L[1].append('xx')
# print(L)


# names = ['Amir', 'Bear', 'Charlton', 'Daman']
# print(names[-3][-1][-1][-1])




# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# b=len(numbers)
# print(b)
    


# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# count = 0
# for element in numbers:
#  count += 1
# print("Number of elements in the list: ", count)



a=[2,33,41,5,52,35,111,32]
count=0
i=0
while i<len(a):
    if a[i]>=20 and a[i]<=40:
        count=count+1
    i=i+1
print(count)