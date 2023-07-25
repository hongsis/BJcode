import sys

n=int(input())

Stack=[]

for _ in range(n):
    command = sys.stdin.readline().split()
    c = command[0]

    if c == 'push':
        value=command[1]
        Stack.append(value)
    
    elif c == 'top':
        if len(Stack)==0:
            print(-1)
        else:
            print(Stack[-1])
    
    elif c == 'size':
        print(len(Stack))

    elif c =='empty':
        if len(Stack) ==0:
            print(1)
        else:
            print(0)
            
    elif c == 'pop':
        if len(Stack)==0:
            print(-1)
        else:
            print(Stack.pop())


    
    
    
    
    
    
    
    