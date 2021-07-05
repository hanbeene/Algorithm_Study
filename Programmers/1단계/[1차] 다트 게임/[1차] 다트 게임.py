def solution(dartResult):
    scoresum = []
    bucket = []
    for score in dartResult:
        if len(bucket) > 0 and score.isdigit() == True:
            bucket.pop()
            bucket.append(10)
        elif score.isdigit() == True:
            bucket.append(int(score))
        elif score == 'S':
            scoresum.append(bucket.pop() ** 1)
        elif score == 'D':
            scoresum.append(bucket.pop() ** 2)
        elif score == 'T':
            scoresum.append(bucket.pop() ** 3)
        elif score == '*':
            if len(scoresum) == 1:
                temp = scoresum.pop() * 2
                scoresum.append(temp)
            else:
                temp1 = scoresum.pop()
                temp2 = scoresum.pop()
                temp1 *= 2
                temp2 *= 2
                scoresum.append(temp2)
                scoresum.append(temp1)
        elif score == '#':
            temp = scoresum.pop() * -1
            scoresum.append(temp)
    return (sum(scoresum))


dartResult = '1D2S3T*'
print(solution(dartResult))


def solution2(dartResult):
    scoresum = []
    bucket = []
    SDT = ['S', 'D', 'T']
    for score in dartResult:
        if len(bucket) > 0 and score.isdigit() == True:
            bucket.pop()
            bucket.append(10)
        elif score.isdigit() == True:
            bucket.append(int(score))
        elif score in SDT:
            scoresum.append(bucket.pop() ** (SDT.index(score) + 1))
        elif score == '*':
            if len(scoresum) == 1:
                temp = scoresum.pop() * 2
                scoresum.append(temp)
            else:
                temp1 = scoresum.pop()
                temp2 = scoresum.pop()
                temp1 *= 2
                temp2 *= 2
                scoresum.append(temp2)
                scoresum.append(temp1)
        elif score == '#':
            temp = scoresum.pop() * -1
            scoresum.append(temp)
    return (sum(scoresum))

dartResult = '1D2S3T*'
print(solution2(dartResult))