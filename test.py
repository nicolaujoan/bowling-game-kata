from scoreCard import *

my_score_card = scoreCard('12345123451234512345')
joan_score_card = scoreCard('XXXXXXXXXXXX')
mateu_score_card = scoreCard('9-9-9-9-9-9-9-9-9-9-')
david_score_card = scoreCard('5/5/5/5/5/5/5/5/5/5/5')
otro = scoreCard('81-92/X637-52X-62/X')

# furula
my_score_card.processRolls()
print(my_score_card.getTotalScore())

# furula
mateu_score_card.processRolls()
print(mateu_score_card.getTotalScore())

# furula
david_score_card.processRolls()
print(david_score_card.getTotalScore())

# furula
joan_score_card.processRolls()
print(joan_score_card.getTotalScore())

# peta (needs to be debugged too)
# otro.processRolls()
# print(otro.getTotalScore())
