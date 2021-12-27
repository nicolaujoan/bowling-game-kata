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
        self.current_roll_score = score_sheet[0]
        self.previous_roll_score = ''
        self.total_score = 0
        self.is_last_frame = False

    ### SCORE SHEET GETTER AND SETTER ###
    def getScoreSheet(self):
        return self.score_sheet
    
    def setScoreSheet(self, score_sheet):
        self.score_sheet = score_sheet
    

        