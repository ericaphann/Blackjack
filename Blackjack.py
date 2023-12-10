import random

    #Game Start
def GameStart():
    Player_Status = "None"
    Dealer_Status = "None"

    Player = True

    #Deck
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
    def Check21(Hand_Value):
        if Hand_Value == 21:
            print("You hit 21!")
            return True
        
    #Bet amount
    #need to fix bet system
    def Bet(amount):
         #Currency
        Player_Money = 100
        Pot_Total = 0 
        if (Player_Money - amount) >= 0:
            Player_Money = Player_Money - amount
            Pot_Total = Pot_Total + amount
        else:
            while True:
                print("You can't bet that amount or else you will go negative!")
                if (Player_Money - amount) >= 0:
                    Player_Money = Player_Money - amount
                    Pot_Total = Pot_Total + amount
                    break
        return Pot_Total 


    #Dealer Hand Start
    Dealer_Card = list(Random_Card())
    Dealer_Hand = Dealer_Card[2]
    #If dealer gets an Ace it will always be an 11 since it is the first card
    if Dealer_Card[0] == "A":
        Dealer_Card[2] = 11
    print("Dealer:",Dealer_Card[0], "of", Dealer_Card[1])

    #Player Hand
    Player_Hand = 0
    while Player == True:
        Name_Type_Value = list(Random_Card())
        Ace(Name_Type_Value)
        print("User:",Name_Type_Value[0], "of", Name_Type_Value[1])
        Player_Hand += Name_Type_Value[2]
        Bet_Amount = int(input("How much do you want to bet?"))
        print("Pot Total:", Bet(Bet_Amount))
        

        #If 21, stop
        if Check21(Player_Hand) == True:
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
                if Ask == "yes":
                    Player = True
                    break
                if Ask == "no":
                    Player = False 
                    break     

    #Dealer Hand End
    while Dealer_Hand < 16:
        Dealer_Card = list(Random_Card())
        #If the hand is small dealer will choose to make it worth 11
        if Dealer_Card[0] == "A":
            if (Dealer_Hand + 11) > 21:
                Dealer_Card[2] = 1
            else:
                Dealer_Card[2] = 11
        print("Dealer:",Dealer_Card[0], "of", Dealer_Card[1])
        Dealer_Hand += Dealer_Card[2]
    
    print("User Total:", Player_Hand)
    print("Dealer Total:", Dealer_Hand)
    BustCheck(Dealer_Hand)

    if Dealer_Hand > 21:
        Dealer_Status = "Bust"
        Player_Status = "Win"
    if Player_Hand > 21:
        Player_Status = "Bust"
        Dealer_Status = "Win"
    if Dealer_Hand > Player_Hand and Dealer_Hand <= 21:
        Dealer_Status = "Win"
        Player_Status = "Lose"
    if Player_Hand > Dealer_Hand and Player_Hand <= 21:
        Player_Status = "Win"
        Dealer_Status = "Lose"

    print("Dealer:", Dealer_Status)
    print("Player:", Player_Status)
            
GameStart()
