n=int(input())
k=int(input())
l = [int(input()) for _ in range(n)]
sum=0
for num in l:
    if k!=0:
      sum+=num
      k=k-1
print(sum)

      
