import numpy as np
import ia
import math
import rsk
from rsk import constants
from time import perf_counter
import time
GREEN = -1
BLUE = 1
TEAM = GREEN
client = rsk.Client()
bot1 = ia.ia(client, client.green1,TEAM)
bot2 = ia.ia(client, client.blue1,BLUE)

while True:
    ballprediction = bot2.predictBall()
    goal = bot1.getGoal(TEAM)
    if goal[0] != ballprediction[0] and (ballprediction[1] < 0.3 and ballprediction[1] > -0.3):
        bot1.bot.goto((ballprediction[0],ballprediction[1],0),wait=True)