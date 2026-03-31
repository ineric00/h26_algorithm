import heapq
import sys

# 입출력 속도를 위해 sys.stdin.readline 사용
input = sys.stdin.readline

n = int(input())
max_heap = []

for _ in range(n):
    x = int(input())
    
    if x > 0:
        # 최대 힙을 위해 음수로 변환하여 push
        heapq.heappush(max_heap, -x)
    else:
        # x가 0인 경우 (pop 연산)
        if not max_heap:
            print(0)
        else:
            # 다시 양수로 바꿔서 출력
            print(-heapq.heappop(max_heap))