def check_the_place(easting, northing):
    check_result = False
    if (430000 <= easting <= 465000) and (80000 <= northing <= 95000):
        check_result = True
    return check_result


if __name__ == "__main__":
    print(check_the_place(223456,234565478))
    print(check_the_place(440000,90000))