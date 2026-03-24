def ft_count_harvest_recursive(n=None, actual=1):
    if n is None:
        print('Days until harvest: ', end="")
        n = int(input())
    if actual > n:
        print('Harvest time!')
        return
    print('Day', actual)
    ft_count_harvest_recursive(n, actual + 1)
