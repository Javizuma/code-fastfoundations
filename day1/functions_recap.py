import sys

def get_squareDict(my_dict):
    result_dict= dict()

    for key,value in my_dict

        result_dict[key]= value * value

    return result_dict





def main():
    dictionary = dict("one": 1, "two": 2, "three": 3, "nine": 9)
    print(my_max)
    a = int(input("a: "))
    r = str(input("r: "))

    def using_filter():
        """Filter out words that are in the wrong case"""
        words = ["shock", "brink", "limited", "admission", "demonstration", "alive", "pen", "reactor", "ban",
                 "sentence", ]
        print(f"{words = }")
        print(f"{filter(lambda w: len(w) > 7, words) = }")



    n = int(input("n: "))

    print(f"s_n = {calculate_geometric_series(a, r, n)}")
    return 0

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





if __name__ == "__main__":
    sys.exit(main())
