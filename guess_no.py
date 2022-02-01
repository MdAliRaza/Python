print('''
It's a Guess Game you have to guess for secret number between 0-10
You have 3 chances.
''')
secret_no = 9
guess_limit = 3
guess_count = 0
while guess_count < guess_limit:
    guess = int(input("Guess :"))
    guess_count += 1
    if guess == secret_no:
        print("Congratulation's You Won")
        break
else:
    print("Guess Over You Lost")
print("Thanks for playing.")