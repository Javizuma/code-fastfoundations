import random
import sys


def double_number(n):
    return 2 * n


def using_map():
    """Double the given number"""
    random_numbers = random.choices(range(200), k=10)
    print(f"{random_numbers = }")
    print(f"{map(double_number, random_numbers) = }")


def using_map_and_lambda():
    """Using map with a lambda"""
    random_numbers = random.choices(range(200), k=10)
    print(f"{random_numbers = }")
    print(f"{map(lambda r: 2 * r, random_numbers) = }")


def using_filter():
    """Filter out words that are in the wrong case"""
    words = ["shock", "brink", "limited", "admission", "demonstration", "alive", "pen", "reactor", "ban", "sentence", ]
    print(f"{words = }")
    print(f"{filter(lambda w: len(w) > 7, words) = }")


def get_max(a_list):
    maximum = None
    first = False
    for value in a_list:
        if not first:
            maximum= value
            first= True
        if value > maximum:
            maximum = value
            pass
    return maximum


a_list = [1,7,9,22]
my_max=get_max(a_list)

print(f"my_max")

def main():
    using_map()
    using_map_and_lambda()
    using_filter()
    return 0


if __name__ == '__main__':
    sys.exit(main())
