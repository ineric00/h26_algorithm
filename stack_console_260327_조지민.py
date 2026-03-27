#정수형 스택 연산 실습 (용량 5)
MAX_SIZE = 5
stack = []

#push = append
def isEmpty():
    """스택이 이비있는지 확인"""
    return len(stack) == 0

def isFull():
    """스택이 가득 찼는지 확인 (용량 5 기준)"""
    return len(stack) == MAX_SIZE

def append(data):
    """데이터 삽입"""
    if isFull():
        print(">Stack이 차 있어서 더 이상 추가할 수 없습니다.")
    else:
        stack.append(data)

def pop():
    """데이터 추출(마지막으로 들어온 데이터)"""
    if isEmpty():
        print(">Stack이 비어 있습니다.")
        return None
    else:
        return stack.pop()
    
def peek():
    """가장 위의 데이터 확인 (삭제 안함)"""
    if isEmpty():
        print(">Stack이 비어 있습니다.")
        return None
    else:
        return stack[-1]
    
while True:
    print("-" * 10 + "[ 정수형 스택 연산 실습 (용량 5) ]")
    print(" 1.Append      2.Pop       3. Peek     0.Exit ")
    print("=" * 45)

    choice = input("> 메뉴 선택 : ")

    if choice == '1':
        value = int(input(" > 데이터 입력 : "))
        append(value)
    elif choice == '2':
        removed = pop()
        if removed is not None:
            print(f" > 가져온 데이터 : {removed}")
    elif choice == '3':
        top = peek()
        if top is not None:
            print(f" > 확인된 데이터 : {top}")
    elif choice == '0':
        print("-" * 10 + "[ 정수형 스택 연산 실습 끝 ]")
        break

    print(f" > 현재 스택 상태{stack}\n")



        
