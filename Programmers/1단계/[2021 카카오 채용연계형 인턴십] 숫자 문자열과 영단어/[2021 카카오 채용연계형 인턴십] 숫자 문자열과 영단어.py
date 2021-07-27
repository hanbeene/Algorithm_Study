def solution(s):
    dict = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
            "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    str = ''
    answer = ''
    for i in s:
        if i.isdigit() == False:
            str += i
            if str in dict:
                answer += dict.get(str)
                str = ''
        else:
            answer += i

    return int(answer)

s = "23four5six7"
print(solution(s))
