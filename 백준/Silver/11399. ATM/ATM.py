n=int(input())
p=list(map(int, input().split()))
p.sort()

time=0
for i in range(1,n+1):
  time += p[i-1]*(n-(i-1))

print(time)