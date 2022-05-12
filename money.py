def money():
    import keyboard, os
    day = 9
    money = 0
    pay = 1
    days = 0
    while True:
        if days == 50:
            if pay < 10:
                pay += 2
            else:
                pay += 1
            days = 0
        else:
            while day > 10:
                day -= 10
            if day < 0:
                day = 0
            if day == 0:
                print(f'---Main Page---\nDollars: {money}\nDays till payday: {day}\n1. Next day\n2. Shop\n3. Payday\n')
            else:
                print(f'---Main Page---\nDollars: {money}\nDays till payday: {day}\n1. Next day\n2. Shop')
            if keyboard.read_key() == "1":
                os.system('cls')
                day -= 1
                days += 1
            if keyboard.read_key() == '2':
                print()
            if keyboard.read_key() == '3':
                os.system('cls')
                if day == 0:
                    money += pay
                    day = 9
money()