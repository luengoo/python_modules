def ft_count_harvest_iterative():
    print('Days until harvest: ', end="")
    until_harvest = int(input())
    i = 1
    while i <= until_harvest:
        print('Day', i)
        i += 1
    print('Harvest time!')
