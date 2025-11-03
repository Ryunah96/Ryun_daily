# 단순 증가 패턴

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    raw = list(map(int, input().split()))

    # N을 M으로 나눠 몫과 나머지를 따로 구해두기
    num_q = N // M
    num_r = N % M
    
    # 정답 카운트
    cnt = 0

    # N이 M으로 나눠 떨어지는 값들 우선 비교
    # (0부터 (N-나머지)까지 M 간격으로 확인)
    for i in range(0, N - num_r, M):
        find = True

        for j in range(i, i+M-1):
            
            if raw[j] < raw[j+1]:
                continue
            else:
                find = False
                break
           
        if find:
            cnt += 1

    # 나머지가 있는 경우, 나머지가 1인 경우와 아닌 경우를 나눠서 카운트
    if num_r:

        if num_r == 1:
            cnt += 1

        else:
            for i in range(N - num_r, N-1):
                find = True

                if raw[i] < raw[i+1]:
                    continue
                else:
                    find = False
                    break

            if find:
                cnt += 1


    print(f"#{tc} {cnt}")