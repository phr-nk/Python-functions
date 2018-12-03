def doubleList(listOfNumbers):
    '''This function takes a list as a parameter and modifies the orignal input list to be double'''
    for i in range(len(listOfNumbers)):
        listOfNumbers[i] = listOfNumbers[i] * 2 # change each position of the original list to be double its original value
    #doesn't return anything, just changes original list
        
def acronym(stringOfWords):
    '''Takes as a string a sequence of strings seperated by spaces. It then takes the first letter of each string to form an acronym and returns that string'''
    word_list = stringOfWords.split(' ')#split the input string into a list of strings 
    acronyms = "" #new string to add first letters to and to then return at the end of the function
    #go through the list of words and add the first letter of each word into a new string
    for i in word_list:
         acronyms += i[0]

    return acronyms.upper()#capitalize the letters in the new acronym string


def multiples(listOfInts, n):
    '''Function takes two agruments, a list of ints and a integer n. It then returns a new list of numbers that consist of the numbers that are multiples of n from the orginal list.'''
    mult_list = [] #new list
    for i in range(len(listOfInts)):
        if listOfInts[i] % n == 0: #checks if there is a remainder when the two numbers are divided by each other and if there is not, append the number[i] to the new list
            mult_list.append(listOfInts[i])
        else:
            continue
    return mult_list
            
def formatNames(inName, outName):
    '''Takes two arguments, the file to read and the output file to write to. It then looks through the file to see if its one of two formats then create a new file with the names as either last, first or last,first M.'''
    last = ''
    first = ''
    middle = ''
    name = []
    infile = open(inName,'r')
    contents = infile.readlines()
    infile.close()
    outfile = open(outName,'w')
    for i in range(len(contents)):
        name = contents[i].split()
        if len(name) == 3:
            last = name[2]
            middle = name[1][0]
            first= name[0]
            outfile.write('{}, {} {}.\n'.format(last,first,middle))
            
        else:
            last = name[1]
            first = name[0]
            outfile.write('{}, {}\n').format(last,first)
            

    outfile.close()
        
    
    
def partition(listOfStrings, letter):
    '''Takes a list of strings and a character as parametersand will return the list of strings from the input list that begin with the letter a until the letter desired in the parameter.'''
    new_l = [] #new list
    for i in listOfStrings:
        if i[0].upper() <= letter.upper(): #checks if the first letter is less than or equal to the input character
            new_l.append(i)#if so, append i to the new list
    return new_l

            

    
