# n개 입력받고 돌 하르방이 제시한 숫자는 dol
n,dol = map(int, input().split())
#약수배수 합 메모
memo = [0 for _ in range (dol+1)]
#약수 메모
divMemo = [0 for _ in range(dol+1)]
#배무 메모
multiMemo = [0 for _ in range(dol+1)]

# n개만큼 돼지 배열 생성
pig = [0 for _ in range(n)]
a = list(map(int,input().split()))

# 입력받은 값을 돼지 배열에 저장
for i in range(n):
    pig[i] = a[i]


for i in range(n):
    count = 0
    divCount = 0
    multiCount = 0
    # 중복된 값 일 경우
    if memo[pig[i]]:
        count = memo[pig[i]]
    else:
        # 약수의 개수
        if divMemo[i] :
            divCount = divMemo
        else:
            for j in range(1,pig[i]):
                if pig[i] % j == 0:
                    divCount += 1
            j = pig[i]
        while j <= dol :
            count += 1
            j += pig[i]
    memo[pig[i]] = count
    print(count)
    # 배수의 개수



# print(count)
