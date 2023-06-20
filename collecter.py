import arcade, random

BREITE = 800
HÖHE = 600

class  Collecter(arcade.Window):
    def __init__(self, breite, höhe, titel):
        super().__init__(breite, höhe, titel)

        arcade.set_background_color(arcade.color.DARK_BROWN)

        self.gegenstand_list = arcade.SpriteList()
        self.usables = arcade.SpriteList()
        self.anzahl_sprites = 0

        self.setup()

    def setup(self):

        for i in range (20000):
            grass = arcade.Sprite("Grassss.png", 0.3)
            grass.center_x = random.randrange(BREITE)
            grass.center_y = random.randrange(HÖHE)
            self.gegenstand_list.append(grass)

        kreuz1 = arcade.Sprite("Kreuz2.png")
        kreuz1.center_x = random.randrange(BREITE)
        kreuz1.center_y = random.randrange(HÖHE)
        self.gegenstand_list.append(kreuz1)
        self.usables.append(kreuz1)
        self.anzahl_sprites += 1

        kreuz2 = arcade.Sprite("Kreuz2.png")
        kreuz2.center_x = random.randrange(BREITE)
        kreuz2.center_y = random.randrange(HÖHE)
        self.gegenstand_list.append(kreuz2)
        self.usables.append(kreuz2)
        self.anzahl_sprites += 1


        heart1 = arcade.Sprite("Heart.png")
        heart1.center_x = 80
        heart1.center_y = 580
        self.gegenstand_list.append(heart1)
        self.anzahl_sprites += 1


        heart2 = arcade.Sprite("Heart.png")
        heart2.center_x = 110
        heart2.center_y = 580
        self.gegenstand_list.append(heart2)
        self.anzahl_sprites += 1

        heart3 = arcade.Sprite("Heart.png")
        heart3.center_x = 140
        heart3.center_y = 580
        self.gegenstand_list.append(heart3)
        self.anzahl_sprites += 1
        
        heart4 = arcade.Sprite("Heart.png")
        heart4.center_x = 50
        heart4.center_y = 580
        self.gegenstand_list.append(heart4)
        self.anzahl_sprites += 1

        phone1 = arcade.Sprite("phone.png")
        phone1.center_x = random.randrange(BREITE)
        phone1.center_y = random.randrange(HÖHE)
        self.gegenstand_list.append(phone1)
        self.usables.append(phone1)
        self.anzahl_sprites += 1

        



    def on_mouse_press(self, x, y, taste, modifiers):
        pseudosprite = arcade.Sprite()
        pseudosprite.center_x = x
        pseudosprite.center_y = y
        pseudosprite.set_hit_box([(-1, 1), (1, 1), (-1, -1), (1, -1)])

        self.gegenstand_hitlist = arcade.check_for_collision_with_list(pseudosprite, self.usables)

        for gegenstand in self.gegenstand_hitlist:
            gegenstand.kill()
            self.anzahl_sprites -=1
            print(self.anzahl_sprites)
            print(self.level_finished())

    def on_draw (self):
        self.clear()

        self.gegenstand_list.draw()

    def level_finished(self):
        if self.anzahl_sprites == 0:
            return True
        else:
            return False

    def play(self) -> bool:

        if self.level_finished():
            print("WoooooHOOOOOO")
            
arcade.run()