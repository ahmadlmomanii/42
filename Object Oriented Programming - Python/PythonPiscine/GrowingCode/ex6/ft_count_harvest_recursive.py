def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def rec(day):
        if day > days:
            print("Harvest time!")
            return
        print("Day", day)
        rec(day + 1)
    rec(1)
