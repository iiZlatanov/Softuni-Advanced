honey_needed = float(input())
total = 0
flag = False

while True:
    if flag:
        break
    name_of_the_bee = input()
    if name_of_the_bee != 'Winter has come':
        for i in range(6):
            monthly_honey_carried_by_the_bee = float(input())
            total += monthly_honey_carried_by_the_bee
            if monthly_honey_carried_by_the_bee < 0:
                print(f'{name_of_the_bee} was banished for gluttony')
        if total < 0:
            print(f'{name_of_the_bee} was banished for gluttony')
        if total >= honey_needed:
            print(f'Well done! Honey surplus {(total - honey_needed):.2f}.')
            flag = True
            break
    elif name_of_the_bee == 'Winter has come':
        if total >= honey_needed:
            print(f'Well done! Honey surplus {(total - honey_needed):.2f}.')
            flag = True
            break
        elif total < honey_needed:
            print(f'Hard winter! Honey needed {(honey_needed - total):.2f}.')
            flag = True
            break
    if total > honey_needed:
        print(f'Well done! Honey surplus {(total - honey_needed):.2f}.')
        exit()