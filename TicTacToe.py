import arcade, time, random

BREITE = 660
HÖHE = 700


class  TicTacToe(arcade.Window):


    def __init__(self, breite, höhe, titel):
        super().__init__(breite, höhe, titel)

        arcade.set_background_color(arcade.color.WHITE)

        self.score_player1 = 0
        self.score_player2 = 0

        self.setup()

    def setup(self):

        self.gegenstand_list = arcade.SpriteList()
        self.felder = arcade.SpriteList()
        self.felder_list = []
        self.button_list = arcade.SpriteList()
        self.player1_symbol = "x"
        self.player2_symbol = "o"
        self.background = None
        
        self.play = True

        self.player1 = True

        self.background = arcade.load_texture('Back.jpg')

        field1 = arcade.Sprite("Field.png",0.9)
        field1.center_x = 200
        field1.center_y = 600
        field1.set_position(200,600)
        field1.info = 1
        self.felder_list.append(field1.info)
        self.gegenstand_list.append(field1)
        self.felder.append(field1)

        field2 = arcade.Sprite("Field.png",0.9)
        field2.center_x = 400
        field2.center_y = 600
        field2.set_position(400,600)
        field2.info = 2
        self.felder_list.append(field2.info)
        self.gegenstand_list.append(field2)
        self.felder.append(field2)

        field3 = arcade.Sprite("Field.png",0.9)
        field3.center_x = 600
        field3.center_y = 600
        field3.set_position(600,600)
        field3.info = 3
        self.felder_list.append(field3.info)
        self.gegenstand_list.append(field3)
        self.felder.append(field3)

        field4 = arcade.Sprite("Field.png",0.9)
        field4.center_x = 200
        field4.center_y = 400
        field4.set_position(200,400)
        field4.info = 4
        self.felder_list.append(field4.info)
        self.gegenstand_list.append(field4)
        self.felder.append(field4)

        field5 = arcade.Sprite("Field.png",0.9)
        field5.center_x = 400
        field5.center_y = 400
        field5.set_position(400,400)
        field5.info =5
        self.felder_list.append(field5.info)
        self.gegenstand_list.append(field5)
        self.felder.append(field5)

        field6 = arcade.Sprite("Field.png",0.9)
        field6.center_x = 600
        field6.center_y = 400
        field6.set_position(600,400)
        field6.info = 6
        self.felder_list.append(field6.info)
        self.gegenstand_list.append(field6)
        self.felder.append(field6)

        field7 = arcade.Sprite("Field.png",0.9)
        field7.center_x = 200
        field7.center_y = 200
        field7.set_position(200,200)
        field7.info = 7
        self.felder_list.append(field7.info)
        self.gegenstand_list.append(field7)
        self.felder.append(field7)

        field8 = arcade.Sprite("Field.png",0.9)
        field8.center_x = 400
        field8.center_y = 200
        field8.set_position(400,200)
        field8.info = 8
        self.felder_list.append(field8.info)
        self.gegenstand_list.append(field8)
        self.felder.append(field8)

        field9 = arcade.Sprite("Field.png",0.9)
        field9.center_x = 600
        field9.center_y = 200
        field9.set_position(600,200)
        field9.info = 9
        self.felder_list.append(field9.info)
        self.gegenstand_list.append(field9)
        self.felder.append(field9)

    def on_mouse_press(self, x, y, taste, modifiers):

        if self.play:

            pseudosprite = arcade.Sprite()
            pseudosprite.center_x = x
            pseudosprite.center_y = y
            pseudosprite.set_hit_box([(-1, 1), (1, 1), (-1, -1), (1, -1)])

            self.gegenstand_hitlist = arcade.check_for_collision_with_list(pseudosprite, self.felder)

            for gegenstand in self.gegenstand_hitlist:
                

                if self.player1 == True:

                    self.felder_list[gegenstand.info -1] = self.player1_symbol

                    x_sprite = arcade.Sprite("X.png", 0.9)
                    x_sprite.set_position(gegenstand.center_x +45 , gegenstand.center_y -190)
                    self.gegenstand_list.append(x_sprite)
                    self.felder.remove(gegenstand)

                    self.player1 = False

                    self.gewinnprüfung()

                    print(gegenstand.info)

                elif self.player1 == False:

                    self.felder_list[gegenstand.info -1] = self.player2_symbol

                    o_sprite = arcade.Sprite("Fett.png", 1)
                    o_sprite.set_position(gegenstand.center_x-15, gegenstand.center_y -195)
                    self.gegenstand_list.append(o_sprite)
                    self.felder.remove(gegenstand)
                    self.player1 = True

                    print(gegenstand.info)
                
                self.winning()
                print(self.felder_list)
                print(self.gewinnprüfung())

        else:
            if self.player1 == False:
                self.score_player1 += 1
            else:
                self.score_player2 += 1
                
            self.setup()

    def winning(self):
         if self.gewinnprüfung():
            if not self.player1:
                print("Player 1 wins")
            else:
                print("Player 2 wins")

    def on_draw (self):
        self.clear()

        arcade.draw_lrwh_rectangle_textured(0, 0,BREITE, HÖHE,self.background)
        arcade.draw_text(str(self.score_player1) + str(self.score_player2),60,640,arcade.color.FRENCH_WINE,font_size= 14, bold=True)


        self.gegenstand_list.draw()
        
        if self.gewinnprüfung():

            arcade.draw_text("The WINNER is:",90,400,arcade.color.FRENCH_WINE,font_size= 50, bold=True)

            if not self.player1:
                arcade.draw_text("Player 1",200,300,arcade.color.FRENCH_WINE,font_size= 50, bold=True)
                
            else:
                arcade.draw_text("Player 2",200,300,arcade.color.FRENCH_WINE,font_size= 50, bold = True)
                
            self.play = False

    def gewinnprüfung(self):

        return self.felder_list[0] == self.felder_list[1] == self.felder_list[2] or \
                self.felder_list[3] == self.felder_list[4] == self.felder_list[5] or \
                self.felder_list[6] == self.felder_list[7] == self.felder_list[8] or \
                self.felder_list[0] == self.felder_list[3] == self.felder_list[6] or \
                self.felder_list[1] == self.felder_list[4] == self.felder_list[7] or \
                self.felder_list[2] == self.felder_list[5] == self.felder_list[8] or \
                self.felder_list[0] == self.felder_list[4] == self.felder_list[8] or \
                self.felder_list[2] == self.felder_list[4] == self.felder_list[6]
    
tictactoe_spiel = TicTacToe(BREITE, HÖHE, "TicTacToe")

arcade.run()