from ursina import *
from inventory_ui import ChestGUI
def create_chest(player):

    chest_group = Entity(position=(1,0,1))

    Entity(
        model='cube',
        parent=chest_group,
        scale=(1.5,1,1.2),
        position=(0,0.5,0),
        color=color.gold,
        texture=None,
        collider='box'
    )
    Entity(
        model='cube',
        parent=chest_group,
        scale=(0.4,0.2,0.3),
        color=color.orange,
        texture=None,
        collider='box'
    )

    chest_gui = ChestGUI()

    def update():

        dist = distance(player.position,chest_group.position)

        if dist < 3:
            pass

    chest_group.update = update
    chest_group.gui = chest_gui

    return chest_group