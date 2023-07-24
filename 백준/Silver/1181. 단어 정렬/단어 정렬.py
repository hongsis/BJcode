import sys
n=int(input())

word=[]
for _ in range(n):
    word.append(sys.stdin.readline().strip())
    
word = list(set(word)) #set으로 중복 제거 후 다시 리스트로 묶어주기
word.sort()       #알파벳순으로 정렬
word.sort(key=len)#길이순으로 재정렬

for i in word:
    print(i)