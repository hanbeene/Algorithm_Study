I = input()
J = ['c=','c-','dz=','d-','lj','nj','s=','z=']
sum = 0
for i in range(len(I)):
    if I[i:i+2] in J:
       sum += 1
    elif I[i:i+3] in J:
        sum += 1
print(len(I) - sum)
