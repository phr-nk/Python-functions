def indexes(string, char):
    '''this function takes a string and char parameter and returns a list of how many times that char was located in the string'''
    index_l = []
    for i in range(len(string)):
        if string[i]== char:
            index_l.append(i)
        else:
            continue
    return index_l

def doubles(numberList):
    '''takes a list and returns a list of numbers that have a value double its size in the list'''
    double_list = []
    for i in range(len(numberList)-1):
        if numberList[i+1] == numberList[i]*2:
            double_list.append(numberList[i+1])
    return double_list
        
def rps(play1, play2):
    '''This function replicates the game rock paper scissors and returns -1 if play1 wins and 1 if play2 and 0 if there is a tie'''
    if (play1 == 'R' and play2 == 'S') or \
       (play1 == 'P' and play2 == 'R') or \
       (play1 == 'S' and play2 == 'P'):
        return -1
    elif (play1 == 'R' and play2 == 'P') or \
         (play1 == 'P' and play2 == 'S') or \
         (play1 == 'S' and play2 == 'R'):
        return 1
    elif play1 == play2:
        return 0

def tableMax(table):
    ''''takes a table pf floats as a parameter and goes through the table to find the max value in the table and then returns it'''
    max_n = 0.0
    
    for i in table:
        if max_n == 0:
            max_n = max(i)
        else:
            max_n = max(max_n, max(i))
    return max_n

def columnMins(table):
    '''This function takes a 2D table of floats and return the list of the min value in each column'''
    min_col = []
    new_l = []
    col = 0
    for j in range(len(table[col])):
        for i in range(len(table)):
            min_col += [ table[i][col] ]
        col +=1
        new_l.append(min(min_col))
        min_col = []
    return new_l
