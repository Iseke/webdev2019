upper = 0


def squirrel_play(temp, is_summer):
    if is_summer:
        upper = 100
    else:
        upper = 90
    return 60 <= temp and temp <= upper


