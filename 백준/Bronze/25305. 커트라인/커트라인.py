N, M=map(int,input().split())
scores=list(map(int,input().split()))
scores.sort(reverse=True)
print(scores[M-1])