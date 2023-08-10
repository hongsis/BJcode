from collections import deque

n, k=map(int,input().split())
q=deque([i for i in range(1,n+1)])
a=[]

while len(q) !=0:
    for _ in range(k-1): 
        q.append(q.popleft())  # k-1번째 노드까지 deq 맨 뒤로 이동
    a.append(str(q.popleft())) # k번째 노드 삭제 후 결과 배열에 추가
    
print('<'+', '.join(a)+'>')    



