def money():
    import keyboard, os
    from random import randint
    day = 4
    money = 0
    pay = 1
    days = 0
    plus5cost = 40
    while True:
        if days == 25:
            pay += randint(1, 4)
            days = 0
        else:
            while day > 5:
                day -= 5
            if day < 0:
                day = 0
            if day == 0:
                os.system('cls')
                print(f'---Main Page---\nDollars: {money}\nDays till payday: {day}\n1. Next day\n2. Shop\n3. Payday\n')
            else:
                os.system('cls')
                print(f'---Main Page---\nDollars: {money}\nDays till payday: {day}\n1. Next day\n2. Shop')
            if keyboard.read_key() == "1":
                os.system('cls')
                day -= 1
                days += 1
            if keyboard.read_key() == '2':
                os.system('cls')
                print(f'---Shop---\nDollars" {money}\nq. Add 5 to pay: {plus5cost}\np. Exit')
                plus5cost += randint(1, 10)
            if keyboard.read_key() == 'q':
                if money >= 50:
                    pay += 5
                    money -= 50
                day -= 1
                days += 1
            if keyboard.read_key() == 'p':
                day -= 1
                days += 1
                continue
            if keyboard.read_key() == '3':
                os.system('cls')
                if day == 0:
                    money += pay
                    day = 4
money()
