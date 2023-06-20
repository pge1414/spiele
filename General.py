import arcade, GameView, InstructionView

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "1"


class MyGame(arcade.Window):
    

    def main():

        window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        start_view = InstructionView()
        window.show_view(start_view)

        window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        start_view = GameView()
        window.show_view(start_view)
        start_view.setup()
        """ Main function """

arcade.run()