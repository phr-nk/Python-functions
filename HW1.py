def computeTuition():
    'Takes the students number of credit hours and the amount of tution per credit hour which the returns total tuition cost'
    creditHours = int(input("Enter the number of credit hours: ")) #takes user input for amount of credit ours
    cost = float(input("Enter the cost per credit hour: "))#takes user input for cost per credit hour
    totalTuition = creditHours * cost #calculates total 
    return totalTuition


def createStr(character, number):
    'This function takes a single letter string and creates a string the length of the second parameter, if the second parameter is less than or equal to 0 it returns the orginal string'''
    temp = str(character * eval(number))
    return temp


def sequences():
    'Uses the for loop and range method to print out rows of values, each with different start/end points and '''
    for i in range(18, 52, 2):
        print(i, end=" ")
    print(" ")
    for i in range(27,99,9):
        print(i, end=" ")
    print(" ")
    for i in range(40, 10, -4): 
        print(i, end= " ")
        
        

def printAllBut(s):
    'Prompts user to type a list of strings and it will print all of the strings in that list except for the one that is the parameter'''
    list_str = eval(input("Type a list of strings: "))
    for i in range(len(list_str)): #goes through the list of strings
        if s.lower() == list_str[i].lower(): #if the string given as a parameter equals the string at i, skip it
            continue
        else:
            print(list_str[i]) #else contiune printing 
        
    


def printNth(n):
    'User types a list as in put and the function returns the nth element in the list and nothing if it is not in the list'''
    num_list = eval(input("Type a list: ")) #takes as input a list which is evaluated
    if -len(num_list) <= n < len(num_list): #valid indices are negative ones down to -len(num_list) inclusive, and non negative ones up to len(num_list) exclusive
        print(num_list[n])
    else:
        return
        
    
   
    
    
