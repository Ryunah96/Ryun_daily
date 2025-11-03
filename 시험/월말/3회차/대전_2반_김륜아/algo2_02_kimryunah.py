# 문제2
# MST 문제 but, import 사용 금지
# 리스트 이용해서 최솟값만 뽑아내기

T = int(input())

def star(cnt, total):
    global answer

    if total >= answer:
        return
    
    if cnt == V+1:
        answer = min(total, answer)
        return
    
    for i in range(V+1):

        for j in range(V+1):
            if raw[i][j] != 0 and not visited[j]:

                visited[j] = 1

                star(cnt+1, total + raw[i][j])
                
                visited[j] = 0

        

for tc in range(1, T+1):
    V, E = map(int, input().split())
    # u v w

    raw = [[0]*(V+1) for _ in range(V+1)]
    
    for _ in range(E):
        u, v, w = map(int, input().split())
        raw[u][v] = w
        raw[v][u] = w
    
    visited = [0] * (V+1)
    answer = 9999999999999999999

    star(0, 0)

    print(f"#{tc} {answer}")