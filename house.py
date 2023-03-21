import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()

def build_house(x, y, z, width, depth, floor_material, wall_material, roof_material, num_floors):
    height = num_floors * 4
    floor_height = height // num_floors
    for floor in range(num_floors):
        # Construire le sol
        for i in range(x, x + width):
            for j in range(z, z + depth):
                mc.setBlock(i, y + floor * floor_height, j, floor_material)

        # Construire les murs
        for i in range(x, x + width):
            for j in range(y + floor * floor_height + 1, y + (floor + 1) * floor_height):
                mc.setBlock(i, j, z, wall_material)
                mc.setBlock(i, j, z + depth - 1, wall_material)
        for i in range(z, z + depth):
            for j in range(y + floor * floor_height + 1, y + (floor + 1) * floor_height):
                mc.setBlock(x, j, i, wall_material)
                mc.setBlock(x + width - 1, j, i, wall_material)

        # Ajouter une porte
        mc.setBlock(x + width // 2, y + floor * floor_height + 1, z, block.DOOR_IRON.id, 0)
        mc.setBlock(x + width // 2, y + floor * floor_height + 2, z, block.DOOR_IRON.id, 8)

        # Ajouter des fenêtres
        mc.setBlock(x + width // 4, y + floor * floor_height + floor_height // 2, z, block.GLASS_PANE.id)
        mc.setBlock(x + width - width // 4, y + floor * floor_height + floor_height // 2, z, block.GLASS_PANE.id)
        mc.setBlock(x + width // 4, y + floor * floor_height + floor_height // 2, z + depth - 1, block.GLASS_PANE.id)
        mc.setBlock(x + width - width // 4, y + floor * floor_height + floor_height // 2, z + depth - 1, block.GLASS_PANE.id)

        # Construire le toit
        for i in range(x, x + width):
            mc.setBlock(i, y + (floor + 1) * floor_height, z, roof_material)
            mc.setBlock(i, y + (floor + 1) * floor_height, z + depth - 1, roof_material)
        for i in range(z, z + depth):
            mc.setBlock(x, y + (floor + 1) * floor_height, i, roof_material)
        
        # Ajouter des escaliers
        if floor < num_floors - 1:
            # Creuser un trou dans le sol pour les escaliers
            for i in range(x + width - 1, x + width + 1):
                for j in range(y + floor * floor_height, y + floor * floor_height + 2):
                    mc.setBlock(i, j, z + depth - 1, block.AIR.id)

            for j in range(y + floor * floor_height + 1, y + (floor + 1) * floor_height + 1):
                mc.setBlock(x + width - 1, j, z + depth - 1, block.STAIRS_NETHER_BRICK.id, 0)
        

# exemple pour construire un gratte-ciel:
x, y, z = mc.player.getTilePos()
width = 10
depth = 10
# floor_height = 3
num_floors = 20
wall_material = block.GLASS.id
floor_material = block.IRON_BLOCK.id
roof_material = block.IRON_BLOCK.id
door_material = block.DOOR_IRON.id
window_material = block.GLASS.id


build_house(x, y, z, width, depth, floor_material, wall_material, roof_material, num_floors)