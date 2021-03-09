def solution(s):
    list(s)
    slist = list(s.split(" "))
    newlist = []
    for i in range(len(slist)):
        for j in range(len(slist[i])):
            word = slist[i]
            str(word)
            if j % 2 == 0:
                newlist.append(word[j].upper())
            else:
                newlist.append(word[j].lower())
        newlist.append(' ')
    answer = newlist[:-1]
    realanswer = ''.join(answer)
    return realanswer


s = 'try hello world'
print(solution(s))