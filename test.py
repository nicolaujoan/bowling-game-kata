from scoreCard import *

my_score_card = scoreCard('12345123451234512345')
joan_score_card = scoreCard('XXXXXXXXXXXX')
mateu_score_card = scoreCard('9-9-9-9-9-9-9-9-9-9-')
david_score_card = scoreCard('5/5/5/5/5/5/5/5/5/5/5')
otro = scoreCard('X63--9/5281XX1/X8/')


# just some pins bowled every time, works fine --> 60
my_score_card.processRolls()
print(my_score_card.getTotalScore())

# 9 and no pins bowled mix, works fine --> 90
mateu_score_card.processRolls()
print(mateu_score_card.getTotalScore())

### strikes case, needs to bee 300 instead of 210 (second forward score adding needed) --> 300
joan_score_card.processRolls()
print(joan_score_card.getTotalScore())

### spares case, works fine --> 150
david_score_card.processRolls()
print(david_score_card.getTotalScore())

### mixed case, needs to bee 140 instead of 127 (second forward score adding needed) --> 127
otro.processRolls()
print(otro.getTotalScore())
