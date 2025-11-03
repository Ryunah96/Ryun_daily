# 문제 1

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    # 가로
    raw = [input() for _ in range(N)]
    
    # 각 범위에서 답이 안 나오는 경우 check
    no_answer = 0

    for i in range(N - M + 1):
        for j in range(N - M + 1):

            # 별 개수 카운트
            count = 0

            # 영역의 좌표를 왼쪽 상단 모서리의 좌표로 뽑으려고 역순으로 비교
            for r in range(M-1, -1, -1):
                for c in range(M-1, -1, -1):
                    if raw[i + r][j + c] == '*':
                        count += 1

            # 별 개수가 K개면 출력
            if count == K:
                print(f"#{tc} {i+r} {j+c}")
                count = 0
                break
            
            # 별 개수가 K개가 아니면 count 개수 초기화 및 no_answer 카운트 +1
            else:
                count = 0
                no_answer += 1

    # 별 개수가 K인 구역이 없으면 -1, -1 출력
    if no_answer == ((N-M+1)**2):
        print(f"#{tc} -1 -1")