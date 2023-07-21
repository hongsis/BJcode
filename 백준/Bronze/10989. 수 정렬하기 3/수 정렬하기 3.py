import sys
n=int(input())
num=[0]*10001

for _ in range(n):
    s=int(sys.stdin.readline())
    num[s]+=1

for i in range(10001):
    if num[i] !=0:
        for j in range(num[i]):
            print(i)
    
    