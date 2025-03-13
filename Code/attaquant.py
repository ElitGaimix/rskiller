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
bot1.speedGoto((0.3,0,bot1.bot.pose[2]))
time.sleep(0.5)
bot = client.blue1  
# bot1.speedGoto((bot.pose[0],bot.pose[1],0))
start = perf_counter()
bot1.transfertToGallPosition()
end = perf_counter()
print("Temps de déplacement:",end - start)
bot.kick()
while True:
    pass