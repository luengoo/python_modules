def ft_plant_age():
    print('Enter plant age in days: ', end="")
    plant_age = int(input())
    if plant_age > 60:
        print('Plant is ready to harvest!')
    else:
        print('Plant needs more time to grow')
