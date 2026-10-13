from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ground import create_ground,update_ground
from mountain import create_mountain

app = Ursina()

player = FirstPersonController(position=(0,15,0))

NORMAL_SPEED = 5
DASH_SPEED = 12
player.speed = NORMAL_SPEED

last_w_press_time = 0
is_dashing = False

def input(key):
    global last_w_press_time,is_dashing

    if key == 'w down':
        current_time = time.time()
        if current_time - last_w_press_time < 0.4:
            is_dashing = True
        last_w_press_time = current_time

mountain_entity = create_mountain()
ground_entity = create_ground()

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