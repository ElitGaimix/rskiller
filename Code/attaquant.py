import numpy as np
import ia
import math
import rsk
from rsk import constants
from time import perf_counter
GREEN = -1
BLUE = 1
TEAM = BLUE
client = rsk.Client()
bot1 = ia.ia(client, client.blue1,TEAM)
bot2 = ia.ia(client, client.blue2,TEAM)
bot = client.blue1  
# bot1.goto((client.ball[0],client.ball[1],bot.pose[2]),0.1)
start = perf_counter()
bot1.transfertToGallPosition()
end = perf_counter()
print("Temps de déplacement:",end - start)
bot.kick()
while True:
    pass