import arcade, random

BREITE = 800
HÖHE = 600


class  Collecter(arcade.Window):
    def __init__(self, breite, höhe, titel):
        super().__init__(breite, höhe, titel)

        arcade.set_background_color(arcade.color.DARK_GREEN)

        self.gegenstand_list = arcade.SpriteList()

        self.setup()
        
    def setup(self):

        kreuz1 = arcade.Sprite("Kreuz2.png")
        kreuz1.center_x = random.randrange(BREITE)
        kreuz1.center_y = random.randrange(HÖHE)
        self.gegenstand_list.append(kreuz1)

        kreuz2 = arcade.Sprite("Kreuz2.png")
        kreuz2.center_x = random.randrange(BREITE)
        kreuz2.center_y = random.randrange(HÖHE)
        self.gegenstand_list.append(kreuz2)

        heart1 = arcade.Sprite("Heart.png")
        heart1.center_x = random.randrange(BREITE)
        heart1.center_y = random.randrange(HÖHE)
        self.gegenstand_list.append(heart1)

        heart2 = arcade.Sprite("Heart.png")
        heart2.center_x = random.randrange(BREITE)
        heart2.center_y = random.randrange(HÖHE)
        self.gegenstand_list.append(heart2)
        
        heart3 = arcade.Sprite("Heart.png")
        heart3.center_x = random.randrange(BREITE)
        heart3.center_y = random.randrange(HÖHE)
        self.gegenstand_list.append(heart3)
        
        heart4 = arcade.Sprite("Heart.png")
        heart4.center_x = random.randrange(BREITE)
        heart4.center_y = random.randrange(HÖHE)
        self.gegenstand_list.append(heart4)

        phone1 = arcade.Sprite("phone.png")
        phone1.center_x = random.randrange(BREITE)
        phone1.center_y = random.randrange(HÖHE)
        self.gegenstand_list.append(phone1)

        for i in range (1600):
            grass = arcade.Sprite("grass.png", 0.3)
            grass.center_x = random.randrange(BREITE)
            grass.center_y = random.randrange(HÖHE)
            self.gegenstand_list.append(grass)


    def on_mouse_press(self, x, y, button, modifiers):
        pseudosprite = arcade.Sprite()
        pseudosprite.center_x = x
        pseudosprite.center_y = y
        pseudosprite.set_hit_box([(-1, 1), (1, 1), (-1, -1), (1, -1)])

        gegenstand_hitlist = arcade.check_for_collision_with_list(pseudosprite, self.gegenstand_list)

        for gegenstand in gegenstand_hitlist:
            gegenstand.kill()

    def on_draw (self):
        self.clear()

        self.gegenstand_list.draw()

spiel = Collecter(BREITE, HÖHE, "Suchspiel")
arcade.run()
 