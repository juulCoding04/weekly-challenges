def hoursPassed(t1, t2):
    h1 = int(t1.split(" ")[0].split(":")[0])
    m1 = int(t1.split(" ")[0].split(":")[1])
    h2 = int(t2.split(" ")[0].split(":")[0])
    m2 = int(t2.split(" ")[0].split(":")[1])

    diff = h2 - h1

    if ("AM" in t1 and "PM" in t2) or ("PM" in t1 and "AM" in t2):
        diff += 12

    if diff == 0:
        print("no time passed")
        return -1
    
    print(str(diff) + " hours")
    return 0

if __name__ == "__main__":
    hoursPassed("1:00 AM", "3:00 PM")
    hoursPassed("2:00 PM", "4:00 PM")
    hoursPassed("3:00 AM", "9:00 AM")
    hoursPassed("4:00 PM", "4:00 PM")