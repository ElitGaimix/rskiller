import numpy as np
import ia
import math
import rsk
from rsk import constants
from time import perf_counter
import time
GREEN = -1
BLUE = 1
TEAM = BLUE
client = rsk.Client()
bot1 = ia.ia(client, client.blue1,TEAM)
bot2 = ia.ia(client, client.blue2,TEAM)
# # bot1.speedGoto((-0.15,0.1,bot1.bot.pose[2]))
# bot = client.blue1  
# # bot.goto((-0.15,0.1,bot1.bot.pose[2] + math.pi/2),wait=True)
# bot.goto((0.3,0,bot1.bot.pose[2]),wait=True)
# time.sleep(0.5)
# start = perf_counter()
# bot1.transfertToGallPosition()
# end = perf_counter()
# print("Temps de déplacement:",end - start)
# bot.kick()
# bot1.calibrateBall()

while True:
    pass