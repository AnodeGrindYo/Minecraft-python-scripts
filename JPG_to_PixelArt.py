import mcpi.minecraft as minecraft
import mcpi.block as block
from PIL import Image

# PERMET D'IMPORTER UNE IMAGE JPG ET D'EN FAIRE 
# DU PIXEL ART DANS UN MONDE MINECRAFT A L'AIDE
# DE BLOCKS DE LAINE

# permet d'avoir le numéro identifiant des couleurs de laine
WOOL_COLOR = {
    "WHITE":0,
    "ORANGE":1,
    "MAGENTA":2,
    "LIGHT_BLUE":3,
    "YELLOW":4,
    "LIME":5,
    "PINK":6,
    "GRAY":7,
    "LIGHT_GRAY":8,
    "CYAN":9,
    "PURPLE":10,
    "BLUE":11,
    "BROWN":12,
    "GREEN":13,
    "RED":14,
    "BLACK":15
}

WOOL_COLOR_RGB = {
    "WHITE": (255, 255, 255),
    "ORANGE": (255, 165, 0),
    "MAGENTA": (255, 0, 255),
    "LIGHT_BLUE": (173, 216, 230),
    "YELLOW": (255, 255, 0),
    "LIME": (0, 255, 0),
    "PINK": (255, 192, 203),
    "GRAY": (128, 128, 128),
    "LIGHT_GRAY": (211, 211, 211),
    "CYAN": (0, 255, 255),
    "PURPLE": (128, 0, 128),
    "BLUE": (0, 0, 255),
    "BROWN": (165, 42, 42),
    "GREEN": (0, 128, 0),
    "RED": (255, 0, 0),
    "BLACK": (0, 0, 0)
}




def flatten_terrain(mc, length, width):
    # Récupérer la position actuelle du joueur
    x, y, z = mc.player.getPos()

    # Calculer les coordonnées du coin supérieur gauche de la zone à niveler
    startX = int(x - (length // 2))
    startZ = int(z - (width // 2))
    endX = int(startX + length)
    endZ = int(startZ + width)

    # Remplacer les blocs dans la zone définie avec des blocs de terre
    for i in range(startX, endX):
        for j in range(startZ, endZ):
            mc.setBlock(i, y, j, block.DIRT)
            
def faire_sol(mc, length, width, block_type=block.COBBLESTONE):
    # Récupérer la position actuelle du joueur
    x, y, z = mc.player.getPos()
    
    # Calculer les coordonnées du coin supérieur gauche de la zone à niveler
    startX = int(x - (length // 2))
    startZ = int(z - (width // 2))
    endX = int(startX + length)
    endZ = int(startZ + width)
    
    # Remplacer les blocs dans la zone définie avec des blocs de terre
    for i in range(startX, endX):
        for j in range(startZ, endZ):
            mc.setBlock(i, y, j, block_type)
            
def faire_damier(mc, length, width, block_type=block.WOOL.id, color_A=WOOL_COLOR["WHITE"], color_B=WOOL_COLOR["BLACK"]):
    # Récupérer la position actuelle du joueur
    x, y, z = mc.player.getPos()
    
    # Calculer les coordonnées du coin supérieur gauche de la zone à niveler
    startX = int(x - (length // 2))
    startZ = int(z - (width // 2))
    endX = int(startX + length)
    endZ = int(startZ + width)
    
    # créationnalisationnage du damier
    for i in range(startX, endX):
        for j in range(startZ, endZ):
            if((i%2==0)):
                if(j%2==0):
                    mc.setBlock(i, y, j, block_type, color_A)
                else:
                    mc.setBlock(i, y, j, block_type, color_B)
            else:
                if(j%2==0):
                    mc.setBlock(i, y, j, block_type, color_B)
                else:
                    mc.setBlock(i, y, j, block_type, color_A)

def create_wall(mc, image_path, height, width):
    # Récupérer la position actuelle du joueur
    x, y, z = mc.player.getPos()

    # Charger l'image à partir du chemin d'accès
    image = Image.open(image_path)

    # Réduire l'image à la taille souhaitée
    image = image.resize((width, height), Image.LANCZOS)
    
    # retourne l'image
    image = image.rotate(180)

    # Convertir l'image en pixels RGB
    pixels = image.load()
    
    # conversion des couleurs pour qu'elles correspondent aux couleurs de laine
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            # nearest_wool_color = min(WOOL_COLOR_RGB.items(), key=lambda x: abs(x[1] - (r, g, b)))[0]
            nearest_wool_color = min(WOOL_COLOR_RGB.items(), key=lambda x: ((r - x[1][0]) ** 2 + (g - x[1][1]) ** 2 + (b - x[1][2]) ** 2) ** 0.5)[0]
            # print(nearest_wool_color)
            pixels[i, j] = WOOL_COLOR_RGB[nearest_wool_color]

    # Pour chaque pixel de l'image, déterminer la couleur de laine correspondante
    # et la placer dans le monde Minecraft
    for i in range(height):
        for j in range(width):
            # Récupérer les composantes R, G, B du pixel
            r, g, b = pixels[j, i]

            # Convertir les composantes RGB en couleur de laine
            wool_color = None
            if r == 255 and g == 255 and b == 255:
                wool_color = block.WOOL.id, WOOL_COLOR["WHITE"]
            elif r == 255 and g == 165 and b == 0:
                wool_color = block.WOOL.id, WOOL_COLOR["ORANGE"]
            elif r == 255 and g == 0 and b == 255:
                wool_color = block.WOOL.id, WOOL_COLOR["MAGENTA"]
            elif r == 0 and g == 255 and b == 255:
                wool_color = block.WOOL.id, WOOL_COLOR["LIGHT_BLUE"]
            elif r == 255 and g == 255 and b == 0:
                wool_color = block.WOOL.id, WOOL_COLOR["YELLOW"]
            elif r == 0 and g == 255 and b == 0:
                wool_color = block.WOOL.id, WOOL_COLOR["LIME"]
            elif r == 255 and g == 192 and b == 203:
                wool_color = block.WOOL.id, WOOL_COLOR["PINK"]
            elif r == 128 and g == 128 and b == 128:
                wool_color = block.WOOL.id, WOOL_COLOR["GRAY"]
            elif r == 192 and g == 192 and b == 192:
                wool_color = block.WOOL.id, WOOL_COLOR["LIGHT_GRAY"]
            elif r == 0 and g == 255 and b == 255:
                wool_color = block.WOOL.id, WOOL_COLOR["CYAN"]
            elif r == 128 and g == 0 and b == 128:
                wool_color = block.WOOL.id, WOOL_COLOR["PURPLE"]
            elif r == 0 and g == 0 and b == 255:
                wool_color = block.WOOL.id, WOOL_COLOR["BLUE"]
            elif r == 165 and g == 42 and b == 42:
                wool_color = block.WOOL.id, WOOL_COLOR["BROWN"]
            elif r == 0 and g == 128 and b == 0:
                wool_color = block.WOOL.id, WOOL_COLOR["GREEN"]
            elif r == 255 and g == 0 and b == 0:
                wool_color = block.WOOL.id, WOOL_COLOR["RED"]
            else:
                wool_color = block.WOOL.id, WOOL_COLOR["BLACK"]
            mc.setBlock(x + j + 3, y+i, z+3, *wool_color)

def clear_space(mc, x, y, z):
    pos = mc.player.getPos()

    for i in range(x):
        for j in range(y):
            for k in range(z):
                mc.setBlock(pos.x + i - x//2, pos.y + j, pos.z + k - z//2, block.AIR.id)

mc = minecraft.Minecraft.create()

# Remplacer par l'emplacement d'un jpg sur votre disque dur
create_wall(mc, "./img/joconde.jpg", 50, 50)

# clear_space(mc, 100, 100, 100)
