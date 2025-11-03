#  사과 수학

T = int(input())

def cac(A, B):
    return (abs(A[0]-B[0]) + abs(A[1]-B[1]))
            
def dfs(cnt, now_x, now_y, total):
    global answer


    if cnt == N:
        total += cac([0,0], [now_x, now_y])
        answer = min(answer, total)
        return

    if total > answer:
        return

    for i in range(N):
        if not visited[i]:
            nx, ny = apples[i]
            visited[i] = 1

            dfs(cnt+1, nx, ny, (total + cac([now_x, now_y], [nx, ny])))

            visited[i] = 0


for tc in range(1, T+1):
    N = int(input())

    apples = []
    visited = [0] * N

    for _ in range(N):
        x, y = map(int, input().split())
        apples.append((x, y))
    
    answer = 9999999999

    dfs(0, 0, 0, 0)

    print(f"#{tc} {answer}")
