# 문제 2

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    raw = [list(map(int, input().split())) for _ in range(N)]

    # 우 하 좌 상
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    # 안전구역 개수 카운트
    answer = 0

    for i in range(1, N-1):
        for j in range(1, M-1):
            
            # 안전구역 후보
            A = raw[i][j]

            # 상하좌우 비교 카운트 (안전구역이면 4 됨)
            check = 0

            for idx in range(4):
                if raw[i + di[idx]][j + dj[idx]] < A:
                    check += 1
            
            # check = 4 나오면 answer +1 카운트, check는 매번 0으로 초기화
            if check == 4:
                answer += 1
                check = 0
            else:
                check = 0

    print(f"#{tc} {answer}")