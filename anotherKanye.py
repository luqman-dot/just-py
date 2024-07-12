import random

def print_title():
    print(r"""                      
                                 ____                 _     ____            
  /\ /\__ _ _ __  _   _  ___    /___ \_   _  ___  ___| |_  |___ \ _             
 / //_/ _` | '_ \| | | |/ _ \  //  / / | | |/ _ \/ __| __|   __) (_)            
/ __ \ (_| | | | | |_| |  __/ / \_/ /| |_| |  __/\__ \ |_   / __/ _             
\/  \/\__,_|_| |_|\__, |\___| \___,_\ \__,_|\___||___/\__| |_____(_)            
                  |___/                                                         
   __ _           _        _          ___                         _             
  /__\ | ___  ___| |_ _ __(_) ___    / __\ ___   ___   __ _  __ _| | ___   ___  
 /_\ | |/ _ \/ __| __| '__| |/ __|  /__\/// _ \ / _ \ / _` |/ _` | |/ _ \ / _ \ 
//__ | |  __/ (__| |_| |  | | (__  / \/  \ (_) | (_) | (_| | (_| | | (_) | (_) |
\__/ |_|\___|\___|\__|_|  |_|\___| \_____/\___/ \___/ \__, |\__,_|_|\___/ \___/ 
                                                      |___/     """)
    print("\n")

def start_over():
    print("Kanye never finds his family and dies alone. Try Again!")
    main()

def invalid_input():
    print("Invalid input, Kanye never finds his family and dies alone. Try Again!")
    main()

def main():
    print_title()
    
    start_of_game = input("Would you like to play the game? (yes/no)  ").strip().lower()
    if start_of_game == "no":
        print("Then why are you here? Thanks for coming!")
        start_over()
    elif start_of_game == "yes":
        print("\nPreviously on Kanye Quest….")
        print("Drake and Kanye’s long feud had come to an end when Kanye stopped Drake's tomfoolery.")
        print("Now that the beef has been squashed, as Kanye and Drake will soon find out that there is a new enemy amidst,")
        print("threatening not just Kanye's Yeezys but the man's family. The two unlikely foes will have to join forces to stop this threat.\n")
        
        still = input("Would you still like to play? (yes/no)  ").strip().lower()
        if still == "no":
            print("Ok then Leave.")
            start_over()
        elif still == "yes":
            print("\nThen let's start the game!\n")
            print("Setting: Donda 2 concert\n")
            print("Kanye is performing in front of a large crowd when he notices his lovely wife Kim and his children being taken against their will by hooded figures.")
            print("Shocked but composed, Kanye finishes the concert before taking action.")
            print("Kanye frantically searches the stadium for his family, but to no success.\n")
            print("He turns to the only person he trusts to help him: DRAKE.")
            print("Drake is on stage, and Kanye asks for his help. Drake agrees, but says, 'Yes, but there will be a cost.'")
            print("Understanding, Kanye gets into Drake's limo.\n")
            print("Drake and Kanye speed down the street and come across 3 intersections:")
            print("1. 5th Avenue")
            print("2. Howard Street")
            print("3. Elysian Park\n")
            
            first_intersection = input("Which intersection do they choose? (1/2/3)  ").strip()
            if first_intersection == "1":
                fifth_avenue()
            elif first_intersection == "2":
                howard_street()
            elif first_intersection == "3":
                elysian_park()
            else:
                invalid_input()
        else:
            invalid_input()
    else:
        invalid_input()

def fifth_avenue():
    print("\nKanye and Drake make a left onto 5th Avenue. They see one of the hooded figures.")
    print("The figure starts running, leading Kanye and Drake to an alleyway where it disappears.")
    print("Kanye is confused and turns to Drake for advice.\n")
    
    second_intersection = input("What should Kanye do? (call the police/keep looking)  ").strip().lower()
    if second_intersection == "call the police":
        print("\nKanye calls the police and tells them about his family being kidnapped.")
        print("The police assure Kanye they will do everything they can to help.")
        print("Kanye feels a little relieved but knows he must keep searching.\n")
        print("Where should Kanye and Drake go next?")
        print("1. Home")
        print("2. Hotel\n")
        
        third_intersection = input("Enter your choice (home/hotel):  ").strip().lower()
        if third_intersection == "home":
            home()
        elif third_intersection == "hotel":
            hotel()
        else:
            invalid_input()
    elif second_intersection == "keep looking":
        print("\nKanye and Drake decide to keep looking for more clues.")
        print("They come across another hooded figure who puts up a fight.")
        print("After a tough battle, they manage to overpower the figure and get information about the kidnappers' hideout.")
        print("Kanye and Drake head to the hideout and rescue Kim and the kids.")
        print("Kanye and Drake have saved the day!")
    else:
        invalid_input()

def howard_street():
    print("\nKanye and Drake make a right onto Howard Street. They see a suspicious van parked on the side.")
    print("They decide to follow the van discreetly, which leads them to an old warehouse.")
    print("Kanye and Drake sneak into the warehouse and find Kim and the kids tied up.")
    print("They manage to rescue them and escape just in time before the kidnappers return.")
    print("Kanye and Drake have saved the day!")

def elysian_park():
    print("\nKanye and Drake head towards Elysian Park. They come across a group of people having a meeting.")
    print("Kanye and Drake hide and listen to their conversation, realizing they are part of the kidnapping gang.")
    print("They follow the group to their hideout and successfully rescue Kim and the kids.")
    print("Kanye and Drake have saved the day!")

def home():
    print("\nKanye and Drake head to Kanye's home. They see signs of a struggle and realize they are getting closer.")
    print("They find a note with an address leading them to an abandoned warehouse.\n")
    print("Kanye and Drake sneak into the warehouse and find Kim and the kids tied up.")
    print("They manage to rescue them and escape just in time before the kidnappers return.")
    print("Kanye and Drake have saved the day!")

def hotel():
    print("\nKanye and Drake check into a hotel to regroup and plan their next move.")
    print("While at the hotel, they receive a tip-off about the kidnappers' location.")
    print("They rush to the location and successfully rescue Kim and the kids.")
    print("Kanye and Drake have saved the day!")

main()
