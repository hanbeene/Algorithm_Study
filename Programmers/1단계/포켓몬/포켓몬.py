def solution(nums):
    answer = set(nums)
    realanswer = 0
    if len(answer) < len(nums) // 2:
        realanswer = len(answer)
    else:
        realanswer = len(nums) // 2
    return realanswer


nums = [3, 3, 3, 2, 2, 2]
print(solution(nums))
