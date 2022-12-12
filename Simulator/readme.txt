Baseball Simulator is a Python command-line program that simulates a complete 
baseball game.

Run Main.py for-

The user is prompted to choose any two MLB teams, and the year for each team. 
The program then scrapes player data from baseball-reference.com.

The program attempts to be as accurate as possible to real-world outcomes. 
Data from the following sources was used to refine the algorithms that 
determine results:

https://www.baseball-reference.com/leagues/MLB/bat.shtml
https://www.baseball-fever.com/forum/general-baseball/statistics-analysis-sabermetrics/81427-pitch-outcome-distribution-over-25-years
https://www.baseballprospectus.com/news/article/8936/prospectus-idol-entry-grounding-home-run-hitters/

For each at-bat, the program takes into account the batter's batting average, 
the pitcher's earned run average, and the pitcher's pitch count to determine 
whether the batter or pitcher has an edge, and how big of an edge. A player 
with an edge over the other will be more likely to have a positive result for 
each pitch, and that likelihood increases with larger edge percentages.

At the end of each game, the program will output a box score, and give the 
user the option to save the box score to a .txt file.


Run Main-looped.py for-
Our modified version which allows the user to run the simulation any number of times.
It also provides win probability of each team along with the actual win-probability acraped from www.baseball-reference.com
Note- If the code does not complete execution in 5 minutes, run it again. The program goes into an infinite loop due to an error in the new loop we implemented that we haven/t figured out yet. Please run the code again until a result is obtained.
