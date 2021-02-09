def converter(miles):
    km_miles = 1.6 * miles
    if miles <= 100:
        print("invalid value. ")
    else:
        print(km_miles)
    return km_miles


result = converter(int(input("enter mile: ")))
