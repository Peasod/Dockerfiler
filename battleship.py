import numpy as np  
import random       #Importerar numpy och random. Random är en modul som generarar slumpmässiga nummer.
 
counter = 0
win_CPU = False
win_Player = False
used_NR = []           #Initerar variablerna som jag använder mig utav senare i koden. Använder mig av Global för att nå dessa.



def ship_Coordinates_Setup():
    x_Coords = int(input("Where do you want to place your ship?\nX-coordinate:"))
    y_Coords = int(input("Y-coordinate:"))
    angle = str.upper(input("H for Horizontal or V for Vertical: "))
    return x_Coords, y_Coords, angle            # Denna funktion tar hand om att fråga användaren efter värden och returnerar 3 variabler.

def meny ():

    opponent_Board_TEXT ="               Enemy Board                 \n _______________________________________  X\n|   |   |   |   |   |   |   |   |   |   | 1\n|   |   |   |   |   |   |   |   |   |   | 2\n|   |   |   |   |   |   |   |   |   |   | 3\n|   |   |   |   |   |   |   |   |   |   | 4\n|   |   |   |   |   |   |   |   |   |   | 5\n|   |   |   |   |   |   |   |   |   |   | 6\n|   |   |   |   |   |   |   |   |   |   | 7\n|   |   |   |   |   |   |   |   |   |   | 8\n|   |   |   |   |   |   |   |   |   |   | 9\n|___|___|___|___|___|___|___|___|___|___|10\nY 1   2   3   4   5   6   7   8   9  10      "
    player_Board_TEXT ="              Player Board                 \n _______________________________________  X\n|   |   |   |   |   |   |   |   |   |   | 1\n|   |   |   |   |   |   |   |   |   |   | 2\n|   |   |   |   |   |   |   |   |   |   | 3\n|   |   |   |   |   |   |   |   |   |   | 4\n|   |   |   |   |   |   |   |   |   |   | 5\n|   |   |   |   |   |   |   |   |   |   | 6\n|   |   |   |   |   |   |   |   |   |   | 7\n|   |   |   |   |   |   |   |   |   |   | 8\n|   |   |   |   |   |   |   |   |   |   | 9\n|___|___|___|___|___|___|___|___|___|___|10\nY 1   2   3   4   5   6   7   8   9  10      "
    reset_Opponent_Board_Text ="               Enemy Board                 \n _______________________________________  X\n|   |   |   |   |   |   |   |   |   |   | 1\n|   |   |   |   |   |   |   |   |   |   | 2\n|   |   |   |   |   |   |   |   |   |   | 3\n|   |   |   |   |   |   |   |   |   |   | 4\n|   |   |   |   |   |   |   |   |   |   | 5\n|   |   |   |   |   |   |   |   |   |   | 6\n|   |   |   |   |   |   |   |   |   |   | 7\n|   |   |   |   |   |   |   |   |   |   | 8\n|   |   |   |   |   |   |   |   |   |   | 9\n|___|___|___|___|___|___|___|___|___|___|10\nY 1   2   3   4   5   6   7   8   9  10      "
    reset_Player_Board_Text ="              Player Board                 \n _______________________________________  X\n|   |   |   |   |   |   |   |   |   |   | 1\n|   |   |   |   |   |   |   |   |   |   | 2\n|   |   |   |   |   |   |   |   |   |   | 3\n|   |   |   |   |   |   |   |   |   |   | 4\n|   |   |   |   |   |   |   |   |   |   | 5\n|   |   |   |   |   |   |   |   |   |   | 6\n|   |   |   |   |   |   |   |   |   |   | 7\n|   |   |   |   |   |   |   |   |   |   | 8\n|   |   |   |   |   |   |   |   |   |   | 9\n|___|___|___|___|___|___|___|___|___|___|10\nY 1   2   3   4   5   6   7   8   9  10      "
    # Dessa fin strängar används för att skriva ut bräden som användaren ser. Dessa ändras när datorn och/eller användaren har "skjutit".


    x = True
    while x == True :
        print("\n1 : Place Battleship\n2 : Place Warship\n3 : Place Gunship\n4 : Place Scoutship\n5 : Show Board\n6 : Save the players Board to file\n7 : Load opponent board from previous saves.\n8 : Show Opponents Board\n9 : Start Playing\n10 : Exit game")
        i = input()
        if i == "1":
            Battleship = battleship()
            Battleship.place_Ship()                 
        elif i == "2":
            warship1 = warship()
            warship1.place_Ship()
            warship2 = warship()
            warship2.place_Ship()                    

        elif i == "3":
            Gunship1 = gunship()
            Gunship1.place_Ship()
            Gunship2 = gunship()
            Gunship2.place_Ship()
            Gunship3 = gunship()
            Gunship3.place_Ship()                    

        elif i == "4":
            Scoutship1 = scoutship()
            Scoutship1.place_Ship()
            Scoutship2 = scoutship()
            Scoutship2.place_Ship()
            Scoutship3 = scoutship()
            Scoutship3.place_Ship()
            Scoutship4 = scoutship()
            Scoutship4.place_Ship()                  # Dessa variabler skapar skepp och placerar ut de efteråt.
        elif i == "5":            
            print(board)
        elif i == "6":
            save_Board_Setup(board)                   # Skickar användarens bräde till en funktion som skriver ner till .txt fil.
        elif i == "7":
            opponent_Board = make_Board(read_Board_Setup_From_File(), int(input("Which save? Enter Digit.\n")))     # Tar en input av användaren, skickar sedan det till en funktion använder siffran som indexering i txt dokument. Returnerar det värdet. Skapar en bräda av det värdet och sparar ner det i en variabel. Som används som motståndarens bräde.  
        elif i == "8":
            try:
                print(opponent_Board)       # Visar hur motståndarens bräde ser ut. Detta bör man se som en Gamemaster funktion i eventuella framtida verisioner , haha.
            except UnboundLocalError:           
                print("\nYou must create your opponets board before you can show it.")          # Trysatsen är felsäkerhet. Ifall variabeln opponent_Board ej har skapats än får man felmeddelande.
        elif i == "9":
            global counter
            counter = 0
            global win_CPU
            win_CPU = False
            global win_Player
            win_Player  = False
            global used_NR
            used_NR = []
            opponent_Board_TEXT = reset_Opponent_Board_Text
            player_Board_TEXT = reset_Player_Board_Text         # Då jag har använt mig av globala variabler i min lösning måste jag kunna nollställa dem, ifall jag vill köra igen utan att starta om programmet. Det gör jag här.

            while win_Player == False and win_CPU == False:
                
                print(opponent_Board_TEXT)
                print(player_Board_TEXT) 
                opponent_Board_TEXT = shoot(opponent_Board,opponent_Board_TEXT)
                if win_Player == True:
                    print(opponent_Board_TEXT)
                    print(player_Board_TEXT) 
                    break
                
                player_Board_TEXT = shoot_CPU(board,player_Board_TEXT)
                if win_CPU == True:
                    print(opponent_Board_TEXT)
                    print(player_Board_TEXT)                # Detta är det som kör tills en segrare har korats.

        elif i == "10":
            x = False           # Stänger av while loopen i meny() och därmed spelet.
        else:
            print("Incorrect input.\nTry again!")   # Skrivit fel enligt meny()s regeler ? Då får du meddelande.

# Meny funktionen som är navet i koden.

def save_Board_Setup(board_Setup): # Läser in alla elements värde ifrån numpyboarden(själva boarden där all info finns, till skillnad från output boarden som är för användaren.) och sparar det på en rad i en .txt fil. Konverterar allt till en lång sträng.
    board_Element = ""
    for element in board_Setup:
        board_Element+=(str(element))

    board_Element = board_Element.replace(" " , "")
    board_Element = board_Element.replace("[" , "")
    board_Element = board_Element.replace("]" , "")     
    board_Element += ("\n")                         # Tar bort oönskade tecken i min sträng som jag vill spara och lägger till ett newline tecken.

    with open("boardSetup.txt", "a") as my_file:
        my_file.writelines(board_Element)           # Skapar/appendar till boardSetup.txt filen. Tar man en rad så kan man skapa en ny board och slippa sätta in skepp styckvis. Detta sker i read_Board_Setup_From_File funktioen.



def read_Board_Setup_From_File():   # Sparar ner siffrorna från boardSetup filen ner till en integerslista. För att detta sedan ska packas upp med en ny funktion och skapa ny numpy bräda. 

    setup_List = []

    with open("boardSetup.txt", "r") as my_file:
        for element in my_file:
            fixed_Str = str(element)
            fixed_Str = fixed_Str.replace("\n", "")
            setup_List.append(fixed_Str)
        
    return setup_List       # Läser boardSetup.txt och tar varje element/siffra och lägger in det i en lång lista som sedan skickas vidare och kan användas.



def make_Board(board_Setup_List, place):    # Denna tar en sträng lista och en siffra som in argument. För att sedan skapa en numpy spelbräda av den och skickar det i returnen.
    
    board = str(board_Setup_List[place])    # Skapar en lång sträng av en lista som skicaks från read_Board_Setup_From_File().

    new_Board = np.ones([10,10], dtype=int)
    counter_X_pos = 0
    counter_Y_pos = 0 

    for digit in board:

        new_Board[counter_X_pos,counter_Y_pos] = int(digit)

        if counter_Y_pos == 9:
            counter_Y_pos = 0
            counter_X_pos += 1
        else:
            counter_Y_pos += 1
        
                                        # går igenom strängen och sätter ut värden på en numpylista. 
    return new_Board        # Returnear en ny numpy lista.

def shoot(opponent_Board,opponent_Board_TEXT):        # Denna gör så att spelaren skjuter, träffar man så byter man värdet på koordinaten till en 0a.Tar in både numpylistan och motståndarens textbärdspelsplan.
    hit = True
    local_opponent_Board_TEXT = opponent_Board_TEXT
    global win_Player

    while hit == True:  # Träffar man får man försöka en gång till.
        try:
            shot_X_coord = int(input("***Aiming***\nX cordinate: "))
            shot_Y_coord = int(input("Y cordinate: "))
        
        except ValueError:          # Säkerhet, ifall man skriver in fel värde eller inget alls så körs loopen om utan att ändra något viktigt värde.
            print("That is not an interger value. Retry.")
            continue
        
        if shot_X_coord == 0 or shot_X_coord > 10 or shot_Y_coord == 0 or shot_Y_coord > 10:        # Detta skall lydas för att skottet ska vara giltigt.

            print("Coordinates is out of battlefield.")
             
        elif opponent_Board[shot_X_coord -1, shot_Y_coord - 1] > 0:             # När indexet i numpylistan har ett värde större än 0, så har du träffat ett skepp och efterföljande sats sker.

            print(f"\nFireing at coordinates {shot_X_coord}:{shot_Y_coord}!\n")
            print("HIT!\n")
            opponent_Board[shot_X_coord - 1,shot_Y_coord - 1] = 0                       # Värdet på platsen ändras till noll.
            round_Counter()     # En runda har registrerats och värdet på en variabel ökas.
            local_opponent_Board_TEXT = opponent_Board_Output(local_opponent_Board_TEXT,shot_X_coord,shot_Y_coord, hit) # Det sätts ut en specifikmarkör på motståndarens spelplan med hjälp av opponent_Board_Output() funktionen.

            if opponent_Board.sum() == 0:       # Om det totala värdet på motståndarens bräda är 0 så betyder det att alla skepp är förstörda/träffade och spelaren har iomed det vunnit.

                print("Congratulation!\nYou have won!")
                win_Player = True
                add_statistic(True, counter)        # Denna gör att det sparas statistik till en fil, med vem som vann och på hur många rundor.
                hit = False     # avbryter while loopen. skulle kunna använda break.
           
        else:

            print(f"\nFireing at coordinates {shot_X_coord}:{shot_Y_coord}!")
            print("Miss.\n")
            round_Counter()
            hit = False
            local_opponent_Board_TEXT = opponent_Board_Output(local_opponent_Board_TEXT,shot_X_coord,shot_Y_coord, hit)     # Ett skott som ej träffade, då går rundcountern upp och motståndarens bärdutskrift uppdateras.
            
    return local_opponent_Board_TEXT    # Returnerar uppdaterat bräde



def shoot_CPU(player_board,player_Board_TEXT):    # Denna metod har hand om CPUns skott.
    hit = True
    local_player_Board_TEXT = player_Board_TEXT
    global win_CPU
    while hit == True:  # Träffar datorn så dår den skjuta igen.
        shot_X_coord_CPU = random.randint(0,9)
        shot_Y_coord_CPU = random.randint(0,9)      # Här genereras två slumpmässiga tal enligt en angiven intervall.

        if list_Of_CPUs_Shots(shot_X_coord_CPU,shot_Y_coord_CPU) == False:      # De två talen skickas till en metod som ser om dessa har skjutits innan. Har det gjort det så kör loopen om till det är två tal som ej har används förut.
            continue

        if player_board[shot_X_coord_CPU, shot_Y_coord_CPU] > 0:
            print(f"Opponent Fireing at coordinates {shot_X_coord_CPU + 1}:{shot_Y_coord_CPU + 1}!\n")
            print("HIT!\n")
            player_board[shot_X_coord_CPU,shot_Y_coord_CPU] = 0
            round_Counter()
            local_player_Board_TEXT = player_Board_Output(local_player_Board_TEXT,shot_X_coord_CPU,shot_Y_coord_CPU, hit)   

            if player_board.sum() == 0:
                hit = False
                win_CPU = True
                add_statistic(False, counter)
                print("OPPONENT HAVE WON THE GAME.\n\nGAME OVER")

        else:
            print(f"Opponent Fireing at coordinates {shot_X_coord_CPU + 1}:{shot_Y_coord_CPU + 1}!\n")
            print("Miss.\n") 
            round_Counter()
            hit = False
            local_player_Board_TEXT = player_Board_Output(local_player_Board_TEXT,shot_X_coord_CPU,shot_Y_coord_CPU, hit)   # Dessa 3 stycken fungerar som deras motsvarighet i shoot(), fast lite modifiering på datorns koordinater i utskriften. 

    return local_player_Board_TEXT
    
def list_Of_CPUs_Shots(shot_X_coord_CPU,shot_Y_coord_CPU):  # Denna funktion kontrollerar att datorns skott ej används 2 gånger.
    global used_NR      # listan som sparar datorns använda skott
    x_Shot = str(shot_X_coord_CPU)
    y_Shot = str(shot_Y_coord_CPU)
    value = x_Shot + y_Shot # Använder mig av strängar för att jämföra. om jag skulle använda mig utav ints så skulle det inte gå. 5+6 och 6+5 är ju inte samma i battleships sammanhang.
    switch = 0
    for element in used_NR: # gå igenom varje element i listan

        if value == element:        # jämför så att value(nya skottet) inte matchar med något element i listan.
            print(f"Varvet value av x å y shot:{value}\nMatchar med elementet: {element} ifrån usedNR listan") 
            switch = 1  

    if switch == 1: 
        return False
    else:
        used_NR.append(value)
        return True     # Returnerar olika beroende på ifall den finns eller ej. Finns den inte i listan läggs value in i listan.



def round_Counter():    # Metod som används när en korrekt runda/skott är gjort. För att få fram rundorna till statestik.
    global counter
    counter += 1

def add_statistic(player_Result, rounds_stat):  # Skriver till fil med vem som har vunnit och hur många rundor det tog.

        if player_Result == True:
            with open("BattleshipStatistics.txt", "a") as my_file:       
                    my_file.writelines(f"Player won in {rounds_stat} rounds.\n") 
        else:
            with open("BattleshipStatistics.txt", "a") as my_file:
                my_file.writelines(f"Computer won in {rounds_stat} rounds.\n") 

def opponent_Board_Output(current_Board, x_Kord_Shot, y_Kord_Shot,hit): # Denna funktion används för att manipulera det motståndarens synliga bräde.
    
    refined_X_shot_Value = (x_Kord_Shot - 1) * 44 + 90
    refined_Shot_Value = refined_X_shot_Value + (4 * (y_Kord_Shot - 1))     

    if hit == True:
        updated_Board = current_Board[:refined_Shot_Value] + "X" + current_Board[(refined_Shot_Value + 1):]
    else:
        updated_Board = current_Board[:refined_Shot_Value] + "O" + current_Board[(refined_Shot_Value + 1):]     # Sträng manipulering. Sätter in ett X ifall hit är true. Hit är true om man har träffat. Google ledde mig till stackoverflow som hjälpte mig här. Visste att det gick ifrån våra lektioner.

    return updated_Board    # Returnerar det updaterade brädet.

def player_Board_Output(current_Board, x_Kord_Shot, y_Kord_Shot,hit):
    
    refined_X_shot_Value = x_Kord_Shot * 44 + 90
    refined_Shot_Value = refined_X_shot_Value + (4 * y_Kord_Shot)

    if hit == True:
        updated_Board = current_Board[:refined_Shot_Value] + "X" + current_Board[(refined_Shot_Value + 1):]
    else:
        updated_Board = current_Board[:refined_Shot_Value] + "O" + current_Board[(refined_Shot_Value + 1):]

    return updated_Board        # Lika som funktionen ovan men andra brädet en siffra min för kalibrering.

class ship:     # Super klassen skepp, vilka alla skepp subklasser ärver metoder av. 
        
    def __init__(self):             # Initierar med hjälp av en funktion. 
        stats = ship_Coordinates_Setup()
        self.ship_X_Coordinates = stats[0]
        self.ship_Y_Coordinates = stats[1]
        self.ship_Angle = stats[2]

    def check_Board_Placement_Sum(self,ship_X_Coordinates, ship_Y_Coordinates, angle, ship_size):    # Metod för att avgöra om placeringen är ok enligt spelets regler. I numpy matrisen får inget angränsade värde vara > 0. 

        x_Coords = ship_X_Coordinates
        y_Coords = ship_Y_Coordinates
        sum_Buffer = 0                      # Sparar inskickade variablar

        if angle == "H" and x_Coords == 0 and y_Coords == 0:    # Kikar om skeppets placering är på koordinat 0:0, kikar angränsade "celler" som är inom brädets index.

            for cell in range(ship_size):

                sum_Buffer += board[ x_Coords: x_Coords + 2 , y_Coords : y_Coords + 2 ].sum()
                y_Coords += 1

        elif angle == "V" and x_Coords == 0 and y_Coords == 0 : # Angle V står för Vertical och H för Horizontal

            for cell in range(ship_size):   # Varje skepp subclass har sin egna skepplängd och den används med shipsize beronede på ifrån vilken subklass anropet kommer ifrån.

                sum_Buffer += board[ x_Coords : x_Coords + 2 , y_Coords : y_Coords + 2 ].sum()  # Kikar på angränsande celler värde och adderar det till variabel. 
                x_Coords += 1

        elif angle == "H":  # Är angel H så gäller följande. (Ifall övre värden ej har stämt.)

            if x_Coords == 0:               # Om koordinaterna är 0 och angle är H så vill skeppet placeras längst upp och då ska inte programet föröska räkna på celler som är över(för det finns inga och det skulle bli fel).
                for cell in range(ship_size):   
                    
                    sum_Buffer += board[ x_Coords : x_Coords + 2, y_Coords - 1 : y_Coords + 2 ].sum()
                    y_Coords += 1

            else:  

                for cell in range(ship_size):   
    
                    sum_Buffer += board[ x_Coords - 1: x_Coords + 2, y_Coords - 1 : y_Coords + 2 ].sum()
                    y_Coords += 1

        elif angle == "V": 

            if y_Coords == 0:   # Om koordinaterna är 0 och angle är V så vill skeppet placeras längst till höger och då ska inte programet föröska räkna på celler som är längre till höger(för det finns inga och det skulle bli fel).
                for cell in range(ship_size):   
                    
                    sum_Buffer += board[ x_Coords - 1: x_Coords + 2, y_Coords : y_Coords + 2 ].sum()
                    x_Coords += 1

            else:    
                for cell in range(ship_size):   
                    
                    sum_Buffer += board[ x_Coords - 1: x_Coords + 2, y_Coords - 1 : y_Coords + 2 ].sum()
                    x_Coords += 1

        if sum_Buffer == 0:
            return True
        else:
            return False    # När metoden har kikat numpybrädets angränsade platser(och även där skeppet vill vara), så kommer det hit. Har det funnits något värde i någon ruta så har det sparats i sum_Buffer och är därmed != 0. returneras False så nekas önskad plats.
        
class battleship(ship):
    
    ship_Size = 4   # Detta värde är unikt för varje subklass av ship.

    def __init__(self):
        super().__init__()      # Ärver superklassens konstruktor. detta görs medhjälp av super()



    def place_Ship(self):
        cBPS = self.check_Board_Placement_Sum(self.ship_X_Coordinates,self.ship_Y_Coordinates,self.ship_Angle,self.ship_Size)  # Skickar det specifika värdet som ett skapat battleship har. Skapar man Battleship1 = battleship(), så är det inte samma värde man skickar om man skapar en Battleship2 på samma sett tack vare "self"
        if cBPS == True:                # Är detta sant så har check_Board_Placement_Sum() returnerat True och därmed är placeringen giltig och inte upptagen!
            if self.ship_Angle == "H" and self.ship_Y_Coordinates <= 6 :            
                board[self.ship_X_Coordinates, self.ship_Y_Coordinates:(self.ship_Y_Coordinates + 4)] = 4
                    
            elif self.ship_Angle == "V" and self.ship_X_Coordinates <= 6 :  # 6 har kontollerar att skeppet inte försöks sättas utan för spelplanen. 
                board[self.ship_X_Coordinates:(self.ship_X_Coordinates + 4),self.ship_Y_Coordinates] = 4
            else:
                print("The ship will be placed out of bounds. Try again.")            
        else:
            print("This space is occupied.\nTry again.")

class warship(ship):    # Fungerar som battleship fast med andra värden.

    ship_Size = 3

    def __init__(self):
        super().__init__()

    def place_Ship(self):

        cBPS = self.check_Board_Placement_Sum(self.ship_X_Coordinates,self.ship_Y_Coordinates,self.ship_Angle,self.ship_Size)
        if cBPS == True:
            if self.ship_Angle == "H" and self.ship_Y_Coordinates <= 7 :
                board[self.ship_X_Coordinates, self.ship_Y_Coordinates:(self.ship_Y_Coordinates + 3)] = 3
                    
            elif self.ship_Angle == "V" and self.ship_X_Coordinates <= 7 :
                board[self.ship_X_Coordinates:(self.ship_X_Coordinates + 3),self.ship_Y_Coordinates] = 3    
            else:
                print("The ship will be placed out of bounds. Try again.")        
        else:
            print("This space is occupied or illegal placement.\nTry again.")

class gunship(ship):    # Fungerar som battleship fast med andra värden.

    ship_Size = 2

    def __init__(self):
        super().__init__()

    def place_Ship(self):

        cBPS = self.check_Board_Placement_Sum(self.ship_X_Coordinates,self.ship_Y_Coordinates,self.ship_Angle,self.ship_Size)
        if cBPS == True:
            if self.ship_Angle == "H" and self.ship_Y_Coordinates <= 8 :
                board[self.ship_X_Coordinates, self.ship_Y_Coordinates:(self.ship_Y_Coordinates + 2)] = 2
                    
            elif self.ship_Angle == "V" and self.ship_X_Coordinates <= 8 :
                board[self.ship_X_Coordinates:(self.ship_X_Coordinates + 2),self.ship_Y_Coordinates] = 2
            else:
                print("The ship will be placed out of bounds. Try again.")                            
        else:
            print("This space is occupied or illegal placement.\nTry again.")
        
class scoutship(ship):  # Fungerar som battleship fast med andra värden.

    ship_Size = 1


    def __init__(self):
        super().__init__()
 
    def place_Ship(self):
        cBPS = self.check_Board_Placement_Sum(self.ship_X_Coordinates,self.ship_Y_Coordinates,self.ship_Angle,self.ship_Size)
        if cBPS == True:
            if (self.ship_X_Coordinates <= 9 and self.ship_X_Coordinates  >= 0) and (self.ship_Y_Coordinates <= 9 and self.ship_Y_Coordinates >= 0) :            
                board[self.ship_X_Coordinates,self.ship_Y_Coordinates] = 1
            else:
                print("The ship will be placed out of bounds. Try again.")

        else:
                print("This space is occupied or illegal placement.\nTry again.")


if input("New board or Load board? N/L\n") == "N":          
    board = np.zeros([10,10], dtype=int)    # Första prompt ifall man vill skapa ny eller ladda ett bräde.

else:
    board = make_Board(read_Board_Setup_From_File(), int(input("Which save? Enter Digit.\n")))  # Laddar ett bräde med kombinerad hjälp av funktioner. Inputvärde syftar på en rad i boardSetup.txt filen.

meny()  # Startar meny funktionen. Navet. 

