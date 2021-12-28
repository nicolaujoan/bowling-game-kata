from scoreCard import *

my_score_card = scoreCard('12345123451234512345')
joan_score_card = scoreCard('XXXXXXXXXXXX')
mateu_score_card = scoreCard('9-9-9-9-9-9-9-9-9-9-')
david_score_card = scoreCard('5/5/5/5/5/5/5/5/5/5/5')
mixed1 = scoreCard('X63--9/5281XX1/X8/')
mixed2 = scoreCard('81-92/X637-52X-62/X')
mixed3 = scoreCard('2345XX-98/-/18/251')
mixed4 = scoreCard('2345XX-98/-/187251')
mixed5 = scoreCard('-2XXX16427/634/XX6')


# just some pins bowled every time, works fine --> 60
my_score_card.processRolls()
print(my_score_card.getTotalScore())

# 9 and no pins bowled mix, works fine --> 90
mateu_score_card.processRolls()
print(mateu_score_card.getTotalScore())

### strikes case, works fine --> 300
joan_score_card.processRolls()
print(joan_score_card.getTotalScore())

### spares case, works fine --> 150
david_score_card.processRolls()
print(david_score_card.getTotalScore())

### mixed case, works fine --> 140
mixed1.processRolls()
print(mixed1.getTotalScore())

### other mixed case, needs to be --> 122
mixed2.processRolls()
print(mixed2.getTotalScore())

# it fails (needs to be debugged)
### other mmixed case, needs to be --> 107
# mixed3.processRolls()
# print(mixed3.getTotalScore())

# it seems it has the same bug
### other mixed case, needs to be --> 158
# mixed4.processRolls()
# print(mixed4.getTotalScore())

### other mixed case, needs to be --> 154
# works fine
mixed5.processRolls()
print(mixed5.getTotalScore())






