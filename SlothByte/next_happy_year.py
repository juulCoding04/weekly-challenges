def nextHappyYear(year):
    next_year = list(map(int, str(year+1)))

    while (len(next_year) != len(set(next_year))):
        y = int("".join(map(str, next_year)))
        next_year = list(map(int, str(y+1)))
    
    return int("".join(map(str, next_year)))

if __name__ ==  "__main__":
    print(nextHappyYear(2017))
    print(nextHappyYear(1990))
    print(nextHappyYear(2021))