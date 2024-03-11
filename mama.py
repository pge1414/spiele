import arcade, time, random

BREITE = 670
HÖHE = 700

# Phase 1 = Startscreen
# Phase 2 = Gamescreen
# Phase 3 = Systemscreen


class  TicTacToe(arcade.Window):


    def __init__(self, breite, höhe, titel):
        super().__init__(breite, höhe, titel)

        arcade.set_background_color(arcade.color.WHITE)

        self.score_player1 = 0
        self.score_player2 = 0
        self.play = False
        self.phase = 1
        self.anfang_liste = arcade.SpriteList()
        self.settings_liste = arcade.SpriteList()
        self.mode = "MULTIPLAYER"

    def setup(self):

        self.background = arcade.load_texture('Sunset.jpeg')
        
        self.gegenstand_list = arcade.SpriteList()
        self.felder = arcade.SpriteList()
        self.felder_ganz = arcade.SpriteList()
        self.felder_list = []
        self.feld_löschen = []
        self.button_list = arcade.SpriteList()
        self.player1_symbol = "x"
        self.player2_symbol = "o"
        self.background = None
        
        self.play = True

        self.player1 = True

        self.background = arcade.load_texture('Mountains.jpg')


        field1 = arcade.Sprite("Field.png",0.9)
        field1.center_x = 200
        field1.center_y = 600
        field1.set_position(200,600)
        field1.info = 1
        self.felder_list.append(field1.info)
        self.gegenstand_list.append(field1)
        self.felder.append(field1)
<<<<<<< HEAD
        self.felder_ganz.append(field1)
=======
        self.feld_löschen.append(field1.info)

>>>>>>> 5c75676edd89e06cf453fa5b07025eb20ee16431

        field2 = arcade.Sprite("Field.png",0.9)
        field2.center_x = 400
        field2.center_y = 600
        field2.set_position(400,600)
        field2.info = 2
        self.felder_list.append(field2.info)
        self.gegenstand_list.append(field2)
        self.felder.append(field2)
<<<<<<< HEAD
        self.felder_ganz.append(field2)
=======
        self.feld_löschen.append(field2.info)

>>>>>>> 5c75676edd89e06cf453fa5b07025eb20ee16431

        field3 = arcade.Sprite("Field.png",0.9)
        field3.center_x = 600
        field3.center_y = 600
        field3.set_position(600,600)
        field3.info = 3
        self.felder_list.append(field3.info)
        self.gegenstand_list.append(field3)
        self.felder.append(field3)
<<<<<<< HEAD
        self.felder_ganz.append(field3)
=======
        self.feld_löschen.append(field3.info)
>>>>>>> 5c75676edd89e06cf453fa5b07025eb20ee16431

        field4 = arcade.Sprite("Field.png",0.9)
        field4.center_x = 200
        field4.center_y = 400
        field4.set_position(200,400)
        field4.info = 4
        self.felder_list.append(field4.info)
        self.gegenstand_list.append(field4)
        self.felder.append(field4)
<<<<<<< HEAD
        self.felder_ganz.append(field4)
=======
        self.feld_löschen.append(field4.info)
>>>>>>> 5c75676edd89e06cf453fa5b07025eb20ee16431

        field5 = arcade.Sprite("Field.png",0.9)
        field5.center_x = 400
        field5.center_y = 400
        field5.set_position(400,400)
        field5.info =5
        self.felder_list.append(field5.info)
        self.gegenstand_list.append(field5)
        self.felder.append(field5)
<<<<<<< HEAD
        self.felder_ganz.append(field5)
=======
        self.feld_löschen.append(field5.info)
>>>>>>> 5c75676edd89e06cf453fa5b07025eb20ee16431

        field6 = arcade.Sprite("Field.png",0.9)
        field6.center_x = 600
        field6.center_y = 400
        field6.set_position(600,400)
        field6.info = 6
        self.felder_list.append(field6.info)
        self.gegenstand_list.append(field6)
        self.felder.append(field6)
<<<<<<< HEAD
        self.felder_ganz.append(field6)
=======
        self.feld_löschen.append(field6.info)
>>>>>>> 5c75676edd89e06cf453fa5b07025eb20ee16431

        field7 = arcade.Sprite("Field.png",0.9)
        field7.center_x = 200
        field7.center_y = 200
        field7.set_position(200,200)
        field7.info = 7
        self.felder_list.append(field7.info)
        self.gegenstand_list.append(field7)
        self.felder.append(field7)
<<<<<<< HEAD
        self.felder_ganz.append(field7)
=======
        self.feld_löschen.append(field7.info)
>>>>>>> 5c75676edd89e06cf453fa5b07025eb20ee16431

        field8 = arcade.Sprite("Field.png",0.9)
        field8.center_x = 400
        field8.center_y = 200
        field8.set_position(400,200)
        field8.info = 8
        self.felder_list.append(field8.info)
        self.gegenstand_list.append(field8)
        self.felder.append(field8)
<<<<<<< HEAD
        self.felder_ganz.append(field8)
=======
        self.feld_löschen.append(field8.info)
>>>>>>> 5c75676edd89e06cf453fa5b07025eb20ee16431

        field9 = arcade.Sprite("Field.png",0.9)
        field9.center_x = 600
        field9.center_y = 200
        field9.set_position(600,200)
        field9.info = 9
        self.felder_list.append(field9.info)
        self.gegenstand_list.append(field9)
        self.felder.append(field9)
<<<<<<< HEAD
        self.felder_ganz.append(field9)
=======
        self.feld_löschen.append(field9.info)
>>>>>>> 5c75676edd89e06cf453fa5b07025eb20ee16431

    def on_mouse_press(self, x, y, taste, modifiers):

        if self.play:

            pseudosprite = arcade.Sprite()
            pseudosprite.center_x = x
            pseudosprite.center_y = y
            pseudosprite.set_hit_box([(-1, 1), (1, 1), (-1, -1), (1, -1)])

            self.gegenstand_hitlist = arcade.check_for_collision_with_list(pseudosprite, self.felder)

            for gegenstand in self.gegenstand_hitlist:
                
                if self.mode == "SINGLEPLAYER":
<<<<<<< HEAD
=======

                        self.felder_list[gegenstand.info -1] = self.player1_symbol
>>>>>>> 5c75676edd89e06cf453fa5b07025eb20ee16431

                        x_sprite = arcade.Sprite("X.png", 0.9)
                        x_sprite.set_position(gegenstand.center_x +45 , gegenstand.center_y -190)
                        self.gegenstand_list.append(x_sprite)
                        self.felder.remove(gegenstand)

                        print(gegenstand.info)

                        self.gewinnprüfung()

                        player2 = Level_2('player2')
                        platz = player2.zug(self.felder_list)
                        self.felder_list[platz -1] = self.player2_symbol

                        print(platz)
                        print(self.felder_list)
                        print(self.felder)

<<<<<<< HEAD
                    player2 = Level_2('player2')
                    print(player2.zug(self.felder_list))
                    pos = player2.zug(self.felder_list)-1

                    self.felder_list[player2.zug(self.felder_list)-1] = self.player2_symbol


                else:

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

                       
=======
                        o_sprite = arcade.Sprite("Fett.png", 1)
                        o_sprite.set_position(self.felder[platz-1].center_x, self.felder[platz-1].center_y)
                        self.gegenstand_list.append(o_sprite)
                        self.felder.remove([self.felder[platz]])

                        self.gewinnprüfung()

                else:

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

>>>>>>> 5c75676edd89e06cf453fa5b07025eb20ee16431
                        self.felder_list[gegenstand.info -1] = self.player2_symbol

                        o_sprite = arcade.Sprite("Fett.png", 1)
                        o_sprite.set_position(gegenstand.center_x-15, gegenstand.center_y -195)
                        self.gegenstand_list.append(o_sprite)
                        self.felder.remove(gegenstand)
                        self.player1 = True

                        print(gegenstand.info)
                
                self.unentschieden()
                self.winning()
                self.pointcounter()
                print(self.felder_list)
                print(self.gewinnprüfung())
                print(self.unentschieden())

        else:
            if self.phase == 1:

                pseudosprite = arcade.Sprite()
                pseudosprite.center_x = x
                pseudosprite.center_y = y
                pseudosprite.set_hit_box([(-1, 1), (1, 1), (-1, -1), (1, -1)])

                listencheck = arcade.check_for_collision_with_list(pseudosprite, self.anfang_liste)
                if listencheck:
                    self.phase = 3

                else:
                    self.phase = 2
                    self.setup()


            if self.phase == 3:

                pseudosprite = arcade.Sprite()
                pseudosprite.center_x = x
                pseudosprite.center_y = y
                pseudosprite.set_hit_box([(-1, 1), (1, 1), (-1, -1), (1, -1)])

                self.settings = arcade.check_for_collision_with_list(pseudosprite, self.settings_liste)

                for setting in self.settings:
                    if setting == self.background_selection:
                        print("skin")

                    if setting == self.skin_selection:
                        print("background")

                    if setting == self.back:
                        self.phase = 1

                    if setting == self.mode_selection:
                        if self.mode == "SINGLEPLAYER":
                            self.mode = "MULTIPLAYER"

                        else:
                            self.mode = "SINGLEPLAYER"
                
            else:
                self.setup()
                

            if self.phase == 2:
                self.setup()


    def winning(self):
         if self.gewinnprüfung():
            if not self.player1:
                print("Player 1 wins")
            else:
                print("Player 2 wins")

    def unentschieden(self):
        if len(self.felder) == 0 and not self.gewinnprüfung():
            return True
        else:
            return False
        
    def pointcounter(self):
        if not self.unentschieden():
            if self.gewinnprüfung():

                if self.player1 == False:
                    self.score_player1 += 1
                else:
                    self.score_player2 += 1

    def on_draw (self):

        if self.phase == 1:

            self.clear()

            arcade.draw_lrwh_rectangle_textured(0,0,BREITE, HÖHE, arcade.load_texture('Back.jpg'))

            einstellungen = arcade.Sprite("einstellung.png",0.5)
            einstellungen.center_x = 600
            einstellungen.center_y = 660
            self.anfang_liste.append(einstellungen)

            self.anfang_liste.draw()

            arcade.draw_text("Tab to play!!!", 40, 400, arcade.color.FRENCH_WINE, font_size= 70, bold= True)

        if self.phase == 2:

            self.clear()

            arcade.draw_lrwh_rectangle_textured(0, 0,BREITE, HÖHE,self.background)
            arcade.draw_text("Score 1: " + str(self.score_player1)+ "     |      Score 2: " + str(self.score_player2),60,640,arcade.color.FRENCH_WINE,font_size= 14, bold=True)


            self.gegenstand_list.draw()
            
            if self.gewinnprüfung():

                self.play = False

                arcade.draw_text("The WINNER is:",90,400,arcade.color.FRENCH_WINE,font_size= 50, bold=True)

                arcade.draw_text(str(self.score_player1) + " : " + str(self.score_player2), 180, 500, arcade.color.FRENCH_WINE, font_size=100, bold=True)

                if not self.player1:
                    arcade.draw_text("Player 1",200,300,arcade.color.FRENCH_WINE,font_size= 50, bold=True)
                    
                else:
                    arcade.draw_text("Player 2",200,300,arcade.color.FRENCH_WINE,font_size= 50, bold = True)

                arcade.draw_text("Tap to play again...",240,200,arcade.color.FRENCH_WINE,font_size= 15)      

            
            if self.unentschieden():

                self.play = False

                arcade.draw_text("DRAW",120,400,arcade.color.FRENCH_WINE,font_size= 90, bold=True)

                arcade.draw_text("What a mess!!!",170,300,arcade.color.FRENCH_WINE,font_size= 30)  

                arcade.draw_text("Tap to play again...",240,200,arcade.color.FRENCH_WINE,font_size= 15)      

        if self.phase == 3:

            self.clear()

            self.play = False

            arcade.draw_lrwh_rectangle_textured(0, 0,BREITE, HÖHE,arcade.load_texture('sunset.jpeg'))
            arcade.draw_text("Settings",170,600,arcade.color.FRENCH_WINE,font_size= 60, bold=True)

            self.background_selection = arcade.Sprite("background.png",0.2)
            self.background_selection.center_x = 200
            self.background_selection.center_y = 100
            self.settings_liste.append(self.background_selection)

            self.skin_selection = arcade.Sprite("Skin.png",0.2)
            self.skin_selection.center_x = 200
            self.skin_selection.center_y = 300
            self.settings_liste.append(self.skin_selection)

            self.mode_selection = arcade.Sprite("singles.png",0.2)
            self.mode_selection.center_x = 200
            self.mode_selection.center_y = 500
            self.settings_liste.append(self.mode_selection)

            arcade.draw_text(self.mode,270,500,arcade.color.FRENCH_WINE,font_size= 20, bold=True)

            self.back = arcade.Sprite("back.png",0.1)
            self.back.center_x = 50
            self.back.center_y = 650
            self.settings_liste.append(self.back)

            self.settings_liste.draw()

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

class Level_2:
    def __init__(self, name):
        self.name = name
    
    def zug(self, spielfeld):
        feld = 0
        gültige_eingabe = False
        if spielfeld[0] == spielfeld[1] == "x" and spielfeld[2] != "o":
            feld = 3
        elif spielfeld[1] == spielfeld[2] == "x" and spielfeld[0] != "o":
            feld = 1
        elif spielfeld[3] == spielfeld[4] == "x" and spielfeld[5] != "o":
            feld = 6
        elif spielfeld[4] == spielfeld[5] == "x" and spielfeld[3] != "o":
            feld = 4
        elif spielfeld[6] == spielfeld[7] == "x" and spielfeld[8] != "o":
            feld = 9
        elif spielfeld[7] == spielfeld[8] == "x" and spielfeld[6] != "o":
            feld = 7
        elif spielfeld[0] == spielfeld[3] == "x" and spielfeld[6] != "o":
            feld = 7
        elif spielfeld[3] == spielfeld[6] == "x" and spielfeld[0] != "o":
            feld = 1
        elif spielfeld[1] == spielfeld[4] == "x" and spielfeld[7] != "o":
            feld = 8
        elif spielfeld[4] == spielfeld[7] == "x" and spielfeld[1] != "o":
            feld = 2
        elif spielfeld[2] == spielfeld[5] == "x" and spielfeld[8] != "o": 
            feld = 9                                
        elif spielfeld[5] == spielfeld[8] == "x" and spielfeld[2] != "o":   
            feld = 3
        elif spielfeld[0] == spielfeld[4] == "x" and spielfeld[8] != "o":
            feld = 9
        elif spielfeld[4] == spielfeld[8] == "x" and spielfeld[0] != "o":
            feld = 1
        elif spielfeld[2] == spielfeld[4] == "x" and spielfeld[6] != "o":
            feld = 7
        elif spielfeld[4] == spielfeld[6] == "x" and spielfeld[2] != "o": 
            feld = 3
        elif spielfeld[0] == spielfeld[2] == "x" and spielfeld[1] != "o": 
            feld = 2
        elif spielfeld[3] == spielfeld[5] == "x" and spielfeld[4] != "o": 
            feld = 5
        elif spielfeld[6] == spielfeld[8] == "x" and spielfeld[7] != "o": 
            feld = 8
        elif spielfeld[0] == spielfeld[6] == "x" and spielfeld[3] != "o": 
            feld = 4
        elif spielfeld[1] == spielfeld[7] == "x" and spielfeld[4] != "o": 
            feld = 5
        elif spielfeld[2] == spielfeld[8] == "x" and spielfeld[5] != "o": 
            feld = 6
        elif spielfeld[0] == spielfeld[8] == "x" and spielfeld[4] != "o": 
            feld = 5
        elif spielfeld[2] == spielfeld[6] == "x" and spielfeld[4] != "o": 
            feld = 5                               
        elif spielfeld[0] == spielfeld[1] == "o" and spielfeld[2] != "x":
            feld = 3
        elif spielfeld[1] == spielfeld[2] == "o" and spielfeld[0] != "x":
            feld = 1
        elif spielfeld[3] == spielfeld[4] == "o" and spielfeld[5] != "x":
            feld = 6
        elif spielfeld[4] == spielfeld[5] == "o" and spielfeld[3] != "x":
            feld = 4
        elif spielfeld[6] == spielfeld[7] == "o" and spielfeld[8] != "x":
            feld = 9
        elif spielfeld[7] == spielfeld[8] == "o" and spielfeld[6] != "x":
            feld = 7
        elif spielfeld[0] == spielfeld[3] == "o" and spielfeld[6] != "x":
            feld = 7
        elif spielfeld[3] == spielfeld[6] == "o" and spielfeld[0] != "x":
            feld = 1
        elif spielfeld[1] == spielfeld[4] == "o" and spielfeld[7] != "x":
            feld = 8
        elif spielfeld[4] == spielfeld[7] == "o" and spielfeld[1] != "x":
            feld = 2
        elif spielfeld[2] == spielfeld[5] == "o" and spielfeld[8] != "x": 
            feld = 9                                
        elif spielfeld[5] == spielfeld[8] == "o" and spielfeld[2] != "x":   
            feld = 3
        elif spielfeld[0] == spielfeld[4] == "o" and spielfeld[8] != "x":
            feld = 9
        elif spielfeld[4] == spielfeld[8] == "o" and spielfeld[0] != "x":
            feld = 1
        elif spielfeld[2] == spielfeld[4] == "o" and spielfeld[6] != "x":
            feld = 7
        elif spielfeld[4] == spielfeld[6] == "o" and spielfeld[2] != "x": 
            feld = 3
        elif spielfeld[0] == spielfeld[2] == "o" and spielfeld[1] != "x": 
            feld = 2
        elif spielfeld[3] == spielfeld[5] == "o" and spielfeld[4] != "x": 
            feld = 5
        elif spielfeld[6] == spielfeld[8] == "o" and spielfeld[7] != "x": 
            feld = 8
        elif spielfeld[0] == spielfeld[6] == "o" and spielfeld[3] != "x": 
            feld = 4
        elif spielfeld[1] == spielfeld[7] == "o" and spielfeld[4] != "x": 
            feld = 5
        elif spielfeld[2] == spielfeld[8] == "o" and spielfeld[5] != "x": 
            feld = 6
        elif spielfeld[0] == spielfeld[8] == "o" and spielfeld[4] != "x": 
            feld = 5
        elif spielfeld[2] == spielfeld[6] == "o" and spielfeld[4] != "x": 
            feld = 5                               
        elif spielfeld[0] == "x" and spielfeld[4] != "o":
            feld = 5  
        elif spielfeld[2] == "x" and spielfeld[4] != "o":  
            feld = 5
        elif spielfeld[6] == "x" and spielfeld[4] != "o":  
            feld = 5
        elif spielfeld[8] == "x" and spielfeld[4] != "o":
            feld = 5  
        elif spielfeld[4] == "x" and spielfeld[0] != "o":  
            feld = 1
        elif spielfeld[1] == "x" and spielfeld[4] != "o":  
            feld = 5
        elif spielfeld[3] == "x" and spielfeld[4] != "o":
            feld = 5  
        elif spielfeld[5] == "x" and spielfeld[4] != "o":  
            feld = 5
        elif spielfeld[7] == "x" and spielfeld[4] != "o":  
            feld = 5       

        else:
            while not gültige_eingabe:
                feld += 1
                if str(feld) in spielfeld and str(feld) != "x" and str(feld) != "o":
                    gültige_eingabe = True
        return feld        

arcade.run()