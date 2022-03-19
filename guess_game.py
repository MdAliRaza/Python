questions = {
    "1> Who created python": "A",
    "2> It was created in year": "B",
    "3> Python created in country": "C",
    "4> Extention of python": "A"
}
options = [['A. Guido Van Rossum', 'B. Elon Musk', 'C. James Gosling', 'D. Bjarne Stroustrup'],
           ['A. 1899', 'B. 1989', 'C. 1991', 'D. 1997'],
           ['A. india', 'B. brazil', 'C. netherlands', 'D. usa'],
           ['A. .py', 'B. .python', 'C. .p', 'D. None of the Above']]


# ------------------------#

def new_game():
    guesses = []
    correct_guess = 0
    question_no = 1

    for ques in questions.keys():
        print('------------------------')
        print(ques)
        for option in options[question_no - 1]:
            print(option, end=' ')
        print()
        guess = input('CHOOSE: ').upper()
        guesses.append(guess)
        correct_guess += check_answer(questions.get(ques), guess)
        question_no += 1
    display_score(correct_guess, guesses)


# ------------------------#

def check_answer(answer, guess):
    if answer == guess:
        print('CORRECT')
        return 1
    else:
        print('WRONG')
        return 0


# ------------------------#

def display_score(correct_guess, guesses):
    print('---------')
    print('RESULTS')
    print('---------')

    print('ANSWERS', end='- ')
    for i in questions:
        print(questions.get(i), end=' ')
    print()

    print('GUESSES', end='- ')
    for i in guesses:
        print(i, end=' ')
    print()

    score = int((correct_guess / len(questions)) * 100)
    print('SCORE: ' + str(score) + '%')


# ------------------------#

def play_again():
    print()
    while True:
        user = input('WANNA PLAY AGAIN: ').upper()
        if user == 'YES':
            new_game()
        else:
            break

# ------------------------#



new_game()
play_again()

print()
print('Thank u for playing')
