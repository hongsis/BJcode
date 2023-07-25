while(True):
    word=input()

    stack=[] # 괄호를 추가할 리스트 stack
    if word=='.': # . 이 들어오면 종료
        break

    for w in word:
        if w=='(' or w=='[': # 여는 괄호가 오면 stack에 추가
            stack.append(w)
        elif w==')': # ) 인 경우
            if len(stack)!=0 and stack[-1]=='(': # stack이 비어있지 않고, 마지막 요소가 ( 이면 pop
                stack.pop()
            else: # stack이 비어있거나 짝이 맞지 않으면 stack에 )을 추가하고 break
                stack.append(w)
                break
        elif w==']': # ] 인 경우
            if len(stack)!=0 and stack[-1]=='[': # stack이 비어있지 않고, 마지막 요소가 [ 이면 pop
                stack.pop()
            else: # stack이 비어있거나 짝이 맞지 않으면 stack에 ]을 추가하고 break
                stack.append(w)
                break

    if len(stack)==0: # stack이 비어있으면 모든 괄호들의 균형이 맞으므로 Yes 출력
        print('yes')
    else: # stack이 비어있지 않으면 괄호들의 균형이 맞지 않는 것이므로 No 출력
        print('no')
    