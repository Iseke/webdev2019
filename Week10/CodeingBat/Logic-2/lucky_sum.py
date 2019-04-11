def lucky_sum(a, b, c):
    if a == 13:
        return 0
    if a != 13 and b == 13:
        return a
    if a != 13 and b != 13 and c == 13:
        return a + b
    if a != 13 and b != 13 and c != 13:
        return a + b + c


