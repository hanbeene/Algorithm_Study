# 에로토스테네스의 체
def prime_list(N):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * (N + 1)

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int((N + 1) ** 0.5)

    for i in range(2, m + 1):
        if sieve[i] == True:  # i가 소수인 경우
            for j in range(i + i, N + 1, i):  # i이후 i의 배수들을 False로 판정
                sieve[j] = False

    return [i for i in range(2, N + 1) if sieve[i] == True]


def solution(nums):
    sosulist = prime_list(3000)
    sumlist = []
    answer = 0
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                sumlist.append(nums[i] + nums[j] + nums[k])

    for q in sumlist:
        if q in sosulist:
            answer += 1

    return answer

test = [1,2,7,6,4]
print(solution(test))
