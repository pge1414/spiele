import arcade

class GameOver(arcade.Window):
    def __init__(self, breite, höhe, titel):
        super().__init__(breite, höhe, titel)

        arcade.set_background_color(arcade.color.GREEN_YELLOW)

    def on_draw(self):
        self.clear()