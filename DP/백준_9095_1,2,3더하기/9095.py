t = int(input())
answer=[]
for i in range(t):
    answer.append(int(input()))
n = [0]*(max(answer)+1)
n[1],n[2],n[3] = 1,2,4
for i in range(4,max(answer)+1):
    n[i] = n[i-1] + n[i-2] + n[i-3]

for i in answer:
    print(n[i])
