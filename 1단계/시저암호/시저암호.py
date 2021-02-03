def solution(s, n):
    answer = ''
    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
        else:
            if ord(s[i]) >= 97 and ord(s[i]) + n > 122:
                answer += chr((ord(s[i]) + n) - 26)
            elif ord(s[i]) <= 90 and ord(s[i]) + n > 90:
                answer += chr((ord(s[i]) + n) - 26)
            else:
                answer += chr(ord(s[i]) + n)
    return answer


s = "z"
n = 1
print(solution(s, n))
