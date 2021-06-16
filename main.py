from login import login
from practice3 import practice
from stats import stats

username, userdata = login() #run the login subroutine
if username == False and userdata == False:
    print('Goodbye!')
    exit()
#check that the user didn't ask to exit - 'false/false' means they entered 'exit'


print(f'Welcome, {username}!')
print('To go back to a previous menu, or to exit on the main menu, type "exit".')
#welcome the user

menu_choice = '0'
while menu_choice.lower() not in ('3','exit'):
    print('\nWhat would you like to do?\n<1> Practice\n<2> Stats\n<3> Exit')
    menu_choice = input('->')
    #main menu - get the user's input
    if menu_choice == '1':
        practice(username)
        #if the user selects practice, run the practice module

    elif menu_choice == '2':
        stats(username)
        #if the user selects stats, run the stats module

    elif menu_choice == '3' or menu_choice.lower() == 'exit':
        break
    #if the user selects exit, exit

    else:
        print('Sorry, I didn\'t understand that. Please try again and choose a number.')
        #if the user didn't make a selection, ask them again.
print('Thanks for playing!')
#once the user has selected to exit, thank them for playing then exit
