from random import *
import time
nteams = 32
w, h = nteams, nteams;
delay = 0.1
Teams = [[0 for x in range(2)] for y in range(h)]
Knockout = [[ 0 for x in range(2)] for y in range (8)]

Teams[0][0] = "Russia"
Teams[0][1] = 18
Teams[1][0] = "Saudi Arabia"
Teams[1][1] = 10
Teams[2][0] = "Uruguay"
Teams[2][1] = 54
Teams[3][0] = "Egypt"
Teams[3][1] = 42
Teams[4][0] = "Portugal"
Teams[4][1] = 57
Teams[5][0] = "Spain"
Teams[5][1] = 58
Teams[6][0] = "Morroco"
Teams[6][1] = 20
Teams[7][0] = "Iran"
Teams[7][1] = 8
Teams[8][0] = "France"
Teams[8][1] = 83
Teams[9][0] = "Peru"
Teams[9][1] = 34
Teams[10][0] = "Denmark"
Teams[10][1] = 42
Teams[11][0] = "Australia"
Teams[11][1] = 15
Teams[12][0] = "Argentina"
Teams[12][1] = 57
Teams[13][0] = "Iceland"
Teams[13][1] = 40
Teams[14][0] = "Croatia" 
Teams[14][1] = 45
Teams[15][0] = "Nigeria"
Teams[15][1] = 38
Teams[16][0] = "Brazil"
Teams[16][1] = 87
Teams[17][0] = "Switzerland"
Teams[17][1] = 40
Teams[18][0] = "Costa Rica"
Teams[18][1] = 38
Teams[19][0] = "Serbia"
Teams[19][1] = 33
Teams[20][0] = "Germany"
Teams[20][1] = 85
Teams[21][0] = "Mexico"
Teams[21][1] = 40
Teams[22][0] = "Sweden"
Teams[22][1] = 41
Teams[23][0] = "South Korea"
Teams[23][1] = 38
Teams[24][0] = "Belgium"
Teams[24][1] = 70
Teams[25][0] = "Panama"
Teams[25][1] = 35
Teams[26][0] = "Tunisia"
Teams[26][1] = 24
Teams[27][0] = "England"
Teams[27][1] = 65
Teams[28][0] = "Poland"
Teams[28][1] = 50
Teams[29][0] = "Colombia" 
Teams[29][1] = 60
Teams[30][0] = "Senegal"
Teams[30][1] = 45
Teams[31][0] = "Japan"
Teams[31][1] = 38






Points = [0 for x in range(w)]
GoalDiff = [0 for x in range(w)]

def PlayPenalties(a1,a2):
    # empty function
    winner = 0
    print(" play penalties")
    i =0
    pen1 =0
    pen2 =0
    Pendiff = 0
    while ( Pendiff < 1 or i < 5):
         pen1 = int(0.92+random()*Teams[a1][1]/100) +pen1
         pen2=  int(0.92+random()*Teams[a2][1]/100) +pen2
         Pendiff = abs(pen1-pen2)
         i =i +1
         time.sleep(delay) 
         print(pen1, pen2, i)
    if (pen1 > pen2):
        winner = a1
    else :
        winner = a2

    print ("Penalty score" ,Teams[a1][0], pen1, Teams[a2][0], pen2)
    return winner 


def PlayOneGame(t1, t2, pen):
    #play one game
    #this is the actual game
    winner = -1 
    score1 = int(6*random()*Teams[t1][1]/100)
    score2 = int(6*random()*Teams[t2][1]/100)
    if ( (score1 == score2) and (Teams[t2][1] -Teams[t1][1] >20) and (random() > 0.01) ):
        score1 =  int(6*random()*Teams[t1][1]/100)
    if ( (score1 > score2) and (Teams[t2][1] -Teams[t1][1] >20) and (random() > 0.01) ):
         a=score2
         score2=score1
         score2=a

    if (score1 > score2 ):
        winner = t1
    elif (score1 < score2): 
        winner = t2


    print(Teams[t1][0],"-",Teams[t2][0],score1,"-",score2,)
    
    if (score1  == score2 and pen == 1): winner =PlayPenalties(t1,t2)

    
 
    return score1, score2, winner

def playg(Teams, nteams, Points, start, pen):
    "Plays  games between teams"
    t1=start
    score1=-1
    score2=-1
    while(t1 < nteams+start):
        t2=t1+1
        while ( t2 < nteams+start): 
            score1, score2, winner = PlayOneGame(t1,t2,0)
            
            #if ( Teams[t1][0] == "Poland" ): score2 =score1+1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
            if (t1 != t2 ):
               # print(Teams[t1][0],"-",Teams[t2][0],score1,"-",score2,)

                if (score1 > score2 ):  Points[t1] =Points[t1]+3
                if (score2 > score1 ):  Points[t2] =Points[t2]+3
                if (score2 == score1 ):
                    Points[t2] = Points[t2]+1
                    Points[t1] = Points[t1]+1
                GoalDiff[t1] = score1 - score2 + GoalDiff[t1]
                GoalDiff[t2] = score2 - score1 + GoalDiff[t2]
                time.sleep(delay)
            t2  = t2 +1
        t1 = t1 + 1
    print ("Games finished!")
    print (Points)
    print(GoalDiff)

    i = start
    max = 0
    winner =0
    #for the winner 
    while (i < nteams+start):
        if (Points [i] > max or  (Points[i] == max and GoalDiff[i] > GoalDiff[winner]) ):
            winner = i
            max = Points[i]
        i = i +1  
    
    winnerscore = Points[winner]
    Points[winner] = -1; 
    #for the runner up
    i = start
    max = 0
    winner2 =0
    while (i < nteams+start):
        if (Points [i] > max or (Points[i] == max and GoalDiff[i] > GoalDiff[winner2]) ):
            winner2 = i
            max = Points[i]
        i = i +1
    print ("winner", Teams[winner][0])    
    print ("Runner-up", Teams[winner2][0])
    Points[winner]= winnerscore
    Knockout[int(start/4)][0] = winner
    Knockout[int(start/4)][1] = winner2
    return 




# group stage
g = 0
for g in range (8): playg(Teams, 4, Points, g*4, 1)


# knockout 16 stage
#  0-A, 1-B, 2-C 3-D, 4-E, 5-F, 6-G, 7-H
print (" knockout 16 stage" )
s1, s2, winnerA = PlayOneGame(Knockout[0][0], Knockout[1][1], 1)
s1, s2, winnerB = PlayOneGame(Knockout[2][0], Knockout[3][1], 1)
s1, s2, winnerC = PlayOneGame(Knockout[4][0], Knockout[5][1], 1)
s1, s2, winnerD = PlayOneGame(Knockout[6][0], Knockout[7][1], 1)
s1, s2, winnerE = PlayOneGame(Knockout[1][0], Knockout[0][1], 1)
s1, s2, winnerF = PlayOneGame(Knockout[3][0], Knockout[2][1], 1)
s1, s2, winnerG = PlayOneGame(Knockout[5][0], Knockout[4][1], 1)
s1, s2, winnerH = PlayOneGame(Knockout[7][0], Knockout[6][1], 1)



#  knockout 8 stage
print (" knockout 8 stage" )
s1, s2, winner1 = PlayOneGame(winnerA, winnerB, 1)
s1, s2, winner2 = PlayOneGame(winnerC, winnerD, 1)
s1, s2, winner3 = PlayOneGame(winnerE, winnerF ,1)
s1, s2, winner4 = PlayOneGame(winnerG, winnerH, 1)

print("knockout 4 stage")
s1, s2, winner1st = PlayOneGame(winner1, winner2, 1)
s1, s2, winner2nd = PlayOneGame(winner3, winner4,1)

print("final")
s1, s2, world_Champion = PlayOneGame(winner1st, winner2nd,1)






#while (g < 32):
#playg(Teams, 4, Points, g)
  #g =g +4

           
