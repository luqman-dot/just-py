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
def main(): 
    def start_over():
        print("Peter never finds his family and dies alone. Try Again!")
        main()
        
    def invalid_input():
        print("Invalid input, Peter never finds his family and dies alone. Try Again!")
        main()
    
    print("")
    start_of_game = input("Would you like to play the game? (yes/no)  ").strip().lower()
    if start_of_game == "no":
        print("Then why are you here? Thanks for coming!")
        start_over()
    elif start_of_game == "yes":
        print(" ")
        print("Previously on Peter Quest….")
        print("Moses and Peter’s long feud had come to an end when Peter stopped Moses's tomfoolery,")
        print("Now that the beef has been squashed, as Peter and Moses will soon find out that there is a new enemy amidst,")
        print("threatening not just Peter's but the man's family. The two unlikely foes will have to join forces to stop this threat.")
        
        still = input("Would you still like to play? (yes/no)  ").strip().lower()
        if still == "no":
            print("Ok then Leave.")
            start_over()
        elif still == "yes":
            print(" ")
            print("Then let's start the game!")
            print(" ")
            print("Setting: WOnda 1 concert")
            print(" ")
            print("Peter is performing in front of a large crowd, he is in the middle of performing when he notices that his lovely wife Winnie and his children are taken against their will by hooded figures.")
            print(" Peter is shocked but as a true gentleman he finishes the concert and then acts accordingly.")
            print("Peter frantically searches around the stadium for his wife and kids to no success.")
            print(r"""
                        ................                                             
                    ............................                                        
                 ..................................                                     
                ............'''''''......................                               
             ..........''','',,,,,''''''...................                             
          ..........''',,,;;;;:;;;;,,,,,,''''''''...........                            
         .......'',,,,;:::c:ccccccc:::;;;;;;,,,,''''..........                          
        ....''',;;;::ccccllloooooolcccc::::;;;,,,'''..........                          
       ....'',,;;::cclclllooodddddollllcc:::;;,,,''''..........                         
    . ....'',,,;;:ccllllloooddxxxxdoollccc::;;,,,,,'''..........                        
    .....'',,,;;;:cclllllooddxxxxxxxxdolcc::;;;,,,,,''...........                       
     ....'',,,;;::cclllllodxxkkkkkOkxdollcc::;;,,,,,,''..........                       
     ....'',,;;;::ccllllodxxxxxxxxxdddooollcc::;;;,,,''..........                       
    ...'''',;;;;::ccllloodddxxxxxxkkkxxdoollc::;;;,,,''..........                       
    ....'',,;;;;::cllooodddxxkkkkxxxxxxddoollc::;;;,,,'''.........                      
     ....',,;;;::ccllooooddddxxxdxxxxkkkxxdollcc:::;;,,''.........                      
     ....',,,;;::cclodddxxkkkkOkkkkkkOkkkkxdoollccc::;;,,'.......                       
      ...',,;;;;::cclodxkkOOOOOOOOOOOkkkkxolcc::;;;;,,,,'.........                      
      ...','....'''',;:ldxkkO000000Okxdol:,''....'''''.............   ....              
      ................'';codxxxxxxdoolc:,'''''',,,,,''''...........  .,'.'.             
      ......',,,,,,,,'''',:clloooolcc::;;;::::clc:c:,,,,,,,'....... .''.':;             
      ....',;;::::;;;;;,''',;;:looc::;,;;::::cod:,'.......',,,,'......',,:;             
      ...',,,,,',;c;,,''',,',,;codoc:;;;;;;;cdk0d:'...'...,;;;;,'.....;:,c;             
      ..''''...:xO0l....':;,;;;coxdlc:;;;:::cloddol:;,,,,;:::::;,'.. .:lc;'             
      ..',,,..'codxl;,;;:loc;;:ldxxdlc:;;:cccccllllc:::::ccccc:;,'....cdl,.             
      .',;::;,',;:ccllcclolc::cldxkxolcc:;:cloooooooooolllllcc:;,'....:dl'              
     ..',;cc::;;;:ccccloolc::ccldxxxolcc:::clooddddddddoddoolc:;,'... .:,.              
      .',;:cccllllooddddolc:::cldxxddoc::;;:loddddddxxxxddoolc:;,'.......               
       .,;:clloooddddddddoc:;:clloddlcccc:;;codxxxxxxxxdoolc:;;,,'....                  
       .';;clloodddddddddol:;:clloddlcccc:;;codxxxxxxxxdoolc:;;,,'....                  
       .',;::clooddddddddol:::clodxxolcccll::ldxdxxxxxddolc::;;,,'....                  
       ..',;::cllooddddxdocccccloxOOxolclodl:;oxddxxdddollc:;;,,''....                  
        .',;;:ccloodddxxdoclolccoodxdoc:::cc:,cxxxxdddoolcc:;;,'''....                  
        .',,;;:clllooddddoc::;,,;:::::;;;;;;;:loddddoollcc::;,,''.....                  
        ..',,;::cclloodddoc:;,;;;:c::ccc::cccllloolllcccc::;,,'''.....                  
        ..'',,;;::ccclllllcccc;',;;;;,,,,',;;:cclollc:::;;;,,,''''...                   
        ...'',,;;;;::::ccc:;,'..',,,,,;;,''..',,;;:ccc:;,;;,,,''''...                   
         ..''',,;;;;;;:c:;,''',::::cllcc::;;,;;,'..';::;,,,,,,,'''..                    
          ..'',,,,,,,;:;,',;;;;;;;;;:c:;;;;,,,,;,''.';:;,,,,,,,''...                    
           ..'',,,,,,;,'',,''',,,,;;::;;:;;;;;,;;:;;,,;:;;,,,,'''..                     
            ..''',;,;;,'',,,,;;::clllllllc::;;::cccc;,,;;,,,,''..  ..               
             ..'',,;;;,,;::;;::cclodddddolc:::::cccc:,,,,,''''.. .........,'......        
               ...'',,,,;::;;::::ccllcc::;;;;::::::;,'.','''..  ..'......'lolccoddolc:'.
                ....''..';;;;;;;,'''..'',,,;:;;,,,''...''''.. ..''''......'cdo:coxkOK0Od:. 
                  ........''',,;,,,,,,::;;;;;,.............. .',,''''...'.':odloxdcdKNXK0xl
                    ..........',,,,;;;;;,'''''............ ..,;,,''''..''',:ldolxkkXNNNNXXX
                  ...............',;;:;;;'''............  .,;;;;,,'''..'',;oocoxx0NWNNNNNNN
             ..,cdkOx:.............'''''''............   .;::;;;,,,''.'',;clodokKNWWNNNNNNN
          .,cdOKXXXXkoc,........................    .   .;c:;;;;,,,,,'',,ckkccdONWNWNNNNWWW
       .:dkKKXNXXNX0xdo;.....................          .;:::;;;;;;;;,,',cllxdo0NWWWWWWWWWWW
    'cx0XXNXXNNNNNXK0d;...............................;:;;:::;;;:;;;;;:looxkkKNNWWWWWWWWWWW
.,lx0KKKXXXXNXXNXNNXKo'..............................;:;;;;;;;;;;:::clodxOKXNWNNNWWWWWWWWWW
:kKXNXXXXXXNXNXXXXNNO;.............................';:;;;;;;;;;;;:cldxOKNNNNWNWWWWWWWWWWWWW
d0XXNXXXNXXXNXXXXNNNO,............................',;:;;;;;;;;;:cldkKXNNNWWNWWWWWWWWWWWWWWW
kXNXXXNXXXXNNXXNNXNNk,...........................,,;:::;;;;:;:coox0NNWWNWWWWWWWWWWWWWWWWWWW
kXXXXXXXXXNNNNNNXXNNx,...........................,,;;:;;;;;:cldxOKNWWNNWWWWWWWWWWWWWWWWWWWW
d0XNNNNNNNNNNNNNNXNNk,...........................,,;;;;;;:cldxOKXNWNNNWWWWWWWWWWWWWWWWWWWWW
:d0XNNNNNNNNNNNXXXXXKo'..........................,,;;;::ccldkKXXNNNWWWWWWWWWWWWWWWWWWWWWWWW
.c0NNXNNNNXNNNNXXXXXXk,..........................,,;;::ccox0XNNNWNNWWWWWWWWWWWWWWWWWWWWWWWW
k0000KXNNXNNNNNNXXXXNNk'.........................,,;:::clxKNNWNNNNWWWWWWWWWWWWWWWWWWWWWWWWWW
NNNNNNNNNNNNNNNNNNNNNNk'.........................,,;::lx0XNWNNNNWWWWWWWWWWWWWWWWWWWWWWWWWWWW
NWWNNNNNNNNNNNNNNNNNNNO,...........................';lx0KXNWNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
NWWWWNNNNNNNNNNNNNNNNN0,...........................,cdOKXNWNNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
NWWWWWWNNNNNNNNNNNNNNN0,............................;oOKXNNWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
""")
            print(" ")
            print("He turns to the only person he trusts to help him, DRAKE.")
            print("Drake is on stage, Kanye asks for his help. Drake says, 'Yes, but there will be a cost.'")
            print("Kanye understands this and gets into Drake's limo.")
            print(" ")
            print("Drake and Kanye speed down the street and come across 3 intersections.")
            print("The first intersection is 5th avenue")
            print("The second intersection is Howard street")
            print("The third intersection is Elysian Park")
            print(" ")
            first_intersection = input("Which intersection do they choose? (1/2/3)  ").strip()
            if first_intersection == "1":
                print(" ")
                print("Kanye and Drake make a left onto 5th avenue. They see one of the hooded figures.")
                print("The figure starts running, leading Kanye and Drake to an alleyway. The figure then disappears.")
                print("Kanye is confused and turns to Drake for advice.")
                print(" ")
                second_intersection = input("What should Kanye do? (call the police/keep looking)  ").strip().lower()
                if second_intersection == "call the police":
                    print(" ")
                    print("Kanye calls the police and tells them about his family being kidnapped.")
                    print("The police assure Kanye that they will do everything they can to help.")
                    print("Kanye feels a little relieved but knows he must keep searching.")
                    print(" ")
                    third_intersection = input("Where should Kanye and Drake go next? (home/hotel)  ").strip().lower()
                    if third_intersection == "home":
                        print(" ")
                        print("Kanye and Drake head to Kanye's home. They see signs of a struggle and realize they are getting closer.")
                        print("They find a note with an address leading them to an abandoned warehouse.")
                        print(" ")
                        print("Kanye and Drake sneak into the warehouse and find Kim and the kids tied up.")
                        print("They manage to rescue them and escape just in time before the kidnappers return.")
                        print("Kanye and Drake have saved the day!")
                    elif third_intersection == "hotel":
                        print(" ")
                        print("Kanye and Drake decide to check into a hotel to regroup and plan their next move.")
                        print("While at the hotel, they receive a tip-off about the kidnappers' location.")
                        print("They rush to the location and successfully rescue Kim and the kids.")
                        print("Kanye and Drake have saved the day!")
                    else:
                        invalid_input()
                elif second_intersection == "keep looking":
                    print(" ")
                    print("Kanye and Drake decide to keep looking for more clues.")
                    print("They come across another hooded figure who puts up a fight.")
                    print("After a tough battle, they manage to overpower the figure and get information about the kidnappers' hideout.")
                    print("Kanye and Drake head to the hideout and rescue Kim and the kids.")
                    print("Kanye and Drake have saved the day!")
                else:
                    invalid_input()
            elif first_intersection == "2":
                print(" ")
                print("Kanye and Drake make a right onto Howard street. They see a suspicious van parked on the side.")
                print("They decide to follow the van discreetly. The van leads them to an old warehouse.")
                print("Kanye and Drake sneak into the warehouse and find Kim and the kids tied up.")
                print("They manage to rescue them and escape just in time before the kidnappers return.")
                print("Kanye and Drake have saved the day!")
            elif first_intersection == "3":
                print(" ")
                print("Kanye and Drake head towards Elysian Park. They come across a group of people who seem to be having a meeting.")
                print("Kanye and Drake hide and listen to their conversation, realizing they are part of the kidnapping gang.")
                print("They follow the group to their hideout and successfully rescue Kim and the kids.")
                print("Kanye and Drake have saved the day!")
            else:
                invalid_input()
        else:
            invalid_input()
    else:
        invalid_input()

main()
