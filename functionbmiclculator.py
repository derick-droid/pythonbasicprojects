def bmi_calculator(name, height, weight ):
    bmi = weight / (height ** 2)
    print("your bmi is: ", bmi)
    if bmi < 25:
        print("hello " + name + " you have a normal bmi. ")
    else:
        print("hello " + name + " you have a normal bmi.")
    return bmi


bmi1 = bmi_calculator("derrick okinda", 23, 45)
bmi1 = bmi_calculator("edna okinda", 23, 45)
bmi1 = bmi_calculator("asenath viki okinda", 23, 45)




