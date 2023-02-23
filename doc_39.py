'''Write a Python program to compute the average of nth elements in a given list of lists with different lengths.
Original list:
[[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
Average of n-th elements in the said list of lists with different lengths:
[4.8, 5.8, 6.8, 8.0, 11.0]'''


a=[[0, 1, 2,0,0], [2, 3, 4,0,0], [3, 4, 5, 6,0], [7, 8, 9, 10, 11], [12, 13, 14,0,0]]
i=0
total=0
while i<len(a):
    j=0
    sum=0
    while j<len(a[i]):
        sum=sum+a[i][j]
        j=j+1
        avg=sum/total
    i=i+1
    print(avg)    