weight = int(input("enter your weight:  "))
unit = input("(L)bs or (K)gs:   ").lower()
if unit == "k":
    uniques = weight * 45
    print(f"you are {uniques} kilos ")
elif unit == "l":
    uniques = weight / 0.45
    print(f"you are {uniques} pounds ")