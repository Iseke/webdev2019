higher = 0


def caught_speeding(speed, is_birthday):
    if is_birthday:
        higher = 5
    else:
        higher = 0
    if 60 + higher >= speed: return 0
    if 61 + higher <= speed and speed <= 80 + higher:
        return 1
    else:
        return 2

