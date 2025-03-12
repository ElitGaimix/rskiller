import math
import rsk
from rsk import constants

# Créé un client Robot Soccer Kit, qui permettra
# de communiquer avec le simulateur de soccer
client = rsk.Client()

# Boucle infinie
while True:
    # Récupération de la position de la balle
    balle_x = client.ball[0]
    balle_y = client.ball[1]

    # Définition de la position cible du robot
    x = constants.field_width / 2.0
    y = balle_y
    orientation = math.radians(180)

    # La fonction goto permet de déplacer le robot vers des
    # coordonnées (x, y, orientation)
    client.green1.goto((x, y, orientation),wait=False)
