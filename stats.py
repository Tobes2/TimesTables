from math import floor #used to find the user's % success
def stats(username):
    with open('users.txt', 'r') as f:
        for line in f.readlines(): #for each line in the file:
            #get username
            line = line.strip()
            line = line.split('|')

            #following code for correct user's ID:
            if line[0]==username:
                rawdata = line[2].split('  ')
                userdata = {} #put userdata into a dictionary for easy access
                for i in rawdata:
                    j = i.split(':')
                    key = int(j[0])
                    value = j[1].split(',')
                    for i in range(len(value)):
                        value[i] = int(value[i])
                    userdata[key] = value

    

    print()
    timestablesdic = {
        2: 'Twos:    ',
        3: 'Threes:  ',
        4: 'Fours:   ',
        5: 'Fives:   ',
        6: 'Sixes:   ',
        7: 'Sevens:  ',
        8: 'Eights:  ',
        9: 'Nines:   ',
        10:'Tens:    ',
        11:'Elevens: ',
        12:'Twelves: ',
    }
    #match the numbers in userdata to meaningful words to show the user
    for i in userdata:
        attempts = userdata[i][0]
        correct = userdata[i][1]
        #access the userdata for each number, specifically attempts and correct answers
        print(timestablesdic[i], end='')
        if attempts == 0:
            print('Never tried!')
            #for numbers where the user has not ever tried a question
            # this is to prevent errors due to division by 0: 
            # 0 correct and 0 attempts means 0/0 = ?? -> error 
        else:
            percent = floor(correct/attempts*100)
            print(f'{correct} / {attempts} = {percent}%')
            #show the user their stats
    print() #extra line to make it clearer
    return #back to menu
