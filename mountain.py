from ursina import *

def create_mountain():

    mountain_group = Entity()

    for x in range(-15,16):
        for z in range(-15,16):

            height = 12 - (abs(x)+abs(z))//2
            if height > 0:
                for y in range(height):
                    Entity(
                    model='cube',
                    parent=mountain_group,
                    color=color.rgb(100,150,80),
                    position=(x+20,y,z+20),
                    collider='box'
                    )
    return mountain_group

