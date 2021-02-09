name = input("emter your name:  ")
age = int(input("enter your age:  "))
height = int(input("enter heigth(m): "))
weight = int(input("enter weight:  "))

bmi = weight / (height * height)

if bmi < 25:
    print("hey " + name + " you are not overweight. ")
else:
    print("hey " + name + "you are overweight. ")