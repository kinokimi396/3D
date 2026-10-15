from ursina import *

class ChestGUI(Entity):
    def __init__(self):

        super().__init__()

        self.background = Entity(
            parent=camera.ui,
            model='quad',
            color=color.black66,
            scale=(0.5,0.4),
            position=(0,0),
            enabled=False
        )

        self.title_text = Text(
            parent=self.background,
            text='Chest Inventory',
            scale=1.5,
            position=(-0.15,0.20),
            color=color.white,
            enabled=False
        )
        self.is_open = False


        self.slots = []
        for row in range(3):
            for col in range(3):
                slot = Button(
                    parent=self.background,
                    model='quad',
                    color=color.dark_gray,
                    scale=(0.15,0.15),

                    position=(col*0.18-0.18,-row*0.18+0.05),
                    text='',
                    enabled=False
                )
                self.slots.append(slot)

    def toggle(self):

            self.is_open = not self.is_open

            self.background.enabled = self.is_open
            self.title_text.enabled = self.is_open
            for slot in self.slots:
                slot.enabled = self.is_open

            mouse.locked = not self.is_open
            mouse.visible = self.is_open

    