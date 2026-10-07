from ursina import *

app = Ursina()

player = Entity(model='cube', color=color.orange, scale_y=2)

ground = Entity(model='plane', scale=100, texture='white_cube', texture_scale=(100, 100), collider='box')

EditorCamera()

app.run()

