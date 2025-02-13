import sys


def using_math_library():
    import math
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    discriminant = b ** 2 - 4 * a * c
    if discriminant >= 0:  # real
        x1 = (-b + math.sqrt(discriminant)) / 2 / a
        x2 = (-b - math.sqrt(discriminant)) / 2 / a
    else:  # imaginary
        x1 = complex(-b / 2 / a, math.sqrt(-discriminant) / 2 / a)
        x2 = complex(-b / 2 / a, -math.sqrt(-discriminant) / 2 / a)
    print(f"{x1 = }")
    print(f"{x2 = }")


def using_cmath_library():
    import cmath
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    discriminant = b ** 2 - 4 * a * c
    x1 = (-b + cmath.sqrt(discriminant)) / 2 / a
    x2 = (-b - cmath.sqrt(discriminant)) / 2 / a
    print(f"{x1 = }")
    print(f"{x2 = }")


def using_datetime_library():
    import datetime
    from zoneinfo import ZoneInfo # https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
    print(datetime.datetime(2022, 4, 28, 11, 14, 32, 13432, ZoneInfo('Asia/Ashkhabad'))) # datetime
    print(datetime.date(2022, 4, 28)) # date
    print(datetime.time(14, 33, 7, 23422, ZoneInfo('Asia/Baku'))) # time
    datetime1 = datetime.datetime(2013, 9, 7, 8, 39, 58, 27389, ZoneInfo('Australia/Lindeman'))
    datetime2 = datetime.datetime.now(ZoneInfo('Europe/Kyiv'))
    print(f"{datetime2 - datetime1 = }") # timedelta
    print(f"{datetime.date.today() = }")

def using_shuffle():
    import random
    my_lits = list(range(127, 349))
    random.shuffle(my_list)
    print(f"{my_list=}")
    for _ in range(10): #if we use
        print(f"{random.choice(another_list) =}")
    print(f"{random.choices(another_list,k=10)}")

def using_stats():
    import statistics
    import random
    values = random.choice(range(20), k=20)
    print(statistics,mean(values))
def organize_ghana():
    import csv
    ghana_data=dict()
    ivory_coast_data= dict()
    with open('FAOSTAT_data_7-23-2022.csv') as f:
        fao_reader = csv.reader(f)
        for row in fao_reader:
            if row[3] == 'Ghana':
                data = row[11]
                year = row[9]
                pass
            elif row[3] =='Côte d’Ivoire':
                pass

def main():
    # using_math_library()
    # using_cmath_library()
    # using_datetime_library()
    #using_shuffle
    organize_ghana()
    return 0


if __name__ == '__main__':
    sys.exit(main())
