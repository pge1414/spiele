import arcade

class GameView(arcade.View):
    super().__init__()

    def on_mouse_press(self, _x, _y, _button, _modifiers):
            """ If the user presses the mouse button, start the game. """
            game_view = GameView()
            game_view.setup()
            self.window.show_view(game_view)

arcade.run()