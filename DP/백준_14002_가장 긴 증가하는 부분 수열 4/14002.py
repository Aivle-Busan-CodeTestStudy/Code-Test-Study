n = int(input())
a = list(map(int,input().split()))

d = [1]*n

for i in range(n):
  for j in range(i+1):
    if a[i] > a[j]:
      d[i] = max(d[i],d[j]+1)

mx = max(d) 
print(mx)

l = []
for idx,i in enumerate(d[::-1]):
  if i == mx:
    l.append(a[::-1][idx])
    mx -= 1
print(' '.join(map(str,l[::-1])))
