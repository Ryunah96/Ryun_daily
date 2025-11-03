# algo1

T = int(input())

for tc in range(1, T+1):

    # 문자열 받아주기
    raw = input()
    
    # '.'을 기준으로 나누기
    result = raw.split('.')

    # '.'을 기준으로 나눠진 길이만큼 반복
    for i in range(len(result)):
        # '.'을 기준으로 문자열 뒤집기
        result[i] = result[i][::-1]
    
    # 다시 '.' 넣어서 붙여주기
    answer = '.'.join(result)
    print(f"#{tc} {answer}")