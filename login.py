users = {}
with open('users.txt', 'r+') as file:
    #This section accesses the user data file and maps it to a dictionary
    #this allows the program to interpret it meaningfully
    while True:
        line = file.readline().split('|')
        if len(line) == 1: break #skip empty lines - catch for e.g. deleted users
        userdata = {}
        line[2] = line[2].strip()

        
        for i in line[2].split('  '):
            data = i.split(':')
            num = int(data[0])
            values = data[1].split(',')
            for j, value in enumerate(values):
                values[j] = int(value)
            userdata[num] = values
        users[line[0]] = [line[1], userdata]
        


def login(): #main login program
    while True:
        #get user choice - login or register?
        choice = input('Would you like to <1> sign in or <2> register a new account? ')
        if choice.lower() in ('1','2','exit'): #validate input
            break
        print('Please enter a number, <1> or <2>.')
    

    if choice == '1':
        username = signin() #run signin module if they choose sign in
    elif choice == '2':
        username = register() #run register module if they choose register
    else:
        return False, False 
        #if the user tries to exit, return username and userdata as False
        #this is received and handled by the main program.

    return username, users[username][1] #return the username and password to the main program

def signin():
    while True:
        username = input('Enter your username: ')
        if username in users:
            break
        print('Sorry, your username wasn\'t found. Please try again.')
        #check that the user enters a username that is in the 
    while True:
        password = input('Enter your password: ')
        if password == users[username][0]:
            break
        print('Sorry, your username/password combination is wrong. Please try again.')
    return username

def get_username(): #part of the registration process
    while True:
        while True:
            username = input('Username: ') #user input the 
            if ' ' not in username and ':' not in username and '|' not in username:
                #user must enter a valid username, without special characters used to separate data in the file.
                break
            print('Spaces-> " ",  colons -> ":"  and pipes-> "|" ',
                  'are not allowed in usernames. Please try again.')

        if username not in users: #check that the username has not been taken
            break

        print('Username is taken.',
              'Would you like to <1> login or <2> register under a different name?') 
              #give the user the choice to login if they remember they have an account already 
        while True:
            choice = input('->')
            if choice in ['1', '2']:
                break
            print('Please enter a number, 1 or 2.')
        if choice == 2:
            get_username()
            #this line uses recurrence - if the user wants to register under a different name, this
            #  subroutine will execute again to get their username. It then passes the username that
            # the user decided on back up to the previous iteration, all the way up until the original.
        break
    return username

def register():
    username = get_username() #get the user's username
    while True:
        password = input('Enter your password: ')
        passwordconfirm = input('Confirm your password: ')
        if password == passwordconfirm:
            break
        print('Sorry, your passwords don\'t match.')
        #get a valid password from the user, ensuring that their confirmation password matches it.

    userdata=''
    for i in range(2,13):
        userdata += f'{i}:0,0  '
    userdata = userdata.strip()
    #create the userdata as a string
    
    users[username] = [password, userdata]
    with open('users.txt', 'a') as file:
        file.write('%s|%s|%s\n' % (username, password, userdata))
    #store the userdata in the text file users.txt
    
    return username #pass the username back to the main program.

#username, password = login()
#print('Your username is %s' % username)
#print('Your password is %s' % password)
