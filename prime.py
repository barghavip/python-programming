n=int(input("n:"))
if n>1:
    for i in range(2,n):
        if(n%i)==0:
            print('no')
            break
    else:
            print('yes')
else:
    print("no")
