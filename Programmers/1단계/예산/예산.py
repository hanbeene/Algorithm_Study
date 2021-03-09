def solution(d, budget):
    if sum(d) <= budget:
        return len(d)
    else:
        d.sort()
        answer = 0
        count = 0
        for i in range(len(d)):
            if answer + d[i] <= budget:
                answer += d[i]
                count += 1
            else:
                return count


d = [5,5,2,2,2]
budget = 11
print(solution(d, budget))
