def letter2number(letter):
    '''this function takes as input a string which is a letter with either a + or - for the students grade. There is then a defnied dictionary that has the number value of each grade and it returns it to the user.'''
    letter_grades = {'A+' : 4.3, 'A' : 4, 'A-' : 3.7, 'B+' : 3.3, 'B' : 3, 'B-' : 2.7, 'C+' : 2.3, 'C' : 2, 'C-' : 1.7, 'D+' : 1.3, 'D': 1, 'D-' : 0.7, 'F+' : 0.3,'F': 0, 'F-' : -0.7}
    
    return letter_grades[letter]

def ex613():
    '''This function defines a dictionary and then adds a whole new value and changes a current value. Then it removes two values at the end.'''
    agencies = {'CCC' :  "Civilian Conservation Corps", 'FCC' : 'Federal Communications Commission', 'FDIC' : 'Federal Deposit Insurance Corporation', 'SSB' : 'Social Security Board', 'WPA' : 'Works Progress Administration'}
    agencies['SEC'] = 'Securities and Exchange Commission'
    agencies['SSB'] = 'Social Security Administration'
    del agencies['CCC']
    del agencies['WPA']
    return agencies
def reverse(phonebook):
    '''This function takes as input a dictionary that acts a phone book and returns a dictionary with the keys and values flipped.'''
    new_phonebook = {}
    for key, value in phonebook.items():
        new_phonebook[value] = key
    return new_phonebook
def different(table):
    '''This function takes as input a 2D table and returns the number of distinct numbers'''
    set_1 = set()
    for i in range(len(table)):
        for j in range(len(table[i])):
            set_1.add(table[i][j])
        
    return len(set_1)

def index(textfile,listOfWords):
    '''this fucntion takes as input a textfile name and a list of words to find in that text file, it then goes through the file to see what lines each of the words in the list appear on and then prints them out for the user'''
    new_d = {}
    set_s = set(listOfWords)
    infile = open(textfile, 'r')
    contents = infile.readlines()
    for line in range(len(contents)): #goes through lines of text
        words = contents[line].split(' ') # splits up line into words
        for word in words:
            if word.lower() in set_s:
                new_d[line+1] = word
            elif word[0:-1].lower() in set_s:
                new_d[line+1] = word[0:-1]
    for k, v in new_d.items():
        if len(v) > 5:
            print('{0}  {1}'.format(v,k))
        elif len(v) < 5:
            print('{0}     {1}'.format(v,k))
        else:
            print('{0}    {1}'.format(v,k))
        

    infile.close()
        
        
    
    

    
        
        
    
