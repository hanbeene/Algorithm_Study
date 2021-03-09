while True:
    Auset, Ausar, Heru = map(int,input().split())
    if Auset == 0 and Ausar == 0 and Heru == 0:
        break
    if (Auset*Auset)+(Ausar*Ausar) == (Heru*Heru) or (Auset*Auset)+(Heru*Heru) == (Ausar*Ausar) or (Heru*Heru)+(Ausar*Ausar) == (Auset*Auset):
        print('right')
    else:
        print('wrong')