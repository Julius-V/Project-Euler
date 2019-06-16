dict_month = {1: 1, 2: 4, 3: 4, 4: 0, 5: 2, 6: 5,
              7: 0, 8: 3, 9: 6, 10: 1, 11: 4, 12: 6}


# Converting a date to a weekday: 0 - Saturday, 1 - Sunday, 2 - Monday, ..., 6 - Friday
def get_weekday(day, month, year):
    return ((year % 100) // 4 + day + dict_month[month] -
            ((month in [1, 2]) & (year % 4 == 0)) + 6 * (year // 100 == 20) +
            year % 100) % 7


# Counting certain weekdays (from 0  to 6) from 1 Jan 1901 to 31 Dec 2000
def count_weekdays(target):
    cnt = 0
    for year in range(1901, 2000 + 1):
        for month in range(1, 12 + 1):
            cnt += get_weekday(1, month, year) == target
    return cnt


print(count_weekdays(1))
