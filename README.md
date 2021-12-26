# bowling-game-kata

**Program** :

given a valid sequence of rolls for one line of American Ten-pin Bowling, produces the total
score for the game.

**Rules of the game (summary)** :

1) Each game or “line” has 10 turns or frames for the bowler.

2) In each frame, the bowler gets up to two tries to knock down all the pins.

3) If in two tries, he fails to knock them all down, his score for that frame is the total number of
pins knocked down in his two tries.

4) If in two tries, he knocks them all down, this is called a “spare” and his score for the frame si
ten plus the number of pins knocked down on his next throw (next turn).

5) If on his first try in the frame he knocks down all the pins, this is called a “strike”. His turn is
over, and his score for the frame is ten plus the simple total of the pins knocked down
in his next two rolls.

6) If he get a spare or strike in the last (tenth) frame, the bowler gets to throw one or two
more bonus balls respectively. These bonus throw one or two more bonus balls
respectively. These bonus throws are taken as part of the same turn. If the bonus
throws knock down all the pins, the process does not repeat.

7) The bonus throws are only used to calculate the score of the final frame.

What the program doesn’t do:

- Check for valid rolls
- Check for correct numbers of rolls and frames
- Provide score for intermediate frame


Practising how to obtain the score:

![score sheet](Scoring%20bowling%20practice%20sheets.jpg)

Second score sheet: 5 + 9 + 20 + 19 + 9 + 10 + 11 + 9 + 9 + 6 = 107 points

Third score sheet: 9 + 17 + 7 + 18 + 9 + 9 + 30 + 26 + 20 + 13 = 158 points

Fourth score sheet: 19 + 9 + 0 + 15 + 7 + 9 + 21 + 20 + 20 + 20 = 140 points

Fifth score sheet: 2 + 30 + 21 + 17 + 7 + 6 + 16 + 9 + 20 + 26 = 154 points


