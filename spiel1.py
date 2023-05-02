import arcade, random

BREITE = 800
HÖHE = 600


class  Spiel(arcade.Window):
    def __init__(self, breite, höhe, titel):
        super().__init__(breite, höhe, titel)

        arcade.set_background_color(arcade.color.BLUE)

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

    def on_draw (self):
        self.clear()

        self.gegenstand_list.draw()

spiel = Spiel(BREITE, HÖHE, "Suchspiel")
arcade.run()
 