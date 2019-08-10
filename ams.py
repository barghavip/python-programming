n1=int(input())
n2=int(input())
for i in range(n1,n2+1): 
    l=len(str(i))
    t=i
    sum=0
    while t>0:
        sum=sum+(t%10)**l
        t=t//10
    if sum==i:
        print(i)
    
