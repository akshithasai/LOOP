a=int(input("enter  the number:"))
i=1
while i<a:
    if a%2!=0:
        b=a//2
        print(a)
        if i==b:
            break
    else:
        print(a)
    i=i+1    