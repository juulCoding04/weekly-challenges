def format_phone_number(numbers):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*numbers)

if __name__ == "__main__":
    print(format_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
    print(format_phone_number([5, 1, 9, 5, 5, 5, 4, 4, 6, 8]))
    print(format_phone_number([3, 4, 5, 5, 0, 1, 2, 5, 2, 7]))