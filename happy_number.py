def proverka_bileta():
    a = input()
    T = []
    try:
        int(a)
    except:
        print("Введите число")
        proverka_bileta()
    if len(a) == 6:
            for i in a:
                T.append(int(i))


            s = sum(T[:3])
            s1 = sum(T[3:])

            if s == s1:
                print("У вас счастливый билет")
                exit()
            else:
                print("У вас не счастливый билет, попробуйте еще раз")
                proverka_bileta()
    else:
        print("Введите шестизначное число")
        proverka_bileta()
print(proverka_bileta())
