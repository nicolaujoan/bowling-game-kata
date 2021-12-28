from scoreCard import *

my_score_card = scoreCard('12345123451234512345')
joan_score_card = scoreCard('XXXXXXXXXXXX') # 12 strikes is a “Thanksgiving Turkey”
mateu_score_card = scoreCard('9-9-9-9-9-9-9-9-9-9-')
david_score_card = scoreCard('5/5/5/5/5/5/5/5/5/5/5')
mixed1 = scoreCard('X63--9/5281XX1/X8/')
mixed2 = scoreCard('81-92/X637-52X-62/X')
mixed3 = scoreCard('2345XX-98/-/187251')  
mixed4 = scoreCard('18X7-2/819-XXX6/3')
mixed5 = scoreCard('-2XXX16427/634/XX6')
test1 = scoreCard('X9-9-9-9-9-9-9-9-9-')
test2 = scoreCard('9-9-9-9-9-9-9-9-9-X9-') # two extra final rolls
test3 = scoreCard('X9-X9-9-9-9-9-9-9-')
test4 = scoreCard('XX9-9-9-9-9-9-9-9-') # two strikes in a row is a double
test5 = scoreCard('XXX9-9-9-9-9-9-9-') # three strikes in a row is a triple
test6 = scoreCard('9-9-9-9-9-9-9-9-9-XXX') # two strikes in extra rolls
test7 = scoreCard('8/549-XX5/53639/9/X') # spare in extra roll
test8 = scoreCard('X5/X5/XX5/--5/X5/') # spare in extra roll


my_score_card.processRolls()
assert my_score_card.getTotalScore() == 60

mateu_score_card.processRolls()
assert mateu_score_card.getTotalScore() == 90

joan_score_card.processRolls()
assert joan_score_card.getTotalScore() == 300

david_score_card.processRolls()
assert david_score_card.getTotalScore() == 150

mixed1.processRolls()
assert mixed1.getTotalScore() == 140

mixed2.processRolls()
assert mixed2.getTotalScore() == 122

mixed3.processRolls()
assert mixed3.getTotalScore() == 107

mixed4.processRolls()
assert mixed4.getTotalScore() == 158

mixed5.processRolls()
assert mixed5.getTotalScore() == 154

test1.processRolls()
assert test1.getTotalScore() == 100

test2.processRolls()
assert test2.getTotalScore() == 100

test3.processRolls()
assert test3.getTotalScore() == 110

test4.processRolls()
assert test4.getTotalScore() == 120

test5.processRolls()
assert test5.getTotalScore() == 141

test6.processRolls()
assert test6.getTotalScore() == 111

test7.processRolls()
assert test7.getTotalScore() == 149

test8.processRolls()
assert test8.getTotalScore() == 175


















