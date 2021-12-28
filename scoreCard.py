class scoreCard():

    ### GLOBALS ###
    STRIKE = 'X'
    SPARE = '/'
    NO_PINS_BOWLED = '-'
    LAST_FRAME_ROLL = 19


    ### CONSTRUCTOR ###
    def __init__(self, score_sheet='') -> None:
        self.score_sheet = score_sheet  
        self.number_of_roll = 1
        self.previous_score = ''
        self.total_score = 0
        self.is_last_frame = False

    
    ### scoresheet ###
    def getScoreSheet(self):
        return self.score_sheet

    
    def setScoreSheet(self, score_sheet):
        self.score_sheet = score_sheet

    
    ### total score getter ###
    def getTotalScore(self):
        return self.total_score

    
    ### current roll number getter ###
    def getCurrentRollNumber(self):
        return self.number_of_roll

    
    ### previous score getter and setter ###
    def getPreviousScore(self):
        return self.previous_score
    

    def setPreviousScore(self, score):
        self.previous_score = score
    

    ### SCORE CALCULATION ###
    def incrementTotalScore(self, increment):
        self.total_score += increment


    def sumStrikeScore(self):
        self.incrementTotalScore(10)


    def sumSpareScore(self, previous_score):
        if previous_score.isnumeric():
            self.incrementTotalScore(10 - int(previous_score))
        else:
            self.incrementTotalScore(10)
        

    def sumNormalScore(self, score):
        self.incrementTotalScore(int(score))
    

    ### roll number acumulator ###
    def incrementRollNumber(self, increment):
        self.number_of_roll += increment

    
    ### PLAYS (jugadas) ###
    def isStrike(self, score):
        return score is self.STRIKE
            
    
    def isSpare(self, score):
        return score is self.SPARE
            
    
    def pinsBowled(self, score):
        return score.isnumeric()
    

    def noPinsBowled(self, score):
        return score is self.NO_PINS_BOWLED

    
    # lógica cuando se da el caso de un "STRIKE" (todavía no estamos en el último frame)
    def processStrike(self, score_sheet, roll):
        
        # strike score addition
        self.sumStrikeScore()

        # first forward case
        first_forward_score = self.get_forward_score(score_sheet, roll, 1)
        
        if self.pinsBowled(first_forward_score):
            self.sumNormalScore(first_forward_score)

        elif self.isStrike(first_forward_score):
            self.sumStrikeScore()

        else: pass

        # second forward case:
        second_forward_score = self.get_forward_score(score_sheet, roll, 2)

        if self.pinsBowled(second_forward_score):
            self.sumNormalScore(second_forward_score)
        
        elif self.isStrike(second_forward_score):
            self.sumStrikeScore()
        
        elif self.isSpare(second_forward_score):
            self.sumSpareScore(first_forward_score)
        
        else: pass
                
    # lógica cuando se da el caso de un "SPARE" (todavía no estamos en el último frame) 
    def processSpare(self, score_sheet, roll):
        
        # sum actual score
        self.sumSpareScore(self.getPreviousScore())

        # take forward score:
        forward_score = self.get_forward_score(score_sheet, roll, 1)

        # evaluate forward score (strike, pins bowled or not pins bowled)
        if self.pinsBowled(forward_score):
            self.sumNormalScore(forward_score)
        
        elif self.isStrike(forward_score):
            self.sumStrikeScore()
        
        else: pass
    

    # procesa las jugadas hechas en el último "frame"
    def processPlayInLastFrame(self, score):
        if self.isStrike(score):
            self.sumStrikeScore()

        elif self.isSpare(score):
            self.sumSpareScore(self.getPreviousScore())

        elif self.pinsBowled(score):
            self.sumNormalScore(score)
        
        else: self.incrementRollNumber(1)

    
    ### check if we are on last frame ###
    def isLastFrame(self):
        return self.getCurrentRollNumber() >= self.LAST_FRAME_ROLL
    

    ### get forward score method (obtiene las puntuaciones próximas) ###
    def get_forward_score(self, score_sheet, roll, increment):
        return score_sheet[roll + increment]


    ### main logic (procesa todas las tiradas "rolls" teniendo en cuenta si estamos o no en el último frame) ###
    def processRolls(self):
        score_sheet = self.getScoreSheet()
        
        for roll, score in enumerate(score_sheet):
            
            if not self.isLastFrame():
                    if self.isStrike(score): 
                        self.processStrike(score_sheet, roll)
                        self.incrementRollNumber(2)

                    elif self.isSpare(score): 
                        self.processSpare(score_sheet, roll)
                        self.incrementRollNumber(1)

                    elif self.pinsBowled(score): 
                        self.sumNormalScore(score)
                        self.incrementRollNumber(1)

                    else:
                        self.incrementRollNumber(1)
            
            else:
                self.processPlayInLastFrame(score)
            
            self.setPreviousScore(score)
            
            


            
    

    