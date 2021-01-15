I = input()
Sum = 0
for i in str(I):
    if ord(i) >= 65 and ord(i) <68:
        Sum += 3
    elif ord(i) >= 68 and ord(i) < 71:
        Sum += 4
    elif ord(i) >= 71 and ord(i) < 74:
        Sum += 5
    elif ord(i) >= 74 and ord(i) < 77:
        Sum += 6
    elif ord(i) >= 77 and ord(i) < 80:
        Sum += 7
    elif ord(i) >= 80 and ord(i) < 84:
        Sum += 8
    elif ord(i) >= 84 and ord(i) < 87:
        Sum += 9
    elif ord(i) >= 87 and ord(i) < 91:
        Sum += 10
print(Sum)