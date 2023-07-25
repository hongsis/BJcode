import sys
k=int(input())

stack=[]
for _ in range(k):
    a= int(sys.stdin.readline())
    
    if a !=0 :
        stack.append(a)
    elif a ==0 :
        stack.pop()

print(sum(stack))
    
    
    
    
    