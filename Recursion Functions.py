def Rtriangle(n):
    '''This function takes as input a number n and recursivly prints a right angle triangle'''
    if n < 1:
        return
    else:
        Rtriangle(n-1)
        print('*' * n)
        
def Rsilly(n):
    '''This function takes as input a number n, then recursivly returns n !'s and n ?'s '''
    if n == 0:
        return ''
    else:
       temp = Rsilly(n-1)
       answer = '!' + temp + '?'
       return answer

def Rcount(lst, n):
    '''Takes as input a list and a number and counts how many times that number appears in the list recursivly'''
    if lst == []:
        return 0
    else:
        temp = Rcount(lst[1:], n) #each has its own temp returned so must add them
        if lst[0] == n:
            temp += 1
        return temp

def Rfilter(lst, n):
    '''This function takes as input a list and a number n and returns a new list with every element except for n'''
    if lst == []:
        return []
    else:
        temp = Rfilter(lst[:-1],n)
        if lst[-1] != n: #if the first element is not equal to the input
            temp += [lst[-1]] #add a list of just that element to the end of temp
        return temp
        

def RdeleteEveryOther(lst):
    '''This function as input a list and returns another list with every other element from the orginal list'''
    if lst == []:
        return []
    else:
        temp = RdeleteEveryOther(lst[:-1])
        index = len(lst) - 1 #finde index by taking length minus 1
        if index % 2 ==  0: #check if index is an even position
            temp += [lst[-1]] #if so, add a list of just that element to the end of temp
            
       
        return temp
                
        
    
