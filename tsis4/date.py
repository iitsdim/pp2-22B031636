from datetime import date, timedelta, datetime


# 1
# year = int(input('Enter a year: '))
# month = int(input('Enter a month: '))
# day = int(input('Enter a day: '))
#
# d = date(year=year, month=month, day=day)
# print(d - timedelta(days=5))

# 2
# d = date.today()
# print(f"yesterday: {d - timedelta(days=1)}, today: {d}, tomorrow: {d + timedelta(days=1)},")

# 3
# d = datetime.now()
# print(f"before: {d}")
# d = d.replace(microsecond=0)
# print(f"after {d}")
# 4
def input_date():
    year = int(input('Enter a year: '))
    month = int(input('Enter a month: '))
    day = int(input('Enter a day: '))

    d = date(year=year, month=month, day=day)
    return d


a = input_date()
b = input_date()
c = b - a
print(c.total_seconds())
