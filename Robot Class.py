class robot():
    def __init__(self,x = 0,y = 0,char = 'U'):
        '''Constructor that initializes the objects variables'''
        self.xpos = x
        self.ypos = y
        self.direction = char.upper()
    def __str__(self):
        '''Returns the string version of the robot'''
        return '({}, {}):{}'.format(self.xpos,self.ypos,self.direction)
    def turnLeft(self):
        '''Turns the robot object left from where it is orginally facing'''
        if self.direction == 'U':
            self.direction = 'L'
        elif self.direction == 'L':
            self.direction = 'D'
        elif self.direction == 'D':
            self.direction = 'R'
        else:
            self.direction = 'U'
        
    def turnRight(self):
        '''Turns the robot right from where it was orginally facing'''
        if self.direction == 'U':
            self.direction = 'R'
        elif self.direction == 'R':
            self.direction = 'D'
        elif self.direction == 'D':
            self.direction = 'L'
        else:
            self.direction = 'U'
    def advance(self):
        '''Advances the robot 1 spot either on the x or y axis depending on which way it is facing'''
        if self.direction == 'U':
            self.ypos += 1
        elif self.direction == 'L':
            self.xpos -= 1
        elif self.direction == 'D':
            self.ypos -= 1
        elif self.direction == 'R':
            self.xpos += 1
    def getPosition(self):
        '''gets and returns the postition of where the robot is located'''
        return self.xpos, self.ypos
    def getFacing(self):
        '''Gets and returns the direction of which way the robot is facing'''
        return self.direction
    def runProgram(self, seq):
        '''Goes through the input sequence and does the corresponding function calls'''
        for letter in seq:
            if letter.upper() == 'A':
                self.advance()
            elif letter.upper() == 'R':
                self.turnRight()
            elif letter.upper() == 'L':
                self.turnLeft()
        
    
