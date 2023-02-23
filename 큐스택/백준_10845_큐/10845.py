from collections import deque
from sys import stdin

q = []
q = deque(q)
n = int(stdin.readline())
for i in range(n):
    a = stdin.readline().split()
    if a[0] == 'push':
        q.append(int(a[1]))
    elif a[0] == 'pop':
        if q:
            b = q.popleft()
            print(b)
        else:
            print(-1)
    elif a[0] == 'size':
        print(len(q))
    elif a[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif a[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
