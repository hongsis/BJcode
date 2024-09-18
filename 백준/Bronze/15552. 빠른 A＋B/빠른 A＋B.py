import sys

input = sys.stdin.readline

N=int(input())
c=0
for _ in range(N):
    a,b=map(int,input().split())
    c=a+b
    print(c)
