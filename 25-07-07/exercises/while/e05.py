# Ask for a password, allow max 3 attempts
# RULES:
# - Use a while loop
# - Allow the user to enter a password up to 3 times
# - If the password is correct, print "Access granted"
# - If the password is incorrect, print "Incorrect" and allow another attempt
attempts = 0
correct_pwd = "forzapalermo27"

pwd = input("Insert password: ")

while attempts < 2:
    if pwd == correct_pwd:
        print("Correct!")
        break

    print("Wrong")
    attempts += 1
    pwd = input("Insert password: ")
    if attempts == 2:
        print("Wrong, no more tries")
        break
