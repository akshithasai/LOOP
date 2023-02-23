i=1
while i<=5:
    j=1
    while j<=i:
        if i==1 and j==1 or i==2 and j==3 or j==5:
            print("*",end=" ")
            j=j+1
    i=i+1
    print()        