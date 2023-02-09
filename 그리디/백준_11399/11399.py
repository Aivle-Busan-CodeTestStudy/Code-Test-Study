N = int(input())
P = list(map(int,input().split(' ')))
answer = 0
P = sorted(P)
for i in range(N):
    answer += sum(P[:i+1])
print(answer)
