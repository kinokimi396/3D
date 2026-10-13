from ursina import *

GROUND_SIZE = 500

def create_ground():

    ground = Entity(
        model='plane',
        scale=(GROUND_SIZE,1,GROUND_SIZE),
        color=color.white,
        texture='white_cube',
        texture_scale=(GROUND_SIZE,GROUND_SIZE),
        collider='box'
    )
    return ground

def update_ground(player,ground):

    dx = player.x - ground.x
    dz = player.z - ground.z

    if abs(dx)>GROUND_SIZE/4:
        ground.x += dx
    if abs(dz) > GROUND_SIZE/4:
        ground.z += dz