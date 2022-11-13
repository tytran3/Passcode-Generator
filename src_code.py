import random

letters_arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers_arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols_arr = ['!', '@', '#', '$', '%', '&', '*']
password = []

print("Do you want to generate a password? ( Y / N )")
response = input().upper()

if (response == "Y") or (response == "YES"):
    print("Great! Let's do it")
    letters = int(input("How many letters? "))
    numbers = int(input("How many numbers? "))
    symbols = int(input("How many symbols? "))

    for i in range(1, letters + 1):
        password.append(random.choice(letters_arr))
    for i in range(1, numbers + 1):
        password.append(random.choice(numbers_arr))
    for i in range(1, symbols + 1):
        password.append(random.choice(symbols_arr))

    random.shuffle(password)
    final_password = ""

    for char in password:
        final_password += char
    print(final_password)

elif (response == "N") or (response == "NO"):
    print("That's okay! Maybe next time")
else:
    print("Invalid request")
