class scoreCard():

    ### GLOBALS ###
    STRIKE = 'X'
    SPARE = '/'
    NO_PINS_BOWLED = '-'
    BOWLING_SYMBOLS = ['X', '/', '-']
    LAST_FRAME_ROLL = 19

    ### CONSTRUCTOR ###
    def __init__(self, score_sheet='') -> None:
        self.score_sheet = score_sheet  
        self.number_of_roll = 1
        self.current_roll_score = ''
        self.previous_roll_score = ''
        self.total_score = 0
        self.is_last_frame = False

    ### SCORE SHEET GETTER AND SETTER ###
    def getScoreSheet(self):
        return self.score_sheet
    
    def setScoreSheet(self, score_sheet):
        self.score_sheet = score_sheet
    
    ### USEFUL GETTERS ###
    def getCurrentRollScore(self):
        return self.current_roll_score
    
    def getPreviousRollScore(self):
        return self.previous_roll_score
    
    def getTotalScore(self):
        return self.total_score

     ### PLAYS (jugadas) ###
    def isStrike(self):
        return self.getCurrentRollScore() is self.STRIKE
    
    def isSpare(self):
        return self.getCurrentRollScore() is self.SPARE
    
    def noPinsBowled(self):
        return self.getCurrentRollScore() is self.NO_PINS_BOWLED
    
    def pinsBowled(self):
        return self.getCurrentRollScore().isnumeric()
    
    ### SCORE CALCULATION ### 
    def incrementTotalScore(self, increment):
        self.total_score += increment

    def sumStrikeScore(self):
        self.incrementTotalScore(10)
        
    def sumNormalScore(self):
        self.incrementTotalScore(int(self.getCurrentRollScore()))
    
    def sumSpareScore(self):
         self.incrementTotalScore(int(self.getPreviousRollScore()))
    
        