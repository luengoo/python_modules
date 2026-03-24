def ft_water_reminder():
    print('Days since last watering: ', end="")
    watering = int(input())
    if watering <= 2:
        print('Plants are fine')
    else:
        print('Water the plants!')
