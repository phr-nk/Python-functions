import random
def craps():
    '''This function implements the game craps which lets the player start with two six sided dice and if the player rolls a 7 or 11, they win, else if they roll a 2, 3 or 12 they lose. Any other number lets the player make another roll until they roll one of those values'''
    keeprolling = True
    while(keeprolling):
        die1 = random.randrange(1,7)
        die2 = random.randrange(1,7)
        score = die1 + die2
        if score in {7,11}:
            return 1
            keeprolling = False
        elif score in {2,3,12}:
            return 0 
            keeprolling = False
        

def testCraps(n):
    '''This function takes as input the number of games the user wants to play and returns the fraction of games the player won '''
    gameswon = 0
    totalgames = n
    while n > 0:
        game = craps()
        if game == 1:
            gameswon += 1
            n -= 1
        else:
            n -= 1
            continue
        
    return gameswon / totalgames

def game(n):
    '''This is a simple program of an addition game, it takes an int n as input which is the number of games the user wants to play, this function also that handles none integer input '''
    isString = True
    while(n > 0):
        firstnum = random.randrange(0,9)
        secondnum = random.randrange(0,9)
        print('{0} + {1} = '.format(firstnum,secondnum))
        while isString:
            try:
                answer = int(input('Enter answer: '))
                isString = False
            except:
                print('Please write your answer using digits 0 through 9, Try again!')
        numsum = firstnum + secondnum
        if numsum == answer:
            print('Correct!')
        else:
            print('Incorrect :(')
        n -= 1
    

def networks(n, friends):
    ''''This function takes as input the number of friends in a class and which of the students are friends. It then determines which students are friends and returns a list of sets of the different social groups '''
    list_sets = []
    answer = []
    for i in range(len(friends)):
        list_sets.append(set(friends[i]))
    for j in range(len(list_sets)-1):
        inter_s = set()
        inter_s = list_sets[j].intersection([j+1])
        if inter_s.issubset(list_sets[j]) and inter_s.issubset(list_sets[j+1]):
            new_t = list_sets[j].union(list_sets[j+1])
            answer.append(new_t)
        else:
            answer.append(list_sets[j+1])
              
    return answer
 
        
            
            



