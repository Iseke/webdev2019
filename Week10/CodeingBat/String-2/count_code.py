def count_code(str):
    cnt = 0
    for x in range(len(str) - 3):
        if str[x:x + 2] == "co" and str[x + 3] == "e":
            cnt += 1

    return cnt

