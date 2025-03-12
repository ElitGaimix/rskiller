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
        if self.team == BLUE:
            goal = self.getGoal(-self.team)
            ballprediction = self.predictBall()
            if(ballprediction[1] < 0.25 and ballprediction[1] > -0.25) and goal[0] != ballprediction[0]:
                angle = self.angleBetween(bot.pose,client.ball)
                bot.goto((client.ball[0] - BallRayon,bot.pose[1],angle), wait=True)
                return
            if client.ball[0] < bot.pose[0]:
                if bot.pose[1] < client.ball[1] + 0.15 and bot.pose[1] > client.ball[1] - 0.15:
                    bot.goto((bot.pose[0],client.ball[1] + 0.16,bot.pose[2]),wait=True)
                bot.goto((client.ball[0] - 0.20,bot.pose[1],bot.pose[2]),wait=True)
            if client.ball[1] < bot.pose[1]:
                nAngle = self.angleBetween(client.ball, (goal[0],-0.25))
                botgo = [client.ball[0] - BallRayon,
                     -0.25 - ((goal[0] - client.ball[0]) * math.tan(nAngle)),
                    nAngle + (math.pi/2) + (math.pi/3)]
            else:
                nAngle = self.angleBetween(client.ball, (goal[0],0.25))
                botgo = [client.ball[0] - BallRayon,
                     0.25 - ((goal[0] - client.ball[0]) * math.tan(nAngle)),
                    nAngle + (math.pi/2) + (2*math.pi/3)]
            bot.goto((botgo[0],botgo[1],botgo[2]), wait=True)
        else:
            goal = self.getGoal(-self.team)
            ballprediction = self.predictBall()
            if(ballprediction[1] < 0.25 and ballprediction[1] > -0.25):
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
        if client.ball[0] > bot.pose[0]:  
            goalPosition = (constants.field_length * 1 / 2,0)
            ballprediction.append(goalPosition[0])
            angle = self.angleBetween(bot.pose,client.ball)
            ballprediction.append((goalPosition[0] - bot.pose[0]) * math.tan(angle))
        else:
            goalPosition = (constants.field_length * -1 / 2,0)
            ballprediction.append(goalPosition[0])
            angle = self.angleBetween(client.ball,bot.pose)
            ballprediction.append((bot.pose[0] - goalPosition[0]) * math.tan(math.pi - angle))
        return ballprediction
    
    def goto(self,target,imprecision : int):
        bot = self.bot
        max1 = max(bot.pose[0],target[0])
        min1 = min(bot.pose[0],target[0])
        max2 = max(bot.pose[1],target[1])
        min2 = min(bot.pose[1],target[1])
            
        
    def angleBetween(self,p1,p2):
        y = p2[1] - p1[1]
        x = p2[0] - p1[0]
        return math.atan2(y, x)
        