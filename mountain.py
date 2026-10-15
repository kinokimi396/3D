from ursina import *
import random


def create_mountain():
    mountain_group = Entity()

    side_colors = [color.gray,color.brown,color.dark_gray,color.light_gray]

    heights = {}
    min_x,max_x = -6,7
    min_z,max_z = -6,7

    for x in range(min_x,max_x+1):
        for z in range(min_z,max_z+1):

            if x == min_x or x == max_x or z == min_z:
                heights[(x,z)] = 1
            else:
                base_height = 9 - (abs(x)+abs(z))//2
                rand_offset = random.randint(-1,1)
                h = base_height+rand_offset
                heights[(x,z)] = max(1,h) if h>0 else 0

    top_group=Entity()
    side_group=Entity()

    for x in range(min_x,max_x+1):
        for z in range(min_z,max_z+1):
            h = heights[(x,z)]
            if h == 0:
                continue
            for y in range(h):
                is_top=(y==h-1)
                is_exposed_side=(
                    (x==min_x or x == max_x or z==min_z or z == max_z) or
                    (heights.get((x+1,z),0)<=y)or
                    (heights.get((x-1,z),0)<=y) or
                    (heights.get((x,z+1),0)<=y) or
                    (heights.get((x,z-1),0)<=y)
                )
                if is_top:
                    Entity(
                        model='cube',
                        parent=top_group,
                        color=color.lime,
                        texture=None,
                        position=(x+20,y,z+20),
                        collider='box'
                    )
                elif is_exposed_side:
                    Entity(
                        model='cube',
                        parent=side_group,
                        color=random.choice(side_colors),
                        texture=None,
                        position=(x+20,y,z+20),
                        collider='box'
                    )

    #top_group.combine(auto_destroy=True)
    #side_group.combine(auto_destroy=True)

    #top_group.collider = 'box'
    #side_group.collider = 'box'

    #top_group.parent = mountain_group
    #side_group.parent = mountain_group

    #mountain_group.combine(auto_destroy=True)
    return mountain_group
