class scoreCard():

    ### GLOBALS ###
    STRIKE = 'X'
    SPARE = '/'
    NO_PINS_BOWLED = '-'
    BOWLING_SYMBOLS = ['X', '/', '-']
    LAST_FRAME_ROLL = 19
    TOTAL_ROLLS = 20

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
    
    def getCurrentRollNumber(self):
        return self.number_of_roll
    
    ### USEFUL SETTERS ###
    def setCurrentRollScore(self, roll_score):
        self.current_roll_score = roll_score
    
    def setPreviousRollScore(self, prev_roll_score):
        self.previous_roll_score = prev_roll_score

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
        self.total_score += int(increment)

    def sumStrikeScore(self):
        self.incrementTotalScore(10)
        
    def sumNormalScore(self):
        self.incrementTotalScore(int(self.getCurrentRollScore()))
    
    def sumSpareScore(self):
         self.incrementTotalScore(10 - int(self.getPreviousRollScore()))
    
    ### ROLL NUMBER METHODS ###
    def incrementRollNumber(self, increment):
        self.number_of_roll += increment
    
    ### LAST FRAME METHODS ### 
    def lastFrameOn(self):
        self.is_last_frame = True
    
    def isLastFrame(self):
        return self.is_last_frame
    
    ### MOVE FORWARD METHODS (for strike and spare plays) ###
    def getFollowingScore(self, score_sheet, roll_number, displacement):
        score_sheet = self.getScoreSheet()
        # roll_number = self.getCurrentRollNumber()
        return score_sheet[roll_number + displacement]
    
    ### future score evaluations ###
    def sumSpareScoreFuture(self):
        self.incrementTotalScore(10 - int(self.getCurrentRollScore()))

    def processFutureScore(self, score):
        if score is self.STRIKE:
            self.sumStrikeScore()
        elif score is self.SPARE:
            self.sumSpareScoreFuture()
        elif score.isnumerical():
            self.sumNormalScore()
        else: pass

    ### PROCESS ROLLS METHOD (main logic) ###
    def processRolls(self):

        # reference to the score sheet
        score_sheet = self.getScoreSheet()
        
        # loop through every roll of the score sheet
        for roll, score in enumerate(score_sheet):

            # actual roll score
            self.setCurrentRollScore(score)
            
            # not in last frame
            if not self.isLastFrame():

                # strike case
                if self.isStrike():
                    # get score
                    self.sumStrikeScore()
                    # get and increment following scores
                    first_following_score = self.getFollowingScore(score_sheet, roll, 1)
                    second_following_score = self.getFollowingScore(score_sheet, roll, 2)
                    self.processFutureScore(first_following_score)
                    self.processFutureScore(second_following_score)
                    # self.incrementTotalScore(first_following_score)
                    # self.incrementTotalScore(second_following_score)
                    # increment roll
                    self.incrementRollNumber(2)
                
                # spare case
                elif self.isSpare():
                    # get score
                    self.sumSpareScore()
                    self.incrementTotalScore(self.getFollowingScore(score_sheet, roll, 1))
                    # increment roll
                    self.incrementRollNumber(1)
                
                # some pins bowled case
                elif self.pinsBowled():
                    # get score
                    self.sumNormalScore()
                    # increment roll
                    self.incrementRollNumber(1)
                
                # no pins bowled case
                elif self.noPinsBowled():
                    # just increment roll, no score is added
                    self.incrementRollNumber(1)
                
                else: continue

            # last frame rolls 
            else:
                # strike case
                if self.isStrike():
                    self.sumStrikeScore()
                    self.incrementRollNumber(1)
                
                elif self.isSpare():
                    self.sumSpareScore()
                    self.incrementRollNumber(1)
                
                elif self.pinsBowled():
                    self.sumNormalScore()
                    self.incrementRollNumber(1)
            
            # select the previous roll score, useful for the next roll in case of "spare"
            self.setPreviousRollScore(self.getCurrentRollScore())
            
            # check if we are in the last roll
            if self.getCurrentRollNumber() == self.LAST_FRAME_ROLL:
                self.lastFrameOn()






    