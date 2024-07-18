'''
Patch notes:
V1.0
- Functioning version of the game
V1.1
- Introduced instruction manual
- Introduced replay ability
V1.2
- Introduced stacking non-special cards
V1.3
- Introduced choice turn order
- Introduced 4 of a kind discard rule
V1.4
- Bug fixes
  * Fixed random errors
  * Fixed saying no to playing multiple cards
- Allowed card to return to hand when played from palace
- Fixed instruction dimensions to fit wide screen
  * Wide screen meaning files tab closed and console size dragged to line
- Added postgame printout, showing what everything has at the end
V1.5
- Revamped instructions, no longer shoddy
  * Still kinda shoddy, just ignore it though
- Yeah thats it
V1.6
- Most inputs are no longer case sensitive
  * Makes it easier to play with capslock on, or with capslock offN

FURTHER NOTES:
This is an unfinished project. This is a working build, but there is some trouble with allowing opponent
to go first, and the tutorial/instructions are shoddy and dont teach you how to play well enough.
Used to require exact syntax, now just make sure you type the right letters/numbers, ignore case.
Good luck with this, I probably wont be changing it much more though.
'''


import random
from time import sleep

if (input("Would you like to read the instructions? (y/n): ")).lower() == "y":
    print("This program simulates the card game known as Palace. In this specific program, ")
    print("the special action cards are 2 and 10, and the 4-of-a-kind rule is active. more about those ")
    print("specific rules are introduced later. Now for the rules of play.")
    print("Rules of play: ")
    print("The game begins with each player recieving 3 random cards facedown, which are placed in front ")
    print("of them. The program does this automatically for you. Then, each player recieves 10 cards ")
    print("to make up their hand. Each player then chooses 3 of the cards from their hand, one at a ")
    print("time, to place faceup ontop of their 3 facedown cards. The hands remain hidden at all times ")
    print("from the other player, unless a card from said hand is played into the game. Gameplay then ")
    print("begins, as each player takes turns to play one or more cards from their hands or cards laid ")
    print("in front of them, onto a common pile in between the two players. Each time it is someones turn, ")
    print("they choose a valid card from their hand to play. A valid card is a card that is of equal or ")
    print("greater value than the card currently in the pile. For instance, a Jack has a higher value than ")
    print("a four, so that would be a valid card to play. If a player has no valid cards or chooses not to ")
    print("play a valid card, they must pick up the pile into their hand, and play continues from the next ")
    print("player. If a player has multiple cards in their hand all of the same value, they can all be ")
    print("played at once, in a stacking fashion. This method is not available when playing from the cards ")
    print("laid in front of you (refered to as the palace). Once cards are played, it is the other players ")
    print("turn to do the same. At the end of someones turn, if they have less than 3 cards in their hand, ")
    print("they must pick up cards from the facedown draw pile to bring their hand to 3 cards. If there are ")
    print("no cards to draw, no cards will be drawn and play continues. Once a players hand is all played and ")
    print("there are no cards to draw, on their next turn they will use one card from the top of their palace ")
    print("to play. The requirements for a card to be played are still active. Once all the faceup cards of ")
    print("the palace are played, a player may play from the facedown cards on their palace. When a player ")
    print("attempts to do so, they will draw a card at random and play it regardless of if it can be played. ")
    print("If it violates the rules of play, the player must pick up the pile. Once all of a players cards are ")
    print("gone, they win. Special cards include the 10 and 2, and they can be played regardless of their value. ")
    print("A 10 when played removes the entire pile from play, placing it into discard. A 2 when played, allows ")
    print("the player who played it to take another turn, playing another card. The four-of-a-kind rule means that ")
    print("if all four of any single value of card is in play at any given point, the entire pile is sent to discard.")
    print("The computer parts: ")
    print("As this is a computer game made by a 16 year old, it requires specific syntax to play properly. When ")
    print("asked to choose a card, you must give the exact format used ingame. The format is as follows: ")
    print("A card (such as the ace of spades) is refered to by the first letter of its suit (S for spade) and then ")
    print("the value of the card (A for ace). All letters must be capitalized if possible. The suits are ")
    print("S for spade, C for clubs, D for diamonds, and H for hearts. For values, number represent all values ")
    print("except in the cases of A for ace, X for 10, J for jack, Q for queen, and K for king. ")
    print("Avoid unecessarily typing or pressing enter when possible, as it may cause an error. Avoid taking to long ")
    print("when prompted to enter something, as it may cause an error. This is still not completely cleaned up, ")
    print("so there may still be some bugs. This is just a pet project so dont necessarily expect me to fix every ")
    print("little bug someone finds, and if anythinog someone else will just have to make a copy of the code and fix ")
    print("it themselves. Thats really all there is to it. When prompted to type a response other than a card, use ")
    print("the exact words given. Anyway, good luck in your game. You may need it depending on how good a mood my ")
    print("opponent AI is.")
    sleep(8)
    input("Press enter to continue")
    
    
replay = True
while replay == True:
    replay = False
    
    wheatlys_solution = [True, False]
    
    to_play = input("Who goes first? (player, opponent, random): ")
    if to_play.lower() == "player":
        player_goes = True
    elif to_play.lower() == "opponent":
        player_goes = False
    else:
        player_goes = random.choice(wheatlys_solution)
    
    
    cards = {"deck":["SA","S2","S3","S4","S5","S6","S7","S8","S9","SX","SJ","SQ","SK","CA","C2","C3","C4","C5","C6","C7","C8","C9","CX","CJ","CQ","CK","DA","D2","D3","D4","D5","D6","D7","D8","D9","DX","DJ","DQ","DK","HA","H2","H3","H4","H5","H6","H7","H8","H9","HX","HJ","HQ","HK"],
    "player":[], "playerdown":[], "playerup":[], "computer":[], "computerdown":[], "computerup":[], "pile":[], "discard":[]}
    
    '''
    # dummy deck for testing
    cards = {"deck":["SA"],
    "player":[], "playerdown":[], "playerup":[], "computer":[], "computerdown":[], "computerup":[], "pile":[], "discard":[]}
    '''
    
    def give_from_deck(key):
        cards[key].append(cards["deck"].pop(random.randint(0, len(cards["deck"]) - 1 )))
    
    def give_from_other_rand(key, other):
        cards[key].append(cards[other].pop(random.randint(0, len(cards[other]) - 1 )))
    
    def give_from_other_choice(key, other, choice):
        cards[key].append(cards[other].pop(choice))
    
    # Setup below, disable for custom starting positions
    setup = True
    if setup == True:
        for i in range(3):
            give_from_deck("playerdown")
            give_from_deck("computerdown")
        for i in range(10):
            give_from_deck("player")
            give_from_deck("computer")
        highcards = ["SA", "CA", "DA", "HA", "SX", "CX", "DX", "HX", "SK", "CK", "DK", "HK", "S2", "C2", "D2", "H2", "SQ", "CQ", "DQ", "HQ", "SJ", "CJ", "DJ", "HJ", "S9", "C9", "D9", "H9", "S8", "C8", "D8", "H8", "S7", "C7", "D7", "H7", "S6", "C6", "D6", "H6", "S5", "C5", "D5", "H5", "S4", "C4", "D4", "H4", "S3", "C3", "D3", "H3"]
        while len(cards["computerup"]) < 3:
            try:
                index = cards["computer"].index(highcards.pop(0))
                give_from_other_choice("computerup", "computer", index)
            except ValueError:
                # Ma-i-a hi
                # Ma-i-a hu
                # Ma-i-a ho
                # Ma-i-a ha-ha
                1 != 2
        for i in range(3):
            print(cards["player"])
            index = cards["player"].index((input("Pick which card to put on top of your palace: ")).upper())
            give_from_other_choice("playerup", "player", index)
    
    def read_table():
        print("---------------Current Table---------------")
        print("Cards remaining in the deck: " + str(len(cards["deck"])))
        print("Cards in the pile: " + str(len(cards["pile"])))
        print("Cards in discard: " + str(len(cards["discard"])))
        if len(cards["player"]) > 0:
            print("Your hand: " + str(cards["player"]))
        print("Your hand size: " + str(len(cards["player"])))
        print("Opponent hand size: " + str(len(cards["computer"])))
        if len(cards["playerup"]) != 0:
            print("Your faceup cards: " + str(cards["playerup"]))
        else:
            print("Your facedown cards left: " + str(len(cards["playerdown"])))
        if len(cards["computerup"]) != 0:
            print("Opponent's faceup cards: " + str(cards["computerup"]))
        else:
            print("Opponent's facedown cards left: " + str(len(cards["computerdown"])))
        try:
            print("Current card in the pile: " + str(cards["pile"][-1]))
        except IndexError:
            print("Pile is currently empty")
        print("-------------------------------------------")
    
    def evaluate(choice_value):
        if choice_value == "A":
            choice_value = 14
        elif choice_value == "K":
            choice_value = 13
        elif choice_value == "Q":
            choice_value = 12
        elif choice_value == "J":
            choice_value = 11
        elif choice_value == "X":
            choice_value = 10
        elif choice_value == "2":
            choice_value = 2
        else:
            choice_value = int(choice_value)
        return choice_value
    
    def player_play_card():
        choice = 0
        while choice == 0:
            try:
                choice = input("Play which card? ")
                choice = choice.upper()
                cards["player"].index(choice)
            except ValueError:
                print("You do not have this cards!")
                choice = 0
        choice_value = list(choice)[-1]
        choice_value = evaluate(choice_value)
        if choice_value == 10 or choice_value == 2:
            if choice_value == 10:
                print("You played " + choice + " onto the pile")
                give_from_other_choice("pile", "player", cards["player"].index(choice))
                print("Since it was a ten, the pile goes into discard!")
                print("Moved " + str(len(cards["pile"])) + " cards into discard!")
                for i in range(len(cards["pile"])):
                    give_from_other_rand("discard", "pile")
            elif choice_value == 2:
                print("You played " + choice + " onto the pile")
                give_from_other_choice("pile", "player", cards["player"].index(choice))
                sleep(1)
                print("Since it was a two, you go again!")
                sleep(1)
                return "steamedhams"
        else:
            if len(cards["pile"]) != 0:
                pile_value = list(cards["pile"][-1])[-1]
                pile_value = evaluate(pile_value)
            else:
                pile_value = 0
            if choice_value < pile_value:
                print("Unable to play this card!")
                print("You took " + str(len(cards["pile"])) + " cards from the pile!")
                for i in range(len(cards["pile"])):
                    give_from_other_rand("player", "pile")
            else:
                print("You played " + choice + " onto the pile")
                give_from_other_choice("pile", "player", cards["player"].index(choice))
                sleep(1)
                for value in cards["player"]:
                    if evaluate(list(value)[-1]) == choice_value:
                        double = input("You have another card of the same value. Would you like to play " + str(value) + "? (y/n)")
                        if double.lower() == "y":
                            give_from_other_choice("pile", "player", cards["player"].index(value))
                        else:
                            return
                for value in cards["player"]:
                    if evaluate(list(value)[-1]) == choice_value:
                        double = input("You have another card of the same value. Would you like to play " + str(value) + "? (y/n)")
                        if double.lower() == "y":
                            give_from_other_choice("pile", "player", cards["player"].index(value))
                        else:
                            return
                for value in cards["player"]:
                    if evaluate(list(value)[-1]) == choice_value:
                        double = input("You have another card of the same value. Would you like to play " + str(value) + "? (y/n)")
                        if double.lower() == "y":
                            give_from_other_choice("pile", "player", cards["player"].index(value))
                        else:
                            return
                for value in cards["player"]:
                    if evaluate(list(value)[-1]) == choice_value:
                        double = input("You have another card of the same value. Would you like to play " + str(value) + "? (y/n)")
                        if double.lower() == "y":
                            give_from_other_choice("pile", "player", cards["player"].index(value))
                        else:
                            return
    
    def player_play_palace():
        choice = 0
        while choice == 0:
            try:
                choice = input("Play which card? ")
                choice = choice.upper()
                cards["playerup"].index(choice)
            except ValueError:
                print("You do not have this cards!")
                choice = 0
        choice_value = list(choice)[-1]
        choice_value = evaluate(choice_value)
        if choice_value == 10 or choice_value == 2:
            if choice_value == 10:
                print("You played " + choice + " onto the pile")
                give_from_other_choice("pile", "playerup", cards["playerup"].index(choice))
                print("Since it was a ten, the pile goes into discard!")
                print("Moved " + str(len(cards["pile"])) + " cards into discard!")
                for i in range(len(cards["pile"])):
                    give_from_other_rand("discard", "pile")
            elif choice_value == 2:
                print("You played " + choice + " onto the pile")
                give_from_other_choice("pile", "playerup", cards["playerup"].index(choice))
                sleep(1)
                print("Since it was a two, you go again!")
                sleep(1)
                return "steamedhams"
        else:
            if len(cards["pile"]) != 0:
                pile_value = list(cards["pile"][-1])[-1]
                pile_value = evaluate(pile_value)
            else:
                pile_value = 0
            if choice_value < pile_value:
                print("Unable to play this card!")
                print("You took " + str(len(cards["pile"])) + " cards from the pile!")
                give_from_other_choice("player", "playerup", cards["playerup"].index(choice))
                for i in range(len(cards["pile"])):
                    give_from_other_rand("player", "pile")
            else:
                print("You played " + choice + " onto the pile")
                give_from_other_choice("pile", "playerup", cards["playerup"].index(choice))
    
    def player_play_bottom():
        choice = 0
        while choice == 0:
            try:
                if len(cards["playerdown"]) == 3:
                    choice = int(input("Play which down card? (1,2,3) "))
                    cards["playerdown"][choice - 1]
                elif len(cards["playerdown"]) == 2:
                    choice = int(input("Play which down card? (1,2) "))
                    cards["playerdown"][choice - 1]
                elif len(cards["playerdown"]) == 1:
                    choice = int(input("Play which down card? (1) "))
                    cards["playerdown"][choice - 1]
            except (ValueError, IndexError) as err:
                print("The number must be of a card you have!")
                choice = 0
        choice = cards["playerdown"][choice - 1]
        choice_value = list(choice)[-1]
        choice_value = evaluate(choice_value)
        if choice_value == 10 or choice_value == 2:
            print("You flipped over...")
            sleep(5)
            print(str(choice) + "!")
            sleep(2)
            if choice_value == 10:
                print("You played " + choice + " onto the pile")
                give_from_other_choice("pile", "playerdown", cards["playerdown"].index(choice))
                print("Since it was a ten, the pile goes into discard!")
                print("Moved " + str(len(cards["pile"])) + " cards into discard!")
                for i in range(len(cards["pile"])):
                    give_from_other_rand("discard", "pile")
            elif choice_value == 2:
                print("You played " + choice + " onto the pile")
                give_from_other_choice("pile", "playerdown", cards["playerdown"].index(choice))
                sleep(1)
                print("Since it was a two, you go again!")
                sleep(1)
                return "steamedhams"
        else:
            if len(cards["pile"]) != 0:
                pile_value = list(cards["pile"][-1])[-1]
                pile_value = evaluate(pile_value)
            else:
                pile_value = 0
            if choice_value < pile_value:
                print("You flipped over...")
                sleep(5)
                print(str(choice) + "!")
                sleep(2)
                give_from_other_choice("pile", "playerdown", cards["playerdown"].index(choice))
                print("But you are unable to play this card!")
                print("You took " + str(len(cards["pile"])) + " cards from the pile!")
                for i in range(len(cards["pile"])):
                    give_from_other_rand("player", "pile")
            else:
                print("You flipped over...")
                sleep(5)
                print(str(choice) + "!")
                sleep(2)
                print("You played " + choice + " onto the pile!")
                give_from_other_choice("pile", "playerdown", cards["playerdown"].index(choice))
    
    
    def opponent_play_card():
        # hoo boy this is gonna be a lot of "artificial intelligence"
        # AKA 50 million nested if statements
        if len(cards["pile"]) != 0:
            pile_value = list(cards["pile"][-1])[-1]
            pile_value = evaluate(pile_value)
        else:
            pile_value = 0
        for i in range(15):
            for value in cards["computer"]:
                choice_value = list(value)[-1]
                choice_value = evaluate(choice_value)
                if choice_value == pile_value + i and choice_value != 10 and choice_value != 2:
                    print("Opponent played " + value + " onto the pile")
                    sleep(1)
                    give_from_other_choice("pile", "computer", cards["computer"].index(value))
                    for value in cards["computer"]:
                        if evaluate(list(value)[-1]) == choice_value:
                            give_from_other_choice("pile", "computer", cards["computer"].index(value))
                            print("Opponent also had a " + str(value) + ", so they played that as well!")
                    for value in cards["computer"]:
                        if evaluate(list(value)[-1]) == choice_value:
                            give_from_other_choice("pile", "computer", cards["computer"].index(value))
                            print("Opponent also had a " + str(value) + ", so they played that as well!")
                    for value in cards["computer"]:
                        if evaluate(list(value)[-1]) == choice_value:
                            give_from_other_choice("pile", "computer", cards["computer"].index(value))
                            print("Opponent also had a " + str(value) + ", so they played that as well!")
                    for value in cards["computer"]:
                        if evaluate(list(value)[-1]) == choice_value:
                            give_from_other_choice("pile", "computer", cards["computer"].index(value))
                            print("Opponent also had a " + str(value) + ", so they played that as well!")
                    return
        for i in range(15):
            for value in cards["computer"]:
                choice_value = list(value)[-1]
                choice_value = evaluate(choice_value)
                if choice_value == 10 or choice_value == 2:
                    if choice_value == 10:
                        print("Opponent played " + value + " onto the pile")
                        give_from_other_choice("pile", "computer", cards["computer"].index(value))
                        print("Since it was a ten, the pile goes into discard!")
                        print("Moved " + str(len(cards["pile"])) + " cards into discard!")
                        for i in range(len(cards["pile"])):
                            give_from_other_rand("discard", "pile")
                        return
                    elif choice_value == 2:
                        print("Opponent played " + value + " onto the pile")
                        give_from_other_choice("pile", "computer", cards["computer"].index(value))
                        sleep(1)
                        print("Since it was a two, they go again!")
                        sleep(1)
                        return "jaderabbit"
        print("Opponent was unable to play a card!")
        print("They took " + str(len(cards["pile"])) + " cards from the pile!")
        for i in range(len(cards["pile"])):
            give_from_other_rand("computer", "pile")
            
    def opponent_play_palace():
        if len(cards["pile"]) != 0:
            pile_value = list(cards["pile"][-1])[-1]
            pile_value = evaluate(pile_value)
        else:
            pile_value = 0
        for i in range(15):
            for value in cards["computerup"]:
                choice_value = list(value)[-1]
                choice_value = evaluate(choice_value)
                if choice_value == pile_value + i and choice_value != 10 and choice_value != 2:
                    print("Opponent played " + value + " onto the pile")
                    give_from_other_choice("pile", "computerup", cards["computerup"].index(value))
                    return
        for i in range(15):
            for value in cards["computerup"]:
                choice_value = list(value)[-1]
                choice_value = evaluate(choice_value)
                if choice_value == 10 or choice_value == 2:
                    if choice_value == 10:
                        print("Opponent played " + value + " onto the pile")
                        give_from_other_choice("pile", "computerup", cards["computerup"].index(value))
                        print("Since it was a ten, the pile goes into discard!")
                        print("Moved " + str(len(cards["pile"])) + " cards into discard!")
                        for i in range(len(cards["pile"])):
                            give_from_other_rand("discard", "pile")
                        return
                    elif choice_value == 2:
                        print("Opponent played " + value + " onto the pile")
                        give_from_other_choice("pile", "computerup", cards["computerup"].index(value))
                        sleep(1)
                        print("Since it was a two, they go again!")
                        sleep(1)
                        return "jaderabbit"
        print("Opponent was unable to play a card!")
        print("They took " + str(len(cards["pile"])) + " cards from the pile!")
        give_from_other_choice("computer", "computerup", cards["computerup"][0])
        for i in range(len(cards["pile"])):
            give_from_other_rand("computer", "pile")
    
    def opponent_play_bottom():
        if len(cards["pile"]) != 0:
            pile_value = list(cards["pile"][-1])[-1]
            pile_value = evaluate(pile_value)
        else:
            pile_value = 0
        choice = random.randint(1, len(cards["computerdown"]))
        choice = cards["computerdown"][choice - 1]
        choice_value = list(choice)[-1]
        choice_value = evaluate(choice_value)
        if choice_value == 10 or choice_value == 2:
            if choice_value == 10:
                print("Opponent flipped over...")
                sleep(5)
                print(str(choice) + "!")
                sleep(2)
                give_from_other_choice("pile", "computerdown", cards["computerdown"].index(choice))
                print("Since it was a ten, the pile goes into discard!")
                print("Moved " + str(len(cards["pile"])) + " cards into discard!")
                for i in range(len(cards["pile"])):
                    give_from_other_rand("discard", "pile")
                return
            elif choice_value == 2:
                print("Opponent played " + str(choice) + " onto the pile")
                give_from_other_choice("pile", "computerdown", cards["computerdown"].index(choice))
                sleep(1)
                print("Since it was a two, they go again!")
                sleep(1)
                return "jaderabbit"
        if choice_value < pile_value:
            print("Opponent flipped over...")
            sleep(5)
            print(str(choice) + "!")
            sleep(2)
            give_from_other_choice("pile", "computerdown", cards["computerdown"].index(choice))
            print("But they are unable to play this card!")
            print("Opponent took " + str(len(cards["pile"])) + " cards from the pile!")
            for i in range(len(cards["pile"])):
                give_from_other_rand("computer", "pile")
        else:
            print("Opponent flipped over...")
            sleep(5)
            print(str(choice) + "!")
            sleep(2)
            print("They played " + choice + " onto the pile!")
            give_from_other_choice("pile", "computerdown", cards["computerdown"].index(choice))
    
    def fourofakind():
        pile_values = []
        for value in cards["pile"]:
            pile_values.append(evaluate(list(value)[-1]))
        for i in range(15):
            if pile_values.count(i) >= 4:
                print("Since there were 4 " + str(i) + "'s in the deck, it went to discard!")
                print("Moved " + str(len(cards["pile"])) + " cards into discard!")
                for i in range(len(cards["pile"])):
                    give_from_other_rand("discard", "pile")

    
    read_table()
    
    def phase_one():
        while True == True:
            # this is the main gameplay code n stuff
            aurora_borealis = "burger"
            aurora_borealis = player_play_card()
            try:
                while aurora_borealis == "steamedhams":
                    aurora_borealis = "burger"
                    aurora_borealis = player_play_card()
                    if len(cards["player"]) == 0:
                        give_from_deck("player")
                        print("Player took a card since they ran out of cards!")
                        read_table()
            except:
                print("There are no more cards in the deck, so your turn ended!")
                aurora_borealis == "burger"
            fourofakind()
            read_table()
            print("Opponent's turn...")
            sleep(7)
            fateofallfools = "jester"
            fateofallfools = opponent_play_card()
            while fateofallfools == "jaderabbit":
                fateofallfools = "jester"
                fateofallfools = opponent_play_card()
                try:
                    if len(cards["player"]) == 0:
                        give_from_deck("computer")
                        print("Opponent took a card since they ran out of cards!")
                except:
                    print("There are no more cards in the deck, so opponent's turn ended!")
                    fateofallfools == "jester"
            while len(cards["player"]) < 3:
                if len(cards["deck"]) == 0:
                    return
                give_from_deck("player")
                print("Player took a card to bring their hand to 3 cards!")
    
            while len(cards["computer"]) < 3:
                if len(cards["deck"]) == 0:
                    return
                give_from_deck("computer")
                print("Opponent took a card to bring their hand to 3 cards!")
            sleep(2)
            fourofakind()
            read_table()
    
    def phase_one_alt():
        while True == True:
            # this is the main gameplay code n stuff
            print("Opponent's turn...")
            sleep(7)
            fateofallfools = "jester"
            fateofallfools = opponent_play_card()
            while fateofallfools == "jaderabbit":
                fateofallfools = "jester"
                fateofallfools = opponent_play_card()
                try:
                    if len(cards["player"]) == 0:
                        give_from_deck("computer")
                        print("Opponent took a card since they ran out of cards!")
                except:
                    print("There are no more cards in the deck, so opponent's turn ended!")
                    fateofallfools == "jester"
            fourofakind()
            read_table()
            aurora_borealis = "burger"
            aurora_borealis = player_play_card()
            try:
                while aurora_borealis == "steamedhams":
                    aurora_borealis = "burger"
                    aurora_borealis = player_play_card()
                    if len(cards["player"]) == 0:
                        give_from_deck("player")
                        print("Player took a card since they ran out of cards!")
                        read_table()
            except:
                print("There are no more cards in the deck, so your turn ended!")
                aurora_borealis == "burger"
            
            while len(cards["computer"]) < 3:
                if len(cards["deck"]) == 0:
                    return
                give_from_deck("computer")
                print("Opponent took a card to bring their hand to 3 cards!")
            
            while len(cards["player"]) < 3:
                if len(cards["deck"]) == 0:
                    return
                give_from_deck("player")
                print("Player took a card to bring their hand to 3 cards!")
            
            sleep(2)
            fourofakind()
            read_table()

    
    def phase_two():
        while True == True:
            read_table()
            if len(cards["player"]) != 0:
                aurora_borealis = "burger"
                aurora_borealis = player_play_card()
                while aurora_borealis == "steamedhams":
                    if len(cards["player"]) == 0:
                        while aurora_borealis == "steamedhams":
                            if len(cards["playerup"]) == 0 and len(cards["playerdown"]) != 0:
                                while aurora_borealis == "steamedhams":
                                    aurora_borealis = "burger"
                                    aurora_borealis = player_play_bottom()
                                    if len(cards["player"]) == 0 and len(cards["playerup"]) == 0 and len(cards["playerdown"]) == 0:
                                        print("GAME OVER!")
                                        print("YOU WON")
                                        return
                            else:
                                aurora_borealis = "burger"
                                aurora_borealis = player_play_palace()
                    else:
                        aurora_borealis = "burger"
                        aurora_borealis = player_play_card()
            elif len(cards["playerup"]) != 0:
                aurora_borealis = "burger"
                aurora_borealis = player_play_palace()
                while aurora_borealis == "steamedhams":
                    if len(cards["playerup"]) == 0 and aurora_borealis == "steamedhams":
                        aurora_borealis = "burger"
                        aurora_borealis = player_play_bottom()
                        while aurora_borealis == "steamedhams" and len(cards["playerdown"]) != 0:
                            aurora_borealis = "burger"
                            aurora_borealis = player_play_bottom()
                            if len(cards["player"]) == 0 and len(cards["playerup"]) == 0 and len(cards["playerdown"]) == 0:
                                print("GAME OVER!")
                                print("YOU WON")
                                return
                    else:
                        aurora_borealis = "burger"
                        aurora_borealis = player_play_palace()
                
            else:
                aurora_borealis = "burger"
                aurora_borealis = player_play_bottom()
                while aurora_borealis == "steamedhams" and len(cards["playerdown"]) != 0:
                    aurora_borealis = "burger"
                    aurora_borealis = player_play_bottom()
                    if len(cards["player"]) == 0 and len(cards["playerup"]) == 0 and len(cards["playerdown"]) == 0:
                        print("GAME OVER!")
                        print("YOU WON")
                        return
            if len(cards["player"]) == 0 and len(cards["playerup"]) == 0 and len(cards["playerdown"]) == 0:
                print("GAME OVER!")
                print("YOU WON")
                return
            fourofakind()
            read_table
            print("Opponent's turn...")
            sleep(7)
            if len(cards["computer"]) != 0:
                fateofallfools = "jester"
                fateofallfools = opponent_play_card()
                while fateofallfools == "jaderabbit":
                    if len(cards["computer"]) == 0:
                        while fateofallfools == "jaderabbit":
                            if len(cards["computerup"]) == 0 and len(cards["computerdown"]) != 0:
                                while fateofallfools == "jaderabbit":
                                    fateofallfools = "jester"
                                    fateofallfools = opponent_play_bottom()
                                    if len(cards["computer"]) == 0 and len(cards["computerup"]) == 0 and len(cards["computerdown"]) == 0:
                                        print("GAME OVER!")
                                        print("YOU LOST")
                                        return
                            else:
                                fateofallfools = "jester"
                                fateofallfools = opponent_play_palace()
                    else:
                        fateofallfools = "jester"
                        fateofallfools = opponent_play_card()
            elif len(cards["computerup"]) != 0:
                fateofallfools = "jester"
                fateofallfools = opponent_play_palace()
                while fateofallfools == "jaderabbit":
                    if len(cards["computerup"]) == 0 and fateofallfools == "jaderabbit":
                        fateofallfools = "jester"
                        fateofallfools = opponent_play_bottom()
                        while fateofallfools == "jaderabbit" and len(cards["computerdown"]) != 0:
                            fateofallfools = "jester"
                            fateofallfools = player_play_bottom()
                            if len(cards["computer"]) == 0 and len(cards["computerup"]) == 0 and len(cards["computerdown"]) == 0:
                                print("GAME OVER!")
                                print("YOU LOST")
                                return
                    else:
                        fateofallfools = "jester"
                        fateofallfools = opponent_play_palace()
            else:
                fateofallfools = "jester"
                fateofallfools = opponent_play_bottom()
                while fateofallfools == "jaderabbit":
                    fateofallfools = "jester"
                    fateofallfools = opponent_play_bottom()
                    if len(cards["computer"]) == 0 and len(cards["computerup"]) == 0 and len(cards["computerdown"]) == 0:
                        print("GAME OVER!")
                        print("YOU LOST")
                        return
            if len(cards["computer"]) == 0 and len(cards["computerup"]) == 0 and len(cards["computerdown"]) == 0:
                print("GAME OVER!")
                print("YOU LOST")
                return
            fourofakind()
            
    def phase_two_alt():
        while True == True:
            read_table()
            print("Opponent's turn...")
            sleep(7)
            if len(cards["computer"]) != 0:
                fateofallfools = "jester"
                fateofallfools = opponent_play_card()
                while fateofallfools == "jaderabbit":
                    if len(cards["computer"]) == 0:
                        while fateofallfools == "jaderabbit":
                            if len(cards["computerup"]) == 0 and len(cards["computerdown"]) != 0:
                                while fateofallfools == "jaderabbit":
                                    fateofallfools = "jester"
                                    fateofallfools = opponent_play_bottom()
                                    if len(cards["computer"]) == 0 and len(cards["computerup"]) == 0 and len(cards["computerdown"]) == 0:
                                        print("GAME OVER!")
                                        print("YOU LOST")
                                        return
                            else:
                                fateofallfools = "jester"
                                fateofallfools = opponent_play_palace()
                    else:
                        fateofallfools = "jester"
                        fateofallfools = opponent_play_card()
            elif len(cards["computerup"]) != 0:
                fateofallfools = "jester"
                fateofallfools = opponent_play_palace()
                while fateofallfools == "jaderabbit":
                    if len(cards["computerup"]) == 0 and fateofallfools == "jaderabbit":
                        fateofallfools = "jester"
                        fateofallfools = opponent_play_bottom()
                        while fateofallfools == "jaderabbit" and len(cards["computerdown"]) != 0:
                            fateofallfools = "jester"
                            fateofallfools = player_play_bottom()
                            if len(cards["computer"]) == 0 and len(cards["computerup"]) == 0 and len(cards["computerdown"]) == 0:
                                print("GAME OVER!")
                                print("YOU LOST")
                                return
                    else:
                        fateofallfools = "jester"
                        fateofallfools = opponent_play_palace()
            else:
                fateofallfools = "jester"
                fateofallfools = opponent_play_bottom()
                while fateofallfools == "jaderabbit":
                    fateofallfools = "jester"
                    fateofallfools = opponent_play_bottom()
                    if len(cards["computer"]) == 0 and len(cards["computerup"]) == 0 and len(cards["computerdown"]) == 0:
                        print("GAME OVER!")
                        print("YOU LOST")
                        return
            fourofakind()
            if len(cards["computer"]) == 0 and len(cards["computerup"]) == 0 and len(cards["computerdown"]) == 0:
                print("GAME OVER!")
                print("YOU LOST")
                return
            if len(cards["player"]) != 0:
                aurora_borealis = "burger"
                aurora_borealis = player_play_card()
                while aurora_borealis == "steamedhams":
                    if len(cards["player"]) == 0:
                        while aurora_borealis == "steamedhams":
                            if len(cards["playerup"]) == 0 and len(cards["playerdown"]) != 0:
                                while aurora_borealis == "steamedhams":
                                    aurora_borealis = "burger"
                                    aurora_borealis = player_play_bottom()
                                    if len(cards["player"]) == 0 and len(cards["playerup"]) == 0 and len(cards["playerdown"]) == 0:
                                        print("GAME OVER!")
                                        print("YOU WON")
                                        return
                            else:
                                aurora_borealis = "burger"
                                aurora_borealis = player_play_palace()
                    else:
                        aurora_borealis = "burger"
                        aurora_borealis = player_play_card()
            elif len(cards["playerup"]) != 0:
                aurora_borealis = "burger"
                aurora_borealis = player_play_palace()
                while aurora_borealis == "steamedhams":
                    if len(cards["playerup"]) == 0 and aurora_borealis == "steamedhams":
                        aurora_borealis = "burger"
                        aurora_borealis = player_play_bottom()
                        while aurora_borealis == "steamedhams" and len(cards["playerdown"]) != 0:
                            aurora_borealis = "burger"
                            aurora_borealis = player_play_bottom()
                            if len(cards["player"]) == 0 and len(cards["playerup"]) == 0 and len(cards["playerdown"]) == 0:
                                print("GAME OVER!")
                                print("YOU WON")
                                return
                    else:
                        aurora_borealis = "burger"
                        aurora_borealis = player_play_palace()
            else:
                aurora_borealis = "burger"
                aurora_borealis = player_play_bottom()
                while aurora_borealis == "steamedhams" and len(cards["playerdown"]) != 0:
                    aurora_borealis = "burger"
                    aurora_borealis = player_play_bottom()
                    if len(cards["player"]) == 0 and len(cards["playerup"]) == 0 and len(cards["playerdown"]) == 0:
                        print("GAME OVER!")
                        print("YOU WON")
                        return
            if len(cards["player"]) == 0 and len(cards["playerup"]) == 0 and len(cards["playerdown"]) == 0:
                print("GAME OVER!")
                print("YOU WON")
                return
            fourofakind()

    if player_goes == True:
        if len(cards["deck"]) != 0:
            phase_one()
        phase_two()
    else:
        if len(cards["deck"]) != 0:
            phase_one_alt()
        phase_two_alt()
    
    print(cards)
    
    replay_response = input("Play again? (y/n) ")
    if replay_response.lower() == "y":
        replay = True
    else:
        replay = False

# fin