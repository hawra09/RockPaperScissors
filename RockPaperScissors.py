import random

def rock_paper_scissors():
    win_count = 0
    lose_count = 0
    computer_choices = ['Rock', 'Paper', 'Scissors']
    while True:
        user_input = input('Please enter Rock, Paper, or Scissors').strip().title()
        random_computer_choices = random.choice(computer_choices)
        print(f'Computer chose: {random_computer_choices}')
        if user_input not in computer_choices:
            print('Error: Please enter Rock, Paper, or Scissors')
            continue
        elif user_input == random_computer_choices:
            print('It is a tie!')
        elif (user_input == 'Rock' and random_computer_choices == 'Scissors') or (user_input == 'Paper' and random_computer_choices == 'Rock'):
            print('You Win!')
            win_count += 1
        elif (user_input == 'Rock' and random_computer_choices == 'Paper') or (user_input == 'Scissors' and random_computer_choices == 'Rock'):
            print('You lose')
            lose_count += 1
        continue_playing = input('Would you like to continue playing? Y or N').upper().strip()
        if continue_playing == 'N':
            print(f'Thank you for playing!\n You won {win_count} number of times and lost {lose_count} number of times!')
            break


rock_paper_scissors()