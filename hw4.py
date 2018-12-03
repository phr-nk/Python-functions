def intersect(list1, list2):
    '''This function takes as input two seperate lists and returns a seperate l;ist of their common values'''
    
    dup_l = []
    for i in list1:
        for j in list2:
            if i == j:
                dup_l.append(i)
    return dup_l

def pay(wage, hours):
    '''This function takes as input an hourly wage and the number of hours worked in a week, it then computes and returns the employees pay, Any hours over 40 but less than equal to 60 should be paid 1.5 times the regular wage and any times beyond 60 should be paid twice the regular amount'''
    if hours < 40:
        return wage * hours
    elif hours > 40 and hours <= 60:
         payment = 40 * wage  # Standard Payment until 40 Hours
         payment = payment + wage * (hours-40) * 1.5
         return payment
    elif hours > 60:
        payment = 40 * wage
        overtime1 = (20*wage) *1.5
        new_total = payment + overtime1
        overtime2 = ((hours - 60) * wage) * 2
        return new_total + overtime2
    
def lastfirst(listOfStrings):
    '''This function takes one argument which is a list of strings in the format <LastName, FristName> and returns a list of two lists which are a list of all first names and all last names'''
    new_l = []
    last_l = []
    first_l = []
    for i in range(len(listOfStrings)):
        new_l.append(listOfStrings[i].split(', '))
    for j in range(len(new_l)):
        last_l.append(new_l[j][0])
        first_l.append(new_l[j][1])
    new_l = []
    new_l.append(last_l)
    new_l.append(first_l)
    return new_l

def inversions(string):
    '''This functin finds the inversions of a all caps string, an inversion is a pair of entries that are out of order The total number of inversions in a sequence is a measure of how unsorted the sequence is.'''
    if(len(string) <= 1):
        return 0
    count = 0
    for i in range(len(string)-1):
        for j in range(i+1, len(string)):
            if(string[i] > string[j]):
                count = count + 1

    return count
def sublist(list1, list2):
    ''' This function takes as input two lists and determines if the first list is a sub list of the second list, a list is a sub list if the all the values appear in the second list in the same order'''
    len1 = len(list1)
    len2 = len(list2)
    id1 = 0 
    id2 = 0 
   
    while id1 < len1 and id2 < len2:
        found = False
        while id2 < len2 and found == False:
            if list1[id1] == list2[id2]: 
                found = True
            else:
                id2 += 1
            
        if found == False: 
            break
        else:
            id1 += 1
    if id1 == len1: 
        return True
    else:
        return False


