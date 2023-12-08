import random

    #Game Start
def GameStart():
    Player = True

    Cards = {"A": [11,1], "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}

    Card_Names = list(Cards.keys())
    Card_Types = ["Hearts", "Clubs", "Diamonds", "Spades"]

    #Random Card Generator
    def Random_Card():
        #Random Number
        Random_Value = random.randint(0,12)
        #Value
        Random_Card_Value = Cards[Card_Names[Random_Value]]
        #Key/Name
        Random_Card_Name = Card_Names[Random_Value]
        Random_Card_Type = Card_Types[random.randint(0,3)]
        return Random_Card_Name,Random_Card_Type, Random_Card_Value

    def Ace(Hand):
        if Hand[0] == "A":
            while True:
                One_11 = str(input("You landed on an Ace! Do you want it to be worth 1 or 11?"))
                if One_11 == "1":
                    Name_Type_Value[2] = 1
                    break
                elif One_11 == "11":
                    Name_Type_Value[2] = 11
                    break
                else:
                    print("Try Again! Type 1 or 11")

    #Checks if the hand is a bust or not
    def BustCheck(Hand):
        if Hand > 21:
            print("Bust!")
            return True
    
    #Check if hand is 21
    def WinCheck(Hand_Value):
        if Hand_Value == 21:
            print("You hit 21!")
            return True

    #Dealer Hand

    Dealer_Card = list(Random_Card())
    Dealer_Hand = Dealer_Card[2]
    print("Dealer:",Dealer_Card[0], "of", Dealer_Card[1])

    #Player Hand
    Player_Hand = 0
    while Player == True:
        Name_Type_Value = list(Random_Card())
        Ace(Name_Type_Value)
        print("User:",Name_Type_Value[0], "of", Name_Type_Value[1])
        Player_Hand += Name_Type_Value[2]

        #If 21, stop
        if WinCheck(Player_Hand) == True:
            break
        #If bust, stop
        if BustCheck(Player_Hand) == True:
            break

        #Asking the user if they want to hit or not
        Ask = input("Do you want to hit?").lower()
        if Ask == "yes":
            Player = True
        elif Ask == "no":
            Player = False
        else:
            
            while True:
                Ask = input("That is not an option, try again")
                if Ask == "Yes":
                    Player = True
                    break
                if Ask == "No":
                    Player = False 
                    break     
            
GameStart()
