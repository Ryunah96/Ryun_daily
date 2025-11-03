# algo2

from collections import deque

T = int(input())

for tc in range(1, T+1):
    N, K, E = list(map(int, input().split()))
    go = [list(map(int, input().split())) for _ in range(E)]

    # 화살표 출발, 도착지 리스트
    go_start = []
    go_end = []
    for i in range(E):
        go_start.append(go[i][0])
        go_end.append(go[i][1])
    
    # 방문
    visited = [[0]*N for _ in range(K+1)]
    q = deque()
    q.append((0, 0))

    max_num = 0

    while q:

        n, k = q.popleft()

        if k == K:
            max_num = max(n, max_num)
        
        for move in (1, 7):

            next_num = n + move

            for i in range(len(go_start)):
                if  n == go_start[i]:
                    n = go_end[i]
                    next_num = go_end[i] + move
                    break
            if next_num <= N:
                q.append((next_num, k+1))



    print(f"#{tc} {max_num}")