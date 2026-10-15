from ursina import *

GROUND_SIZE = 300

def create_ground():

    ground = Entity(
        model='cube',
        scale=(GROUND_SIZE,2,GROUND_SIZE),
        position=(0,-1,0),
        color=color.green,
        texture='white_cube',
        texture_scale=(GROUND_SIZE,GROUND_SIZE),
        collider='box'
    )
    half_size = GROUND_SIZE/2
    wall_height=20
    wall_thickness = 5 

    ground.walls = [
        # 奥の壁 (Z = +150)
        Entity(model='cube', scale=(GROUND_SIZE, wall_height, wall_thickness), position=(0, wall_height/2, half_size), collider='box', visible=False),
        # 手前の壁 (Z = -150)
        Entity(model='cube', scale=(GROUND_SIZE, wall_height, wall_thickness), position=(0, wall_height/2, -half_size), collider='box', visible=False),
        # 右の壁 (X = +150)
        Entity(model='cube', scale=(wall_thickness, wall_height, GROUND_SIZE), position=(half_size, wall_height/2, 0), collider='box', visible=False),
        # 左の壁 (X = -150)
        Entity(model='cube', scale=(wall_thickness, wall_height, GROUND_SIZE), position=(-half_size, wall_height/2, 0), collider='box', visible=False),
    ]

    return ground