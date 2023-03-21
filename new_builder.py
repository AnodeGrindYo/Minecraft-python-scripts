import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

block_1 = [-60, 20, 31]
block_2 = [-101, 20, -27]
first_floor_total_heigth = 7

def get_player_coordinates():
    x, y, z = mc.player.getTilePos()
    coordinates = [x, y, z]
    return coordinates

def get_x_min(coord_1, coord_2):
    return min(coord_1[0], coord_2[0])

def get_x_max(coord_1, coord_2):
    return max(coord_1[0], coord_2[0])


def get_z_min(coord_1, coord_2):
    return min(coord_1[2], coord_2[2])
    
def get_z_max(coord_1, coord_2):
    return max(coord_1[2], coord_2[2])

def get_rectangle_corners(coord_1, coord_2):
    x_min = get_x_min(coord_1, coord_2)
    x_max = get_x_max(coord_1, coord_2)
    z_min = get_z_min(coord_1, coord_2)
    z_max = get_z_max(coord_1, coord_2)
    y = coord_1[1]
    A = [x_min, y, z_min]
    B = [x_max, y, z_min]
    C = [x_min, y, z_max]
    D = [x_max, y, z_max]
    return A, B, C, D

def get_floor_dimensions(coord_1, coord_2):
    x_min = get_x_min(coord_1, coord_2)
    x_max = get_x_max(coord_1, coord_2)
    z_min = get_z_min(coord_1, coord_2)
    z_max = get_z_max(coord_1, coord_2)
    length = x_max - x_min
    width = z_max - z_min
    print("floor_dimensions : ")
    print("length : {} blocks".format(length))
    print("width  : {} blocks".format(width))
    print("surface : {} blocks".format(length * width))
    floor_dimensions = {
        "length": length,
        "width": width,
        "surface":length*width
    }
    return floor_dimensions

def build_floor(coord_1, coord_2, material=block.STONE_BRICK.id):
    A, B, C, D = get_rectangle_corners(coord_1, coord_2)
    x_min = A[0]
    x_max = B[0]
    z_min = A[2]
    z_max = C[2]
    floor_dimensions = get_floor_dimensions(coord_1, coord_2)
    for i in range(floor_dimensions["length"]):
        for j in range(floor_dimensions["width"]):
            # print(i, j)
            x = x_min + i
            z = z_min + j
            mc.setBlock(x, A[1], z, material)
    return

def clean_room_space(coord_1, coord_2, total_heigth):
    y_clean_min = coord_1[1] + 1
    y_clean_max = coord_1[1] + total_heigth - 1
    for y in range(y_clean_min, y_clean_max):
        # print(y)
        A = [
                coord_1[0],
                y, 
                coord_1[2]
            ]
        B = [
                coord_2[0],
                y,
                coord_2[2]
            ]
        build_floor(A, B, block.AIR.id)
    return

def build_walls(coord_1, coord_2, height, material=block.STONE_BRICK.id):
    A, B, C, D = get_rectangle_corners(coord_1, coord_2)
    x_min = A[0]
    x_max = B[0]
    y_min = A[1]
    y_max = y_min + height
    z_min = A[2]
    z_max = C[2]
    for y in range(y_min, y_max):
        # construction des murs en X
        for x in range(x_min, x_max):
            mc.setBlock(x, y, z_min, material)
            mc.setBlock(x, y, z_max, material)
        for z in range(z_min, z_max):
            mc.setBlock(x_min, y, z, material)
            mc.setBlock(x_max, y, z, material)
    return


# Main
# print("player coordinates : ")
# print(get_player_coordinates())
# A, B, C, D = get_rectangle_corners(block_1, block_2)
# print(A)
# print(B)
# print(C)
# print(D)
# floor_dimensions = get_floor_dimensions(block_1, block_2)
# print(floor_dimensions)

# RDC
build_floor(coord_1=block_1, coord_2=block_2, material=block.STONE_BRICK.id)
clean_room_space(block_1, block_2, first_floor_total_heigth)
build_walls(block_1, block_2, first_floor_total_heigth)

# Etage 1
block_3 = block_1
block_3[1] = block_3[1] + first_floor_total_heigth -1
block_4 = block_2
block_4[1] = block_4[1] + first_floor_total_heigth - 1
build_floor(block_3, block_4)
second_floor_height=6
clean_room_space(block_3, block_4, second_floor_height)
build_walls(block_3, block_4, second_floor_height)

# Etage 2
third_floor_height = 7
block_5 = block_3
block_5[1] = block_5[1] + third_floor_height -1
block_6 = block_4
block_6[1] = block_6[1] + third_floor_height -1
build_floor(block_5, block_6)
clean_room_space(block_5, block_6, third_floor_height)
build_walls(block_5, block_6, third_floor_height)

# Etage 3
fourth_floor_height = 6
block_7 = block_5
block_7[1] = block_7[1] + fourth_floor_height -1
block_8 = block_6
block_8[1] = block_8[1] + fourth_floor_height -1
build_floor(block_7, block_8)
clean_room_space(block_7, block_8, fourth_floor_height)
build_walls(block_7, block_8, fourth_floor_height)

# Etage 4
fifth_floor_height = 6
block_9 = block_7
block_9[1] = block_9[1] + fifth_floor_height - 1
block_10 = block_8
block_10[1] = block_10[1] + fifth_floor_height - 1
build_floor(block_9, block_10)
clean_room_space(block_9, block_10, fourth_floor_height)
build_walls(block_9, block_10, fourth_floor_height)