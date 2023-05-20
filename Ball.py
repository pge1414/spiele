import arcade, random, time

BREITE = 800
HÖHE = 600

class Ball(arcade.Window):

    def __init__(self, breite, höhe, title):
        super().__init__(breite, höhe, title)

        arcade.set_background_color(arcade.color.BLACK)

        self.gegenstand_list = arcade.SpriteList()
        self.bewegungs_list = arcade.SpriteList()
        self.alive = True
        self.moon_placeX = 700
        self.moon_placeY = 500

        self.setup()

    def setup(self):
        
        ground = arcade.Sprite("Mama.png",0.5)
        ground.set_position(100,100)
        self.gegenstand_list.append(ground)

        ground2 = arcade.Sprite("Mama.png",0.5)
        ground2.set_position(400,100)
        self.gegenstand_list.append(ground2)

        ground3 = arcade.Sprite("Mama.png",0.5)
        ground3.set_position(700,100)
        self.gegenstand_list.append(ground3)
        
        for i in range(2000):
            star = arcade.Sprite("Star.png",0.1)
            star.center_x = random.randrange(BREITE)
            star.center_y = random.randrange(100, 600)
            self.gegenstand_list.append(star)
        
        moon = arcade.Sprite("Moon.png",0.2)
        moon.center_x = self.moon_placeX
        moon.center_y = self.moon_placeY
        moon.set_position(moon.center_x,moon.center_y)
        self.gegenstand_list.append(moon)

        enemy = arcade.Sprite("enemy.gif",0.2)
        enemy.center_x = 810
        enemy.center_y = 120
        enemy.set_position(enemy.center_x,enemy.center_y)
        self.gegenstand_list.append(enemy)
        self.bewegungs_list.append(enemy)

    #vdef game(self):
        #for i in range(30):
        #    time.sleep(0.5)
        #    for gegenstand in self.bewegungs_list:
        #        gegenstand.center_x -= 5
        #        gegenstand.set_position(gegenstand.center_x,gegenstand.center_y)


    def on_draw(self):
        self.clear()
        self.gegenstand_list.draw()

ball_spiel = Ball(BREITE, HÖHE, "Suchspiel")



arcade.run()
