# Importing arcade module
import arcade

# Creating MainGame class	
class MainGame(arcade.Window):
	def __init__(self):
		super().__init__(600, 600, title="Keyboard Inputs")

		self.x = 100
		self.y = 100

	def on_draw(self):
		arcade.start_render()

		arcade.draw_circle_filled(self.x, self.y,25,arcade.color.GREEN)
		
	def on_mouse_motion(self, x, y, dx, dy):

		self.x = x
		self.y = y
	
	def on_mouse_press(self, x, y, button, modifiers):
		print("Mouse button is pressed")
					
MainGame()
arcade.run()
