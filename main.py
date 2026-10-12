from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

player = FirstPersonController(position=(0,2,0))

GROUND_SIZE = 500

ground = Entity(
    
)