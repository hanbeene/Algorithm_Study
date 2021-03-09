def solution(phone_number):
    Numberlist = list(phone_number)
    NewNumber = ''
    for i in range(len(phone_number[:-4])):
        Numberlist[i] = '*'
    for j in range(len(Numberlist)):
        NewNumber += Numberlist[j]
    return NewNumber