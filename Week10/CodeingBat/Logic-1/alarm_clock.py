def alarm_clock(day, vacation):
    if not vacation and day in range(1, 6):
        return "7:00"
    if not vacation and (day == 0 or day == 6):
        return "10:00"
    if vacation and day >= 1 and day <= 5:
        return "10:00"
    if vacation and day == 0 or day == 6:
        return "off"

