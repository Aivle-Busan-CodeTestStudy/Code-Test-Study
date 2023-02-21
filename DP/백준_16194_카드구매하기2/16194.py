n = int(input())
p = [0] + list(map(int,input().split()))
for i in range(1,n+1):
  for j in range(1,1+i):
      p[i] = min(p[i],p[i-j] + p[j])
print(p[n])
