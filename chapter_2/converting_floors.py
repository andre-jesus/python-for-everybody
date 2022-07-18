# inp = input("European Floor?")
# us_floor = int(inp) + 1

# print("US Floor", us_floor)


def lift_converter():
    eu_floor = input("What is the European flor you are at?").lower()

    if eu_floor == "groud floor":
        print("1")
    else:
        int_eu_floor = int(eu_floor)
        print(int_eu_floor + 1)


lift_converter()
