noun=['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']
while True:
    count=0
    s=input()
    if s =='#':
        break
    for i in s:
        if i in noun:
            count+=1
    print(count)