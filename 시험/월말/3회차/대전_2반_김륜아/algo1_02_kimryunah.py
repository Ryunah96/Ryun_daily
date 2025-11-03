# 문제1
# 합성곱 Convolution

T = int(input())

for tc in range (1, T+1):
    N, M = map(int, input().split())
    raw = [list(map(int, input().split())) for _ in range(N)]
    filter_raw = [list(map(int, input().split())) for _ in range(M)]

    # answer 크기는 (N-M+1)*(N-M+1) 
    answer = [[0]*(N-M+1) for _ in range(N-M+1)]
    
    for i in range(N-M+1):
        for j in range(N-M+1):
            cal = 0
            for r in range(i, i+M):
                for c in range(j, j+M):
                    # 필터 크기는 M*M 이므로 인덱스 [r-i][c-j]
                    cal += raw[r][c] * filter_raw[r-i][c-j]
            answer[i][j] = cal


    print(f"#{tc}")
    for i in range(N-M+1):
        print(*(answer[i]))