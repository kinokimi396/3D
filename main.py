from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ground import create_ground
from mountain import create_mountain
from chest import create_chest

app = Ursina()

player = FirstPersonController(position=(0,5,0))

NORMAL_SPEED = 5
DASH_SPEED = 12
player.speed = NORMAL_SPEED

last_w_press_time = 0
is_dashing = False

mountain_entity = create_mountain()
ground_entity = create_ground()
chest_entity = create_chest(player)

def input(key):
    global last_w_press_time,is_dashing

    if key == 'w down':
        current_time = time.time()
        if current_time - last_w_press_time < 0.4:
            is_dashing = True
        last_w_press_time = current_time

    if key == 'e':
        if distance(player.position, chest_entity.position) < 3:
            chest_entity.gui.toggle()




Sky(color=color.cyan)

def update():
    global is_dashing

    if not held_keys['w']:
        is_dashing = False

    if is_dashing:
        player.speed = DASH_SPEED
    else:
        player.speed = NORMAL_SPEED
app.run()