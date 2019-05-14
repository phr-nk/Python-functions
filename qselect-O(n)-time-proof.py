import random

comp = 0
a=[]
b=[]
c=[]
d=[]
#create four random lists
for i in range(1000): 
        a.append(random.randint(1, 100))
for i in range(2000): 
        b.append(random.randint(1, 100)) 
for i in range(4000): 
        c.append(random.randint(1, 100))
for i in range(8000): 
        d.append(random.randint(1, 100))
#medians
mida = len(a)//2
midb = len(b)//2
midc = len(c)//2
midd = len(d)//2


def qselect(slist,k): #algorithm to find the median in  O(n) time
    global comp #global  variable for comparisons 
    v = random.choice(slist) #randomly pick v
    #create three sublists which will contain values less than, greater than, or equal to the random index
    lows = []
    equals = []
    highs = []
    for i in slist: #go through the input list and create three sublists 
        if i < v:
            comp +=1 #comparison
            lows.append(i)
        elif i > v:
            comp+=1 #comparison
            highs.append(i)
        else:
            equals.append(i)

    #median is in lows
    if k <= len(lows):
        comp += 1#comparison 
        return qselect(lows,k,)
        
    #median is in highs
    if k > len(slist) - len(highs):
        comp += 1#comparison
        return qselect(highs, k -(len(slist) - len(highs)))
    #median is found or equal to v
    else:
        return equals[0]

def runselect():
    global comp #global variable for comparisons
    complist = [] #create an empty comparison list
    #testing on size 1000
    for i in range(1000): #first test
         qselect(a, mida)#run the selection algorithm
         #print(comp)
         complist.append(comp) #append amount of comparisons for each test
         comp = 0 #reset amount of comparisons after each iteration
    print('length of input list:',len(a))   
    avg1 = sum(complist) / 1000 #find the average amount of comparisons 
    print('median of list a:', qselect(a, mida))
    print('average number of compares:', avg1)
    complist =[]
    for i in range(1000):
         qselect(b, midb)
         complist.append(comp)
         comp = 0
         
    print('length of input list:',len(b))
    avg2 = sum(complist) / 1000    
    print('median of list b:', qselect(b, midb))
    print('average number of compares:', avg2)
    complist =[]
    for i in range(1000):
         qselect(c, midc)
         complist.append(comp)
         comp = 0
    print('length of input list:',len(c))
    avg3 = sum(complist) / 1000    
    print('median of list c:', qselect(c, midc))
    print('average number of compares:', avg3)
    
    complist =[]
    for i in range(1000):
         qselect(d, midd)
         complist.append(comp)
         comp = 0
         
    print('length of input list', len(d))
    avg4 = sum(complist) / 1000    
    print('median of list d:', qselect(d, midd))
    print('average number of compares:', avg4)
    
    
