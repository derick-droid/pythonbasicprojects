secret_number = 9
guess_counts = 0
guess_limit = 3
while guess_counts < guess_limit:
    guess = int(input("GUESS:  "))
    guess_counts += 1
    if guess == secret_number:

       print("win")
       break

else:
    print("failed")