i=1
while i<=5:
    k=1
    while k<=5-i:
        print(" ",end=" ")
        k=k+1
    j=1
    while j<=i:
        if i%2==0:
            print(i,end= " ")
        else:
            print("*",end=" ")
        j=j+1
    i=i+1
    print()           