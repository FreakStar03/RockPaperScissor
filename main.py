"""
    Rock, Paper, Scissors In this assignment game of Rock, Paper, Scissors
    is to be designed with single player against computer. Students should 
    use the random function here. Player make a move first
    and then the program makes one.
    To indicate the move, Player can either use a single alphabet 
    or input an entire string. 
    A function will have to be set up to check the validity of the move. 
    Using another function, the winner of that round is decided. 
    Player can then either give an option of playing again or 
    decide a pre-determined number of moves in advance. 
    A scorekeeping function will also have to be created which will return 
    the winner at the end. To maintain scoreboard use the concept of pickling
    from OOP for storing the results of last game.
"""

import random
import pickle

class RockPaperScissors:
    # store score or current match
    score = 0

    def __init__(self):
        # calls start with pickle file 
        f=open("data.dat","wb")
        self.start(f)

    def start(self, f):
        # start method that run a complete round of match
        print(" Number of Turns to play: ")
        turn = int(input("Value: ")) #store number of turns
        i = 0 #for loop in while

        while i<turn:
            print("Choose Rock, Paper or Scissor (Enter Initial Alphabet or Enter Whole String):")
            print(" 1] (r) Rock \n 2] (p) Paper \n 3] (s) Scissor \n 4] Exit")

            #catch non int inputs
            try:
                norm = input("Value: ").lower()
            except ValueError:
                print("Valid number, please")
                continue

            if(turn == 0):break #if number of turn enter by user is 0
            if(norm == 'r' or norm =='rock'):
                norm = "Rock" #for rock
            elif(norm == 'p' or norm =='paper'):
                norm = "Paper" #for paper
            elif(norm == 's' or norm =='scissor'):
                norm = "Scissor"  #for scissor
            elif(norm == 'e' or norm == 'exit'):break
            else: #for else
                print(" Wrong Input, Check Value ")
                continue
            i += 1 #iterate loop
            self.Validity(norm)
        
        print("Game Ended")
        score  = self.score
        #run winnner which returns same score to store in pickle
        s = self.Winner(score, turn)
        pickle.dump(s,f)

        # Re Run the Game

        while(True):
            print("Play Again (Y/N)")
            ans = input("Y/N: ").lower()

            if ans =='y':
                self.start(f)
                break
            elif ans =='n':
                f.close()
                self.AllMatchTotal()
                print("Exiting....")
                break
            else:print("Re-check value")

    def Validity(self, norm):
        # randomly select computer value from array and check with user value
        OptionArray = ["Rock", "Paper", "Scissor"]
        RC = random.choice(OptionArray)
        print("Computer Selects %s and Player Selects %s"  % (RC, norm))
        if RC == norm:
            print("Right Answer")
            self.score += 1 # inc score
        else:
            print("Wrong Answer")

    def Winner(self, score, noOfmatch):
        print("Final Score:  Total Score in %d matches is %d !"  % ( noOfmatch , score))
        return [int(noOfmatch), int(score)]

    def AllMatchTotal(self):
        with open("data.dat","rb") as f:
            unpickled = []
            while True:
                try:
                    unpickled.append(pickle.load(f))
                except EOFError:
                    break
            f.close()
            unpickled.sort(reverse=True)
            print("----------Scoreboard (Decreasing Order)----------")
        for val in unpickled:
            print("Score in %d matches is %d !"  % (val[0] ,  val[1]) )

if __name__ == '__main__':
    RockPaperScissors()

