import random
#import the random number module

def practice(name):
    global username
    username = name
    #create a global variable username, so it can be accessed by all the subroutines (specifically save)
    print(f'Hi {username}, welcome to practice!')

    while True: #not an endless loop - see 'return' statement when user enters 'exit' or '3'.
        while True:
            practicetype = input('What would you like to do?\n<1> Random Practice\n<2> User Targeted Practice\n<3> Exit\n->')
            if practicetype.lower() in ('1','2','3','exit'):
                break
            print('Please type 1, 2, or 3.')
            #menu with input validation

        if practicetype == '1':
            randompractice()
            randompractice()
            randompractice()
            #for random - ask three random questions

        elif practicetype == '2':
            while True:
                num1 = input('What number would you like to practice? ')
                if num1.isnumeric():
                    if int(num1) in range(2,13):
                        break
                print('Please enter a number, 2-12.')
            num1 = int(num1)
            targetedpractice(num1)
            targetedpractice(num1)
            targetedpractice(num1)
            #for targeted - choose a number first then ask three questions on it

        else:
            print('Bye!')
            return

def randompractice(): #randompracticemodule
    num1 = random.randint(2,12)
    num2 = random.randint(2,12)
    #select two random numbers

    while True:
        question = input(f'What is {num1} x {num2}? ')
        if question.isnumeric():
            question = int(question)
            break
        print('Please enter a number.')
    #ask the user the question + validate the input

    if question == num1*num2:
        print('Correct!')
        save(num1, num2, True)
    else:
        print('Sorry, that wasn\'t right. ')
        save(num1, num2, False)
    #check if the user was correct and save the result


def targetedpractice(num1):
    #num1 is a parameter - num2 is random
    num2 = random.randint(2,12)
    
    while True:
        question = input(f'What is {num1} x {num2}? ')
        if question.isnumeric():
            question = int(question)
            break
        print('Please enter a number.')
    #ask the user a question

    if question == num1*num2:
        print('Correct!')
        save(num1, num2, True)
    else:
        print('Sorry, that wasn\'t right. ')
        save(num1, num2, False)
    #check if the user was correct and save the result
    
def save(num1, num2, result): #save the result to the file. 
    #Done after every question so that progress is saved after a crash or unexpected termination.
    global username
    #import the global username variable
    with open('users.txt', 'r') as f: #access the file
        newfile = ''
        for line in f.readlines(): #for each line:
            if len(line)>0: #catch for empty lines
                #get username
                line = line.strip()
                line = line.split('|')

                #following code for correct user's ID:
                if line[0]==username:
                    rawdata = line[2].split('  ')
                    userdata = {}
                    for i in rawdata:
                        j = i.split(':')
                        key = int(j[0])
                        value = j[1].split(',')
                        for i in range(len(value)):
                            value[i] = int(value[i])
                        userdata[key] = value
                    
                    #start change data
                    userdata[num1][0]+=1
                    if result == True:
                        userdata[num1][1]+=1
                    if num1 != num2:
                        userdata[num2][0]+=1
                        if result == True:
                            userdata[num2][1]+=1
                    #end change data

                    #start reinsert new userdata
                    newline = line[0]+'|'+line[1]+'|'
                    for i in userdata:
                        newline = newline + str(i) + ':' + str(userdata[i][0]) + ',' + str(userdata[i][1]) + '  '
                    line = newline
                    #end reinsert new userdata
                
                else:
                    line = line[0]+'|'+line[1]+'|'+line[2]
                line = line.strip()
                newfile = newfile + line + '\n'
    f = open('users.txt', 'w') 
    f.write(newfile) #replace the existing file with the new, edited file
    f.close()
