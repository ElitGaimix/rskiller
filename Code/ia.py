import math
import rsk
from rsk import constants
GREEN = -1
BLUE = 1
BallRayon = 0.1

class ia:
    
    def __init__(self,client : rsk.Client,bot : rsk.client.ClientRobot,team : int):
        self.client = client
        self.bot = bot
        self.team = team
        
    def transfertToGallPosition(self):
        client = self.client
        bot = self.bot
        # Au cas ou le bot veux tirer dans sont camp lmao
        if self.team == BLUE:
            goal = self.getGoal(-self.team)
            ballprediction = self.predictBall() # On récupe ou va allez la balle si le mec tire mtn et si
                                                # elle va dans le but on place le bot et tire
            if(ballprediction[1] < 0.25 and ballprediction[1] > -0.25) and goal[0] != ballprediction[0]:
                angle = self.angleBetween(bot.pose,client.ball)
                bot.goto((client.ball[0] - BallRayon,bot.pose[1],angle), wait=True)
                return
            # Si le robot est du mauvais coté pour tirer
            if client.ball[0] < bot.pose[0]:
                # Le robot doit forcement passer derriere la balle dcp on check sa au cas ou la balle est sur 
                # sont chemin
                if bot.pose[1] < client.ball[1] + 0.15 and bot.pose[1] > client.ball[1] - 0.15:
                    # self.speedGoto((bot.pose[0],client.ball[1] + 0.36,bot.pose[2]))
                    self.goto((bot.pose[0],client.ball[1] + 0.36,bot.pose[2]),0,0.2)
                self.goto((client.ball[0] - 0.3,bot.pose[1],bot.pose[2]),0.2,0)
            # Check si le robot est au dessus ou en dessous de la balle car des truc sont pas les meme
            if client.ball[1] < bot.pose[1]:
                nAngle = self.angleBetween(client.ball, (goal[0],-0.25))
                # On calcul la position minimum pour que quand le robot tire bah sa soit dans le but
                # Pour sa on estime que la balle doit etre au moin en -0.25, on fait en suite un petit triangle
                #rectangle qui vient pointer sur la position du robot
                botgo = [client.ball[0] - BallRayon,
                     -0.25 - ((goal[0] - client.ball[0]) * math.tan(nAngle)),
                    nAngle + (math.pi/2) + (math.pi/3)]
            else:
                # meme chose mais l'angle change et on cherche pour en haut du but
                nAngle = self.angleBetween(client.ball, (goal[0],0.25))
                botgo = [client.ball[0] - BallRayon,
                     0.25 - ((goal[0] - client.ball[0]) * math.tan(nAngle)),
                    nAngle + (math.pi/2) + (2*math.pi/3)]
            bot.goto((botgo[0],botgo[1],botgo[2]), wait=True)
        else:
            # Meme chose qu'au dessus sauf que on doit faire des addition ou d'autre truc a la con
            # Comme c'est pas le meme coté
            goal = self.getGoal(-self.team)
            ballprediction = self.predictBall()
            if(ballprediction[1] < 0.25 and ballprediction[1] > -0.25) and goal[0] != ballprediction[0]:
                angle = self.angleBetween(bot.pose,client.ball)
                bot.goto((client.ball[0] + BallRayon,bot.pose[1],angle), wait=True)
                return
            if client.ball[0] > bot.pose[0]:
                if bot.pose[1] < client.ball[1] + 0.15 and bot.pose[1] > client.ball[1] - 0.15:
                    bot.goto((bot.pose[0],client.ball[1] + 0.16,bot.pose[2]),wait=True)  
                bot.goto((client.ball[0] + 0.20,bot.pose[1],bot.pose[2]),wait=True)
            if client.ball[1] < bot.pose[1]:
                nAngle = self.angleBetween(client.ball, (goal[0],-0.25))
                botgo = [client.ball[0] + BallRayon,
                     -0.25 - ((goal[0] - client.ball[0]) * math.tan(nAngle)),
                    nAngle + (math.pi/2) + (2*(math.pi/3))]
            else:
                nAngle = self.angleBetween(client.ball, (goal[0],0.25))
                botgo = [client.ball[0] + BallRayon,
                     0.25 - ((goal[0] - client.ball[0]) * math.tan(nAngle)),
                    nAngle + (math.pi/2) + (math.pi/3)]
            bot.goto((botgo[0],botgo[1],botgo[2]), wait=True)
        
    def getGoal(self, team : int):
        return constants.field_length * team / 2,0
    
    def predictBall(self):
        client = self.client
        bot = self.bot
        ballprediction = []
        if client.ball[0] > bot.pose[0]:  # Zone gauche de la balle
            goalPosition = (constants.field_length * 1 / 2,0)
            ballprediction.append(goalPosition[0])
            # Calcul de la distance en y qui sépare le robot et la ou la balle va arriver (On chercher l'adjacent avec 
            # l'opposé et l'angle => adjacant = opposé * tan(angle))
            angle = self.angleBetween(bot.pose,client.ball)
            ballprediction.append((goalPosition[0] - bot.pose[0]) * math.tan(angle))
        else: # Zone droite/millieu 
            goalPosition = (constants.field_length * -1 / 2,0)
            ballprediction.append(goalPosition[0])
            # Meme chose qu'au dessus sauf que ici l'angle doit changer de repère dcp on fait un truc avec pi quoi
            angle = self.angleBetween(client.ball,bot.pose)
            ballprediction.append((bot.pose[0] - goalPosition[0]) * math.tan(math.pi - angle))
        return ballprediction
    
    def goto(self,target,ximprecision : int,yimprecision : int):
        bot = self.bot
        bot.goto(target,wait=True)
        # while abs(bot.pose[0] - target[0]) >= ximprecision and abs(bot.pose[1] - target[1]) >= yimprecision:
        #     bot.goto(target,wait=False)
        # bot.control(0,0,0)
        # print("stop")
        
    def speedGoto(self,target):
        pass
        
    
    def angleBetween(self,p1,p2):
        y = p2[1] - p1[1]
        x = p2[0] - p1[0]
        return math.atan2(y, x)