import numpy as np
import ia
import math
import rsk
from rsk import constants
GREEN = -1
BLUE = 1
TEAM = BLUE
# dcx§/PID54°B
# Créé un client Robot Soccer Kit, qui permettra
# de communiquer avec le simulateur de soccer
client = rsk.Client()
# Boucle infinie
bot1 = ia.ia(client, client.blue1,TEAM)
bot2 = ia.ia(client, client.blue2,TEAM)
bot = client.blue1  
bot1.transfertToGallPosition()
bot.kick()
while True:
#     bot1.transfertToGallPosition();
    pass
    