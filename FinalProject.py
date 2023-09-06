# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Victoria Villarreal 531004724
#               Audry Estrada 931009967
#               Nicholas Klein 131007452
# Section:      6-469-569
# Assignment:   Project
# Date:         November 15, 2021
#

from colorama import Fore, Style

# GAME 1 - ADVENTURE #########################################################

# RiGHT PATH STORY
def right():
    print()
    print('You decided to take the right path. However, you begin to wonder if you’ve chosen wisely.')
    print('Before you could turn around, something catches your eye. You find a line of rope.')
    print('Soon after you obtained the rope, you heard a rustle in the trees above you.')
    print('Suddenly, you are shoved to the ground with a man holding you in a chokehold.')
    print('The man tells you to be silent. ')
    choice = input("What will you do? Will you SCREAM, STRUGGLE, or be STILL? ")
    while(choice != 'STOP' or choice != 'stop'):
        if choice == 'SCREAM' or choice == 'scream':
            print()
            print('You decided to scream out in fear and alarmed a dangerous creature.')
            print('The creature captured you and you have decided doom.')
            choice = input("Try again? YES or NO: ")
            while(choice != 'STOP' or choice != 'stop'):
                if choice == 'yes' or choice == 'YES' or choice == 'Y' or choice == 'y':
                    adventure()
                elif choice == 'no' or choice == 'NO' or choice == 'N' or choice == 'n':
                    return 0
                else:
                    print("I didn't understand understand what you're trying to say")
                    choice = input("Try again? YES or NO: ")
            return 0
        elif choice == 'STRUGGLE' or choice == 'struggle':
            print()
            print('You decided to fight off the man, but he was twice your size and all you had was rope.')
            print('Your struggle caused a dangerous creature to notice you and it came to your doom.')
            choice = input("Try again? YES or NO: ")
            while(choice != 'STOP' or choice != 'stop'):
                if choice == 'yes' or choice == 'YES' or choice == 'Y' or choice == 'y':
                    adventure()
                elif choice == 'no' or choice == 'NO' or choice == 'N' or choice == 'n':
                    return 0
                else:
                    print("I didn't understand understand what you're trying to say")
                    choice = input("Try again? YES or NO: ")
            return 0
        
        elif choice == 'stop' or choice == 'STOP':
            return 0
        
        elif choice == "STILL" or choice == "still":
            print()
            print('You decided to hold your tongue and listen to what the man wanted.')
            print('He didn’t say anything but he pointed to the danger. Before you was another local legend.')
            print('A buck that shapeshifts and reveals dark truths whenever a person meets eyes with it.')
            print('The man pulled you behind a tree and waited for the buck to leave.')
            print('It did, eventually, and you and the man came out of hiding.')
            print('“You should go back”, the man tells you, “from wherever it is you came.”')
            print('Before you could tell the man about Guidance, there was a carriage that')
            print('was heading right toward you. The man who saved you from the Buck and you')
            print("were now surrounded. They searched you and took your rope.")
            print("They eventually took you to the Evil Lord Cyriacus.")
            print("The Evil Lord asked you to join him. You noticed that the man you first")
            print("encountered was beside you. He did not look pleased. ")
            choice = input("What do you do? Will you PLEA, REFUSE, or AGREE TO BECOME A MINION? ")
            while(choice != 'STOP' or choice != 'stop'):
                if choice == 'PLEA' or choice == 'plea':
                    print()
                    print('You attempted to gain some sympathy from the tyrant Lord and found it no use.')
                    print('Lord Cyriacus, however, did let you go, but not in a way you think was merciful.')
                    choice = input("Try again? YES or NO: ")
                    while(choice != 'STOP' or choice != 'stop'):
                        if choice == 'yes' or choice == 'YES' or choice == 'Y' or choice == 'y':
                            adventure()
                        elif choice == 'no' or choice == 'NO' or choice == 'N' or choice == 'n':
                            return 0
                        else:
                            print("I didn't understand understand what you're trying to say")
                            choice = input("Try again? YES or NO: ")
                    return 0
                elif choice == "REFUSE" or choice == 'refuse':
                    print()
                    print('You refused to join the Evil Lord and were no longer their concern.')
                    print('They tossed you out of the kingdom and had no idea how to return home.')
                    print('You eventually wandered helplessly lost and met your doom.')
                    choice = input("Try again? YES or NO: ")
                    while(choice != 'STOP' or choice != 'stop'):
                        if choice == 'yes' or choice == 'YES' or choice == 'Y' or choice == 'y':
                            adventure()
                        elif choice == 'no' or choice == 'NO' or choice == 'N' or choice == 'n':
                            return 0
                        else:
                            print("I didn't understand understand what you're trying to say")
                            choice = input("Try again? YES or NO: ")
                    return 0
                
                elif choice == 'stop' or choice == 'STOP':
                    return 0
                elif choice == 'AGREE TO BECOME A MINION' or choice == 'agree to become a minion':
                    print()
                    print('Without much other option, you decided to join the Evil Lord.')
                    print('The man who you encountered instantly refused, but Lord Cyriacus')
                    print('appeared to have history with him so he merely sent him to a dungeon.')
                    print('Your first task as a minion is to guard the cell.')
                    print('When you and the man were alone, the man looked at you.')
                    print('“If you let me go, I can take you back to the forest. I even know a hidden exit')
                    print('we can take to escape. You just need to let me out.”')
                    
                    choice = input("What will you do? Will you FORCE HIM TO TELL YOU THE EXIT, NOT LISTEN TO THE MAN, or LET HIM FREE? ")
                    while(choice != 'STOP' or choice != 'stop'):
                        if choice == 'Force him to tell you the exit' or choice == 'FORCE HIM TO TELL YOU THE EXIT':
                            print()
                            print('You decided to only care about yourself and force the man')
                            print('to tell you the exit before letting him free.')
                            print('Not keeping your word you left the man to rot in the cell.')
                            print('You managed to escape but you had no idea how to return home.')
                            print('You face your doom while wandering through the forest.')
                            choice = input("Try again? YES or NO: ")
                            while(choice != 'YES' or choice != 'yes'):
                                if choice == 'yes' or choice == 'YES' or choice == 'Y' or choice == 'y':
                                    adventure()
                                elif choice == 'no' or choice == 'NO' or choice == 'N' or choice == 'n':
                                    return 0
                                else:
                                    print("I didn't understand understand what you're trying to say")
                                    choice = input("Try again? YES or NO: ")
                            return 0
                        
                        elif choice == 'not listen to the man' or choice == 'NOT LISTEN TO THE MAN':
                            print()
                            print('You decided to not listen to the man and continue to be')
                            print('a minion to the Evil Lord. You gain riches and power after')
                            print('years of dedicating your life to Lord Cyriacus, but you were')
                            print('then used as a pawn when a war was made against your own home.')
                            print('You died in battle for a war you regretted to be in.')
                            choice = input("Try again? YES or NO: ")
                            while(choice != 'YES' or choice != 'yes'):
                                if choice == 'yes' or choice == 'YES' or choice == 'Y' or choice == 'y':
                                    adventure()
                                elif choice == 'no' or choice == 'NO' or choice == 'N' or choice == 'n':
                                    return 0
                                else:
                                    print("I didn't understand understand what you're trying to say")
                                    choice = input("Try again? YES or NO: ")
                            return 0
                        
                        elif choice == 'stop' or choice == 'STOP':
                            return 0
                        
                        elif choice == 'LET HIM FREE' or choice == 'let him free':
                            print()
                            print('You released the man out of his cell and he led you out the castle.')
                            print('While you both were heading back to the forest, you were')
                            print('asked why you were in the forest in the first place.')
                            print('You explained that Guidance had led you there and the man')
                            print('had a disheartened look in his eyes. You asked the man what his story was.')
                            print('He was a hunter who has been tracking down the buck Reality for years.')
                            print('Before you two realise, you both were snatched into the air by a net.')
                            print('You and the man had no tools to escape. You and the man stayed in the net')
                            print('for hours until a hooded figure approached from the path.')
                            print('With one swift motion, the figure cut the rope and you and the man fell to the ground.')
                            choice = input('What will you do? Will you RUN, FIGHT, or SURRENDER? ')
                            while(choice != 'STOP' or choice != 'stop'):
                                if choice == 'Run' or choice == 'RUN':
                                    print()
                                    print('You cowardly ran away from the hooded figure who had')
                                    print('taken the hunter down. You were lost in the forest and')
                                    print('couldn’t return home.')
                                    choice = input("Try again? YES or NO: ")
                                    if choice == 'yes' or choice == 'YES' or choice == 'Y' or choice == 'y':
                                        adventure()
                                    elif choice == 'no' or choice == 'NO' or choice == 'N' or choice == 'n':
                                        return 0
                                    else:
                                        print("I didn't understand understand what you're trying to say")
                                        choice = input("Try again? YES or NO: ")
                                if choice == 'FIGHT' or choice == 'fight':
                                    print()
                                    print('Without hesitation, you try to fight the stranger with nothing')
                                    print('but your bare hands. The hunter joined you, but the armed stranger')
                                    print('instantly outmatched both of you. You meet your doom sooner than expected.')
                                    choice = input("Try again? YES or NO: ")
                                    if choice == 'yes' or choice == 'YES' or choice == 'Y' or choice == 'y':
                                        adventure()
                                    elif choice == 'no' or choice == 'NO' or choice == 'N' or choice == 'n':
                                        return 0
                                    else:
                                        print("I didn't understand understand what you're trying to say")
                                        choice = input("Try again? YES or NO: ")
                                elif choice == 'stop' or choice == 'STOP':
                                    return 0
                                
                                elif choice == 'SURRENDER' or choice == 'surrender':
                                    print()
                                    print('Because the stranger was armed and you were not much of a fighter,')
                                    print('you surrendered to the stranger. The hunter did as well.')
                                    print('The hooded stranger motioned them to walk. Without much choice,')
                                    print('they followed the stranger. The hunter would glance at you and')
                                    print('then to the hooded stranger. The stranger came to a clearing and faced you.')
                                    print('They slipped off their hood and revealed antlers on their head.')
                                    print('The hunter looked away, but you were already trapped in the trance.')
                                    print('The dark truth revealed to you and your doom. The stranger then turned and left.')
                                    print('The hunter asked what you had seen. Before you could answer, an arrow was shot into your shoulder.')
                                    print('The Dark Lord’s minions have found you again. You and the hunter ran past the trees to a cliff.')
                                    print('The ground beneath you collapsed and you and the hunter held onto dead roots of a dying tree.')
                                    print('The hunter was losing his grip.')
                                    choice = input('What do you do? Will you NOT HELP HIM or HELP HIM? ')
                                    while(choice != 'STOP' or choice != 'stop'):
                                        if choice == 'NOT HELP HIM' or choice == 'not help him':
                                            print()
                                            print('Thinking only of yourself, you let the Hunter fall to his doom.')
                                            print('The men eventually found you and took you back as a prisoner.')
                                            print('You met your doom by living in a dungeon for the rest of your life. Try again?')
                                            choice = input("Try again? YES or NO: ")
                                            if choice == 'yes' or choice == 'YES' or choice == 'Y' or choice == 'y':
                                                adventure()
                                            elif choice == 'no' or choice == 'NO' or choice == 'N' or choice == 'n':
                                                return 0
                                            else:
                                                print("I didn't understand understand what you're trying to say")
                                                choice = input("Try again? YES or NO: ")
                                        elif choice == 'stop' or choice == 'STOP':
                                            return 0
                                        
                                        elif choice == 'Help him' or 'HELP HIM':
                                            print('You reached out your hand and the hunter took it before he fell.')
                                            print('You now struggle to hold you and the hunter up.')
                                            print('The Dark Lord stands over the cliff. He offers to help')
                                            print('if you promise to help him conquer the world.')
                                            print('You could either fall into the water below or become')
                                            print('a pawn to conquer the world.')
                                            choice = input("What do you do? Will you CONQUER THE WORLD or FALL? ")
                                            while(choice != 'STOP' or choice != 'stop'):
                                                if choice == 'CONQUER THE WORLD' or choice == 'conquer the world':
                                                    print()
                                                    print('You took the offer and became a pawn to the Dark Lord.')
                                                    print(' You met your doom on a battlefield for a treacherous cause. Try again?')
                                                    choice = input("Try again? YES or NO: ")
                                                    if choice == 'yes' or choice == 'YES' or choice == 'Y' or choice == 'y':
                                                        adventure()
                                                    elif choice == 'no' or choice == 'NO' or choice == 'N' or choice == 'n':
                                                        return 0
                                                    else:
                                                        print("I didn't understand understand what you're trying to say")
                                                        choice = input("Try again? YES or NO: ")
                                                elif choice == 'stop' or choice == 'STOP':
                                                    return 0
                                                
                                                elif choice == 'Fall' or choice == 'fall' or choice == 'FALL':
                                                    print()
                                                    print('You released your hold and you and the hunter fell into the water below.')
                                                    print('You and the hunter managed to leave the water to get to a shore.')
                                                    print('You both had barely survived. The hunter told you that the Dark Lord')
                                                    print('will continue to come for you unless you both put a stop to his reign.')
                                                    print('You and the hunter decided to join forces to stop the Dark Lord.')
                                                    print('As for what Reality has shown you, you had unfinished business with the Lord as well.')
                                                    print('To be continued...')
                                                    print('New Rank: Rebel')
                                                    return 0
                                                
                                                else:
                                                    print("I didn't understand understand what you're trying to say")
                                                    choice = input("What will you do? Will you CONQUER THE WORLD or FALL? ")
                                            return 0
                                                
                                        else:
                                            print("I didn't understand understand what you're trying to say")
                                            choice = input('What do you do? Will you NOT HELP HIM or HELP HIM? ')
                                            
                                    return 0
                                
                                else:
                                    print("I didn't understand understand what you're trying to say")
                                    choice = input('What will you do? Will you RUN, FIGHT, or SURRENDER? ')
                            return 0
                                
                        else:
                            print("I didn't understand understand what you're trying to say")
                            choice = input("What will you do? Will you FORCE HIM TO TELL YOU THE EXIT, NOT LISTEN TO THE MAN, or LET HIM FREE? ")
                    return 0
                       
                else:
                    print("I didn't understand understand what you're trying to say")
                    choice = input("What do you do? Will you PLEA, REFUSE, or AGREE TO BECOME A MINION? ")
                    
            return 0
                    
        else:
            print("I didn't understand understand what you're trying to say")
            choice = input("What will you do? Will you SCREAM, STRUGGLE, or be STILL? ")
    return 0
  
# CENTER PATH STORY  
def center():
    print()
    print('You walk down the center path. You are wondering about your choice,')
    print('when you come across something in your path. An iron sword lays before you.')
    print('You now have a sword in your inventory.')
    print('Suddenly, a brown bear comes into view.')
    C1 = ''
    C1 = input('What do you do? Do you: FIGHT, RUN, or PLAY DEAD? ')
    
    while(C1 != 'STOP' or C1 != 'stop'):
        
        # BAD ENDING
        if(C1 == 'FIGHT'):
            print()
            print('You fight without hesitation. Because you were a commoner and')
            print('had no experience with swords, the bear easily took you down.')
            C2 = input('Try again? YES or NO: ')
            if(C2 == 'YES'):
                adventure()
            else:
                return 0
            
        # BAD ENDING
        elif(C1 == 'RUN'):
            print()
            print('You took off running and the bear gave chase.')
            print('The bear caught you and you met your doom.')
            C3 = input('Try again? YES or NO: ')
            if(C3 == 'YES'):
                adventure()
            else:
                return 0
            
        # GOOD DECISION
        elif(C1 == 'PLAY DEAD'):
            print()
            print('You immediately fall to the ground and play dead.')
            print('The bear approached you and you waited until it lost interest to stand up.')
            print('You hurried away in case the bear decided to check again.')
            print('Suddenly, you are snatched into the air by a snare trap.')
            print('You are held upside down, about 1 foot off the ground.')
            print('You hear something coming toward you.')
            C4 = input('What do you do? Do you: CUT THE ROPE, or DEFEND YOURSELF? ')
            while(('STOP' or 'stop') not in C4):
                # BAD ENDING
                if('CUT' in C4):
                    print()
                    print("You tried to cut the rope but couldn't pull yourself upward to reach.")
                    print('You end up cutting yourself, and your injury prevents you from continuing your journey.')
                    C5 = input('Try again? YES or NO: ')
                    if(C5 == 'YES'):
                        adventure()
                    elif(C5 == 'NO'):
                        print("Oops! That's not an option! Try again.")
                        C5 = input("Try again? YES or NO: ")
                    else:
                        return 0
                    
                # GOOD DECISION
                elif('DEFEND' in C4):
                    print()
                    print('Although caught in a trap, you held the sword and prepared to fight.')
                    print("You saw that a small girl had found you, though she didn't look like a Commoner.")
                    print('She wore animal hide, and no shoes. You lower the weapon, waiting for the girl to do something.')
                    print("She sits on the ground, a few feet from you, and stares.")
                    print("You try talking to her, but she doesnt seem to understand.")
                    C6 = input('What do you do? Do you: SCARE HER, WAIT FOR SOMEONE, or OFFER THE SWORD? ')
                    while('STOP' not in C6):
                        # BAD ENDING
                        if('SCARE' or 'scare' in C6):
                            print()
                            print('You attemptted to scare the girl by shouting and swinging the sword madly.')
                            print("But the girl isn't afraid of you in the slightest. But she suddenly turns, running from something.")
                            print('You turn and see another legendary creature.')
                            print('Reality, the shapeshifting buck, meets your eyes, revealing a dark truth.')
                            print('You meet your doom sooner than expected.')
                            C7 = input('Try again? YES or NO: ')
                            if(C7 == 'YES'):
                                adventure()
                            elif(C7 == 'NO'):
                                return 0
                            else:
                                print("Oops! That's not an option! Try again.")
                                C7 = input("Try again? YES or NO: ")
                                
                            
                        # BAD ENDING
                        elif('WAIT'  or 'wait' in C6):
                            print()
                            print('Since the girl is not interested in freeing you, you wait for someone else to come along.')
                            print('Minutes turn into hours, but no one has come.')
                            print('Eventually, you pass out from all the blood rushing to your head. You could not continue your journey.')
                            C8 = input('Try again? YES or NO: ')
                            if('YES' == C8):
                                adventure()
                            elif('NO' == C8):
                                return 0
                            else:
                                print("Oops! That's not an option! Try again.")
                                C8 = input("Try again? YES or NO: ")
                            
                        # GOOD DECISION
                        elif('GIVE' or 'OFFER' or 'SWORD' in C6):
                            print()
                            print('You carefully held out the sword to the little girl.')
                            print('Her eyes gleamed with excitement at the sight of the sword.')
                            print('She approached you and took it into her hands. Then she looks at you,')
                            print('saying something in her language. She then went to a nearby tree and cut you down.')
                            print('You got to your feet and the little girl pointed down the path.')
                            print('You see Guidance was on the path. The little girl walked alongside Guidance down the path.')
                            print('You followed them and came to a small hidden clearing with a pond and apple tree.')
                            print('You then noticed how many foxes there were. The little girl beams with joy and sits as the foxes circled around her.')
                            print('You saw Guidance drink from the pond and then looked toward you.')
                            print('Her eyes said the word: Stay. She then left the clearing.')
                            print('The little girl approached you with a small fox cub. You hold the cub and she runs off to play with the foxes.')
                            print('The fox cub was whimpering and you saw a long gash on one of its legs.')
                            print('You carefully wrapped the wound. The girl called out to something.')
                            print('You turned to see a woman holding rabbits - her game from hunting.')
                            print('The little girl pointed at you and showed the sword. The woman was angry.')
                            print('She took the sword from the girl and approached you. She shoved you and you stumbled out of the clearing.')
                            print('She threw the sword in disgust and yelled out to you. She wanted you gone.')
                            C9 = input('What do you do? Do you: LEAVE, or STAY? ')
                            while('STOP' not in C9):
                                # BAD ENDING
                                if('LEAVE' in C9):
                                    print('Not wanting to upset the woman any longer, you began to head back.')
                                    print('You saw the little girl calling after you but the woman held her back.')
                                    print('As you neared your way to the fork, you came across a dangerous creature and met your doom.')
                                    C10 = input('Try again? YES or NO: ')
                                    if('YES' == C10):
                                        adventure()
                                    elif(C10 == 'NO'):
                                        return 0
                                    else:
                                        print("Oops! That's not an option! Try again.")
                                        C10 = input("Try again? YES or NO: ")
                                    
                                # GOOD DECISION
                                elif('STAY' in C9):
                                    print()
                                    print('You didn’t pick up the sword and sat down to show you didn’t want to leave.')
                                    print('The injured cub went to your lap and laid down.')
                                    print('The woman saw that you had wrapped the cub up.')
                                    print('She picked up the sword and motioned to herself, saying it was hers now.')
                                    print('You stayed with the woman, the small girl and the pack of foxes.')
                                    print('When it came dark, the woman and girl settled in a small makeshift tent.')
                                    print('You decided to stay awake for some time before you will fall asleep.')
                                    print('There was a rustling. You stood and saw the bear. It went toward the tent.')
                                    C11 = input("What do you do? Do you: FIGHT, CALL OUT WARNING or GET BEAR'S ATTENTION? ")
                                    while(('STOP' or 'stop' or 'Stop') not in C11):
                                        # BAD ENDING
                                        if(('fight' or 'Fight' or 'FIGHT') in C11):
                                            print('You tried to use the sword to fight the bear but you were no match for the beast.')
                                            print('You met your doom sooner than expected.')
                                            C12 = input('Try again? YES or NO: ')
                                            if('YES' == C12):
                                                adventure()
                                            elif(C12 == 'NO'):
                                                return 0
                                            else:
                                                print("Oops! That's not an option! Try again.")
                                                C12 = input("Try again? YES or NO: ")
                                            
                                        # BAD ENDING
                                        elif('WARNING' in C11):
                                            print()
                                            print('You tried to warn the woman and girl but they didn’t understand what you were saying.')
                                            print('They managed to escape the tent in time, but now the bear was after you.')
                                            print('You ran as fast as you could but the bear caught you easily.')
                                            print('You met your doom sooner than expected.')
                                            C13 = input('Try again? Yes or No: ')
                                            if('YES' == C13):
                                                adventure()
                                            elif(C13 == 'NO'):
                                                return 0
                                            else:
                                                print("Oops! That's not an option! Try again.")
                                                C13 = input("Try again? YES or NO: ")
                                        
                                        # GOOD DECISION
                                        elif('ATTENTION' in C11):
                                            print()
                                            print('You throw a rock at the bear and wave your arms.')
                                            print('The bear turns, and goes after you. You get a large stick and hit the bear repeatedly.')
                                            print('Suddenly, the foxes attacked the bear. The bear thrashed and roared.')
                                            print('The woman dropped from a tree above and ended the bear.')
                                            print('She threw her head back and cried out in victory. The foxes barked wildly.')
                                            print('When morning came, you had become part of the pack.')
                                            print('You found a family in the oddest place but you were happy')
                                            print('New rank: Protector')
                                            print()
                                            
                                            return 0
                                        
                                        elif(C11 == 'STOP' or C11 == 'stop'):
                                            return 0
                                            
                                        else:
                                            print("Oops! That's not an option! Try again.")
                                            C11 = input("What do you do? Do you: FIGHT, CALL OUT WARNING or GET BEAR'S ATTENTION? ")
                                            
                                    return 0
                                        
                                elif(C9 == 'STOP' or C9 == 'stop'):
                                    return 0
                                
                                else:
                                    print("Oops! That's not an option! Try again.")
                                    C9 = input('What do you do? Do you: LEAVE, or STAY? ')
                                    
                            return 0
                                    
                        elif(C6 == 'STOP' or C6 == 'stop'):
                            return 0
                        
                        else:
                            print("Oops! That's not an option! Try again.")
                            C6 = input('What do you do? Do you: SCARE HER, WAIT FOR SOMEONE, or OFFER THE SWORD? ')
                            
                    return 0
                           
                elif(C4 == 'STOP' or C4 == 'stop'):
                    return 0
                                
                else:
                    print("Oops! That's not an option! Try again.")
                    C4 = input('What do you do? Do you: CUT THE ROPE, or DEFEND YOURSELF? ')
                    
            return 0
        
        elif(C1 == 'STOP' or C1 == 'stop'):
            return 0
            
        else:
            print("Oops! That's not an option! Try again.")
            C1 = input('What do you do? Do you: FIGHT, RUN, or PLAY DEAD? ')
            
            
    return 0
    
# LEFT PATH STORY
def left():
    print('You walk down the left path. After some miles, you came across a kingdom.')
    print('The kingdom was named Haven. You heard stories of Haven from your village.')
    print('It was a prosperous kingdom that had monsters, vikings, and beings from another world.')
    print('It was an enchanting place, but only some people are allowed inside.')
    print('No one ever left Haven, but it was a dream land and paradise.You happen upon the gate of Haven.')
    print('Guidance stood there, waiting for you. The gate opens and she guides you inside.')
    print('You followed her through the woods and she stopped at the treeline. You went to a local village.')
    print('The houses were white stone and the streets were paved with gray bricks. The locals were as the rumors said.')
    print('Some had green scalded skin with snake eyes and horns. Others had fair skin colored purple,')
    print('their noses resembled triangles and their eyes that shimmered like the galaxy.')
    print('Some locals even had wings like angel or were made of dark matter said to be ink.')
    print('You didn’t get too far into the village before soldiers stopped you. You were trespassing.')
    choose = input("What will you do? SAY YOU WERE LOST or TELL THEM ABOUT GUIDANCE? ")
    while(choose != 'STOP' or choose != 'stop'):
        if choose == 'SAY YOU WERE LOST' or choose == 'say you were lost':
            print()
            print('You said you were lost but they didn’t care about your excuse.')
            print('They forced you out the Kingdom and you had no choice but to return home.')
            print('On your way back you encountered a dangerous creature and your doom came sooner than expected.')
            choose = input('Try again? YES or NO: ')
            while(choose != 'STOP' or choose != 'stop'):
               if choose == 'yes' or choose == 'YES' or choose == 'Y' or choose == 'y':
                   adventure()
               elif choose == 'no' or choose == 'NO' or choose == 'N' or choose == 'n':
                   return 0
               else:
                   print("I didn't understand understand what you're trying to say")
                   choose = input("Try again? YES or NO: ")
            return 0
        elif choose == 'TELL THEM ABOUT GUIDANCE' or choose == 'tell them about guidance':
            print('')
            print('Although the attempt seems far-fetched, you told them about Guidance.')
            print('The soldiers looked to each other then to you. They took you to the castle.')
            print('The castle was made of marble, stone and gold.')
            print('The throne room was small and had soldiers stationed on either side.')
            print('On the thrones were a King and Queen. King Michael of Haven sat beise his wife, Queen Maria.')
            print('The King asked why you had come here. You told them about Guidance.')
            print('The Queen then spoke to you. She knew what had led you here,')
            print('she wanted to know why you chose to follow Guidance. You take a moment to find the right words.')
            print('You tell the royals that you were a commoner and had no clue of what to do before he grew old.')
            print('You wanted adventure. The Queen’s eyes held understanding. The King, however, told you that there was nothing for you here.')
            print('The Queen spoke softly to the King about something.')
            print('The soldiers left your side and the Queen approached you. She told you to follow her.')
            print('She led you to the courtyard where there were peach trees and a fountain.')
            print('She told you she understood how you felt about adventure.')
            print('She herself loved adventures, but had to remain at the castle to stay by her husband.')
            print('She turned to you and asked if you knew how to write. You told her yes and she offered you a deal.')
            print('If you do something for her, she will let you remain in Haven.')
            choose = input('What do you do? HIDE, FIGHT, or HELP?: ')
            while(choose != 'STOP' or choose != 'stop'):
                if choose == 'HIDE' or choose == 'hide':
                    print()
                    print('You stayed in your room and watched as countless citizens met their doom.')
                    print('The remaining citizens were outmatched by the number of invaders and the kingdom perished.')
                    print('You were not able to finish the story.')
                    choose = input('Try again? YES or NO: ')
                    while(choose != 'STOP' or choose != 'stop'):
                        if choose == 'yes' or choose == 'YES' or choose == 'Y' or choose == 'y':
                            adventure()
                        elif choose == 'no' or choose == 'NO' or choose == 'N' or choose == 'n':
                            return 0
                elif choose == 'FIGHT' or choose == 'fight':
                    print()
                    print('Believing you knew how to fight, you tried to attack one of the nightmarish beings.')
                    print('However, you soon found it impossible because they were fast, dangerous,')
                    print('and their touch burned like acid in contact with your skin. You became overwhelmed and met your doom.')
                    choose = input('Try again? YES or NO: ')
                    while(choose != 'STOP' or choose != 'stop'):
                        if choose == 'yes' or choose == 'YES' or choose == 'Y' or choose == 'y':
                            adventure()
                        elif choose == 'no' or choose == 'NO' or choose == 'N' or choose == 'n':
                            return 0
                        else:
                           print("I didn't understand understand what you're trying to say")
                           choose = input("Try again? YES or NO: ")
                        return 0
                elif choose == 'HELP' or choose == 'help':
                    print()
                    print('Although you wanted to fight these creatures, you remembered how dangerous this place is compared to outside the kingdom.')
                    print(' You ran to the village and helped evacuate the families to the castle.')
                    print('As you were doing this, you caught sight of ten individuals.')
                    print('Two monsters, two other-worlders, two vikings, three soldiers, and the Queen.')
                    print('The Queen wore armor that resembled gold and glowed like ambers.')
                    print('You watched in awe as they began to fight. The monsters were strong and crushed the invaders with their bare hands.')
                    print('The other-worlders would screech high pitches that damaged the creatures.')
                    print('The vikings were ruthless and slayed by the dozen. Two of the soldiers had wings like angels and used strings of light.')
                    print('The remaining soldiers had magic and power.')
                    print('The Queen was fearless and fought alongside them. After the fight, the Kingdom fell to a hush.')
                    print('The next day, the Queen called you to the garden. She sat before the fountain.')
                    print('You then noticed her physique and how ill she seemed. She told you it was time for the last story.')
                    print('She told you about becoming Queen and the cost she paid to save the Kingdom.')
                    print('After writing the book, she told you to take the book as far as possible from the Kingdom and to never return.')
                    choose = input('What do you do? STAY or LEAVE: ')
                    while(choose != 'STOP' or choose != 'stop'):
                        if choose == 'STAY' or choose == 'stay':
                            print()
                            print('In spite of the Queen’s wishes, you choose to remain in the Kingdom.')
                            print('You and the Kingdom then faced the end of the world as was fated for Haven.')
                            print('You suffered your doom among the ashes of the Kingdom.')
                            choose = input('Try again? YES or NO: ')
                            while(choose != 'STOP' or choose != 'stop'):
                                if choose == 'yes' or choose == 'YES' or choose == 'Y' or choose == 'y':
                                    adventure()
                                elif choose == 'no' or choose == 'NO' or choose == 'N' or choose == 'n':
                                    return 0
                                else:
                                   print("I didn't understand understand what you're trying to say")
                                   choose = input("Try again? YES or NO: ")
                                return 0
                        elif choose == 'LEAVE' or choose == 'leave':
                            print()
                            print('You took the book and left Haven. You had no clue where you would go, but you took the book as far away as possible.')
                            print('You found a place to keep the book. A cave underside of the mountains, you set the book covered in cloth.')
                            print('You left the mountain and saw in the distance the end of the world. The Kingdom had fallen for all of its inhabitants.')
                            print('You wandered the world in search of stories. You found it strange that no time passed for you.')
                            print('Before you knew it, centuries had passed. You had written many stories, but it did not compare to the ones in Haven.')
                            print('You were walking through a forest and came upon a castle. A girl sat before a stone water fountain.')
                            print('She turned to you and you were taken aback. The girl smiled softly and asked if you could write for her.')
                            print()
                            return 0
                        else:
                            print("I didn't understand understand what you're trying to say")
                            choose = input('What will you do? Will you STAY or LEAVE? ')
                    return 0
                else:
                    print("I didn't understand understand what you're trying to say")
                    choose = input('What will you do? Will you HIDE, FIGHT, or HELP? ')
            return 0
        else:
            print("I didn't understand understand what you're trying to say")
            choose = input("What do you do? Will you SAY YOU WERE LOST or TELL THEM ABOUT GUIDANCE? ")
    return 0

# Play the Adventure game
def adventure():
    # Instructions
    print()
    print('Welcome to Choose your own Adventure!')
    print('The goal of the game: Follow the path Fate has set out for you, or meet your own destruction!')
    print('You play by typing in your chosen path/choice in the provided space. Options are in ALL CAPS.')
    print('If you want to leave at any time, enter the word STOP. Enjoy!')
    print()
    
    print('Our story begins with a local legend of a mystical doe called Guidance.')
    print('This doe is rarely seen, but can be found deep within the forest.')
    print('Some have said that Guidance leads people to their fate. Others, their doom.')
    print('One day, you, a Commoner, happen upon her.')
    print('She meets your eyes, and you follow her, beckoned by her gaze.')
    print('She leads you to the edge of the forest, and stops at a fork.')
    print('Three paths lay before you, carved by the footsteps of generations past.')
    print('This is where your story begins…')
    
    # Counter to check if need to break out of loop
    count = -1
    choice = ''
    
    while(choice != 'STOP' or choice != 'stop'):
        # Playing the Game
        choice = input('Which path do you take? RIGHT, LEFT, or CENTER? ')
        # RIGHT PATH
        if(choice == 'RIGHT' or choice == 'right' or choice == 'Right'):
            count = right()
            if(count == 0):
                break
            
        # CENTER PATH
        elif(choice == 'CENTER' or choice == 'center' or choice == 'Center'):
            count = center()
            if(count == 0):
                break
            
        # LEFT PATH
        elif(choice == 'LEFT' or choice == 'left' or choice == 'Left'):
            count = left()
            if(count == 0):
                break

        elif(choice == 'STOP' or choice == 'stop'):
            break
        
        else:
            print("Oops! That's not an option! Try again.")
            print()
            
    # Exiting the Game
    print()
    print('Thanks for playing Choose your own Adventure!')
    print()
    main_menu()

# GAME 2 - WORDSEARCH ########################################################

# Show the board
def display(words):
    for i in words:
        print(' ', end = '')
        for j in i:
            if(j != i[-1]):
                print(j, end = ' ')
            else:
                print(j)

# Function to color the words SIMPLY
def color_it(words, row, col):
    words[row][col] = Fore.RED + Style.BRIGHT + words[row][col] + Fore.RESET

# Color the words
def update(words, k=0):
    # RESET
    if(k == 0):
        words = Fore.RESET
    # MAROON
    if(k == 1):
        color_it(words, 7, 0)
        color_it(words, 8, 0)
        color_it(words, 9, 0)
        color_it(words, 10, 0)
        color_it(words, 11, 0)
        color_it(words, 12, 0)
    # AGGIELAND
    if(k == 2):
        color_it(words, 13, 1)
        color_it(words, 12, 2)
        color_it(words, 11, 3)
        color_it(words, 10, 4)
        color_it(words, 9, 5)
        color_it(words, 8, 6)
        color_it(words, 7, 7)
        color_it(words, 6, 8)
        color_it(words, 5, 9)
    # TRADITION
    if(k == 3):
        color_it(words, 10, 2)
        color_it(words, 9, 3)
        color_it(words, 8, 4)
        color_it(words, 7, 5)
        color_it(words, 6, 6)
        color_it(words, 5, 7)
        color_it(words, 4, 8)
        color_it(words, 3, 9)
        color_it(words, 2, 10)  
    # HOWDY
    if(k == 4):
        color_it(words, 3, 2)
        color_it(words, 4, 2)
        color_it(words, 5, 2)
        color_it(words, 6, 2)
        color_it(words, 7, 2)
    # FIGHT
    if(k == 5):
        color_it(words, 1, 1)
        color_it(words, 1, 2)
        color_it(words, 1, 3)
        color_it(words, 1, 4)
        color_it(words, 1, 5)
    # GIGE1M
    if(k == 6):
        color_it(words, 1, 3)
        color_it(words, 2, 3)
        color_it(words, 3, 3)
        color_it(words, 4, 3)
        color_it(words, 5, 3)   
    # FARMERS
    if(k == 7):
        color_it(words, 0, 7)
        color_it(words, 0, 8)
        color_it(words, 0, 9)
        color_it(words, 0, 10)
        color_it(words, 0, 11)
        color_it(words, 0, 12)
        color_it(words, 0, 13)
    # WHOOP
    if(k == 8):
        color_it(words, 3, 7)
        color_it(words, 3, 8)
        color_it(words, 3, 9)
        color_it(words, 3, 10)
        color_it(words, 3, 11)
    # FAMILY
    if(k == 9):
        color_it(words, 11, 8)
        color_it(words, 10, 9)
        color_it(words, 9, 10)
        color_it(words, 8, 11)
        color_it(words, 7, 12)
        color_it(words, 6, 13)
    # RELLIS
    if(k == 10):
        color_it(words, 5, 12)
        color_it(words, 6, 12)
        color_it(words, 7, 12)
        color_it(words, 8, 12)
        color_it(words, 9, 12)
        color_it(words, 10, 12)
    # CADETS
    if(k == 11):
        color_it(words, 12, 8)
        color_it(words, 12, 9)
        color_it(words, 12, 10)
        color_it(words, 12, 11)
        color_it(words, 12, 12)
        color_it(words, 12, 13)
    # REVEILLE
    if(k == 12):
        color_it(words, 13, 4)
        color_it(words, 13, 5)
        color_it(words, 13, 6)
        color_it(words, 13, 7)
        color_it(words, 13, 8)
        color_it(words, 13, 9)
        color_it(words, 13, 10)
        color_it(words, 13, 11)

# Play the WordSearch
def wordsearch():
    # The wordsearch puzzle
    row01 = ['T','V','C','D','A','Q','Y','F','A','R','M','E','R','S']
    row02 = ['M','F','I','G','H','T','K','D','X','P','L','A','D','R']
    row03 = ['C','E','Q','I','N','P','S','C','W','Y','N','V','F','O']
    row04 = ['F','D','H','G','T','F','V','P','O','O','H','W','R','S']
    row05 = ['K','Y','O','E','K','L','J','M','I','H','U','C','I','D']
    row06 = ['H','I','W','M','D','B','O','T','V','D','R','L','R','N']
    row07 = ['J','B','D','U','G','W','I','S','N','T','L','O','E','Y']
    row08 = ['M','X','Y','E','G','D','Z','A','J','A','L','R','L','I']
    row09 = ['A','Q','H','F','A','O','L','R','N','S','D','I','L','P']
    row10 = ['R','O','v','R','D','E','V','U','G','L','M','C','I','T']
    row11 = ['O','L','T','P','I','F','W','O','N','A','X','T','S','V']
    row12 = ['O','K','E','G','B','S','Q','P','F','J','Y','L','O','H']
    row13 = ['N','Y','G','Z','Y','I','L','H','C','A','D','E','T','S']
    row14 = ['C','A','O','X','R','E','V','E','I','L','L','E','F','Q']
    
    complete = [row01, row02, row03, row04, row05, row06, row07, row08, row09, row10, row11, row12, row13, row14]
    
    # User input
    userWord = ''
    
    # How to update the board color
    key = 0
    
    # Booleans and counter to check all 12 words have been found, and are found ONCE
    count = 0
    word1 = False
    once1 = False
    
    word2 = False
    once2 = False
    
    word3 = False
    once3 = False
    
    word4 = False
    once4 = False
    
    word5 = False
    once5 = False
    
    word6 = False
    once6 = False
    
    word7 = False
    once7 = False
    
    word8 = False
    once8 = False
    
    word9 = False
    once9 = False
    
    word10 = False
    once10 = False
    
    word11 = False
    once11 = False
    
    word12 = False
    once12 = False
    
    allTrue = word1 and word2 and word3 and word4 and word5 and word6 and word7 and word8 and word9 and word10 and word11 and word12
    
    # Instructions
    print()
    print('Welcome to The 12th Man Wordsearch! Brought to you by Audry Estrada.')
    print('The goal of the game: Identify all 12 words hidden in the wordsearch.')
    print('You play by typing any word you find in the provided space.')
    print('If you want to leave at any time, enter the word STOP. Enjoy!')
    print()
    
    # Display the game
    display(complete)
    
    # Play the Game until all 12 words found
    while(not(allTrue) and count < 12):
        
        # User input
        userWord = input('Enter a word: ')
        
        # MAROON
        if(userWord in ['MAROON', 'maroon']):
            if(once1 == False):
                print('Success! You have found ' + userWord + '\n')
                word1 = not(word1)
                once1 = True
                key = 1
                count += 1
            else:
                count += 0
            
        # AGGIELAND   
        elif(userWord in ['AGGIELAND', 'aggieland']):
            if(once2 == False):
                print('Success! You have found ' + userWord + '\n')
                word2 = not(word2)
                once2 = True
                key = 2
                count += 1
            else:
                count += 0
            
        # TRADITION
        elif (userWord in ['TRADITION', 'tradition']):
            if(once3 == False):
                print('Success! You have found ' + userWord + '\n')
                word3 = not(word3)
                once3 = True
                key = 3
                count += 1
            else:
                count += 0
            
        # HOWDY
        elif (userWord in ['HOWDY', 'howdy']):
            if(once4 == False):
                print('Success! You have found ' + userWord + '\n')
                word4 = not(word4)
                once4 = True
                key = 4
                count += 1
            else:
                count += 0
            
        # FIGHT
        elif (userWord in ['FIGHT', 'fight']):
            if(once5 == False):
                print('Success! You have found ' + userWord + '\n')
                word5 = not(word5)
                once5 = True
                key = 5
                count += 1
            else:
                count += 0
            
        # GIGEM
        elif (userWord in ['GIGEM', 'gigem']):
            if(once6 == False):
                print('Success! You have found ' + userWord + '\n')
                word6 = not(word6)
                once6 = True
                key = 6
                count += 1
            else:
                count += 0
            
        # FARMERS
        elif (userWord in ['FARMERS', 'farmers']):
            if(once7 == False):
                print('Success! You have found ' + userWord + '\n')
                word7 = not(word7)
                once7 = True
                key = 7
                count += 1
            else:
                count += 0
            
        # WHOOP
        elif (userWord in ['WHOOP', 'whoop']):
            if(once8 == False):
                print('Success! You have found ' + userWord + '\n')
                word8 = not(word8)
                once8 = True
                key = 8
                count += 1
            else:
                count += 0
            
        # FAMILY
        elif (userWord in ['FAMILY', 'family']):
            if(once9 == False):
                print('Success! You have found ' + userWord + '\n')
                word9 = not(word9)
                once9 = True
                key = 9
                count += 1
            else:
                count += 0
            
        # RELLIS
        elif (userWord in ['RELLIS', 'rellis']):
            if(once10 == False):
                print('Success! You have found ' + userWord + '\n')
                word10 = not(word10)
                once10 = True
                key = 10
                count += 1
            else:
                count += 0
            
        # CADETS
        elif (userWord in ['CADETS', 'cadets']):
            if(once11 == False):
                print('Success! You have found ' + userWord + '\n')
                word11 = not(word11)
                once11 = True
                key = 11
                count += 1
            else:
                count += 0
        
        # REVEILLE
        elif(userWord in ['REVEILLE', 'reveille']):
            if(once12 == False):
                print('Success! You have found ' + userWord + '\n')
                word12 = not(word12)
                once12 = True
                key = 12
                count += 1
            else:
                count += 0
        
        # LEAVE THE WORDSEARCH
        elif(userWord == 'STOP' or userWord == 'stop'):
            break
            
        # WRONG WORD    
        else:
            print("Oops! That's not a word hidden in The 12th Man Wordsearch! Try again.")
            print()
        
        # MAIN MENU & RESET
        update(complete, key)    
        print(count, 'out of 12 words!')
        print()
        display(complete)
            
    # Exiting the game
    update(complete)
    print()
    print('Thanks for playing The 12th Man Wordsearch!')
    print()
    main_menu()
                
# GAME 3 - TRIVIA ############################################################

# Ask the question until answered
def question(question, key):
    ans = ''
    print(question)
    ans = input('Enter a name: ')
    if(ans == 'STOP' or ans == 'stop'):
        return 0
    else:
        while ans not in key:
            print("Oops! That's not the right character! Try again.")
            print()
            print(question)
            ans = input('Enter a name: ')
            if(ans == 'STOP' or ans == 'stop'):
                return 0
    print('Success! You have named ' + ans)
    print()

# Play the Trivia Game
def trivia():
    # Counter to check all questions are answered
    counter = 0
    
    # Bonus counter and input
    bonusAns = ''
    bonus= 0
    
    # Instructions
    print()
    print('Welcome to Disney Trivia!')
    print('The goal of the game: Name the correct Disney character for 20 different movies.')
    print("You will be given a Supporting character description, and you must identify them.")
    print('You play by typing any name you think of in the provided space.')
    print('If you want to leave at any time, enter the word STOP. Enjoy!')
    print()
    
    # Play the Game
    while counter < 20 and bonus < 10:
        # CINDERELLA
        num1 = question('Cinerella had many friends, but these 2 were key in rescuing her. Can you remember one of them?', ['JAQ', 'jaq', 'GUS GUS', 'gus gus', 'GUS', 'gus', 'GUSGUS', 'gusgus'])
        if(num1 == 0):
            break
        else:
            counter += 1
            
        # CARL FREDRICKSEN
        num2 = question('Carl Fredricksen and this person had one crazy adventure over in South America. Who is this Wilderness Explorer?', ['RUSSELL', 'russell'])
        if(num2 == 0):
            break
        else:
            counter += 1
        
        # ALADDIN
        num3 = question('Aladdin had the help of 2 creatures on his way to become Prince Ali. Can you remember one of them?', ['ABU', 'abu', 'GENIE', 'genie'])
        if(num3 == 0):
            break
        else:
            counter += 1
            
        # MULAN
        num4 = question("Mulan's guardian? Small, and travel-size for conveinience.", ['MUSHU', 'mushu'])
        if(num4 == 0):
            break
        else:
            counter += 1
        
        # EMPEROR KUZCO
        num5 = question('Emperor Kuzco learned humilty from this person. Who taught him to stop being selfish?', ['PACHA', 'pacha'])
        if(num5 == 0):
            break
        else:
            counter += 1
        
        # SULLEY
        num6 = question("Sulley's best friend, with a penchant for wanting to put Boo back where she came from. What's his name?", ['MIKE', 'mike', 'MIKE WAZOWSKI', 'mike wazowski', 'MIKEWAZOWSKI', 'mikewazowski'])
        if(num6 == 0):
            break
        else:
            counter += 1
            
        # LILO
        num7 = question("Lilo's friend and Nani's terror, mistaken for a dog?", ['STITCH', 'stitch'])
        if(num7 == 0):
            break
        else:
            counter += 1
            
        # JIM HAWKINS
        num8 = question('Jim Hawkins had many allies who helped him as he sought out treasure. Can you remember one of their names?', ['BEN', 'ben', 'DOPPLER', 'doppler', 'DR DOPPLER', 'dr doppler', 'DRDOPPLER', 'drdoppler'])
        if(num8 == 0):
            break
        else:
            counter += 1
            
        # LIGHTNING MCQUEEN
        num9 = question("Lightning McQueen's first friend, with a habit of driving backwards?", ['MATER', 'mater', 'TOW MATER', 'tow mater', 'TOWMATER', 'towmater'])
        if(num9 == 0):
            break
        else:
            counter += 1
        
        # MR INCREDIBLE
        num10 = question("Mr. Incredible could trust this super with his life. Who is this ultra-cool hero?", ['FROZONE', 'frozone'])
        if(num10 == 0):
            break
        else:
            counter += 1
        
        # BOLT
        num11 = question("Bolt's #1 fan? Small for size, but big in heart. No matter what comes his way, he will roll with the punches. Who is he?", ['RHINO', 'rhino'])
        if(num11 == 0):
            break
        else:
            counter += 1
        
        # BAMBI
        num12 = question("Bambi's best friend, who taught him to talk and skate on ice. Who is this character?", ['THUMPER', 'thumper'])
        if(num12 == 0):
            break
        else:
            counter += 1
        
        # WINNIE THE POOH
        num13 = question('Winnie the Pooh would often visit this fretful little person in the Hundred-Acre Wood. Who is he?', ['PIGLET', 'piglet'])
        if(num13 == 0):
            break
        else:
            counter += 1
        
        # ARIEL
        num14 = question("Ariel routinely told this person not to be a guppy. Can you name this fearful fish?", ['FLOUNDER', 'flounder'])
        if(num14 == 0):
            break
        else:
            counter += 1
        
        # HERCULES
        num15 = question("Hercules wouldn't have become a hero without this person's guidance. Who is this Satyr?", ['PHIL', 'phil'])
        if(num15 == 0):
            break
        else:
            counter += 1
        
        # ROBIN HOOD
        num16 = question("Robin Hood's right-hand man, who rescued him from execution. One of the heroes of the Animal Kingdom. Can you remember his name?", ['LITTLE JOHN', 'little john', 'LITTLEJOHN', 'littlejohn'])
        if(num16 == 0):
            break
        else:
            counter += 1
        
        # MARLIN
        num17 = question('Marlin met this forgetful fish on his way to find Nemo. Who is she?', ['DORY', 'dory'])
        if(num17 == 0):
            break
        else:
            counter += 1
        
        # SIMBA
        num18 = question('Simba made 2 friends in his exile, who taught him all about living a carefree life. Can you name one of them?', ['TIMONE', 'timone', 'PUMBA', 'pumba'])
        if(num18 == 0):
            break
        else:
            counter += 1
        
        # WALL-E
        num19 = question('WALL-E made a friend on the AXIOM, who faithfully followed his trail of dirt. Who is he?', ['MO', 'mo'])
        if(num19 == 0):
            break
        else:
            counter += 1
        
        # ALICE
        num20 = question('Alice followed the advice of this creature all the way to the Queen of Hearts. Who is this fiendish feline?', ['CHESHIRE CAT', 'cheshire cat', 'CHESHIRECAT', 'cheshirecat'])
        if(num20 == 0):
            break
        else:
            counter += 1
            
        bonusAns = input('Excellent! You found all 20 characters! Interested in a Bonus Round? Yes or No: ')
        print()
        
        # Bonus Round Instructions
        if(bonusAns == ('YES' or 'yes' or 'y' or 'Yes')):
            print('Welcome to Disney Trivia: Bonus Round!')
            print('The goal of the game: Name the correct Disney character for 10 different movies')
            print('You will be given a Villan-Minion character description, and you must identify them.')
            print('You play by typing any name you think of in the provided space.')
            print('If you want to leave at any time, enter the word STOP. Enjoy!')
            print()
            
            # YZMA
            bonus1 = question("Yzma's henchman? Talks to squirrels, his conscience, and random strangers.", ['KRONK', 'kronk'])
            if(bonus1 == 0):
                break
            else:
                bonus += 1
            
            # HADES
            bonus2 = question('Hades had 2 little minions, well suited to their names. Can you name one of them?', ['PAIN', 'pain', 'PANIC', 'panic'])
            if(bonus2 == 0):
                break
            else:
                bonus += 1
            
            # URSULA
            bonus3 = question("Ursula's 2 pets, who ruined Ariel's date with Prince Eric. Can you recall one of their names?", ['FLOTSOM', 'flotsom', 'JETSUM', 'jetsum'])
            if(bonus3 == 0):
                break
            else:
                bonus += 1
            
            # RATIGAN
            bonus4 = question("Professor Ratigan's errand boy, with a crippled wing and peg-leg?", ['FIDGET', 'fidget'])
            if(bonus4 == 0):
                break
            else:
                bonus += 1
            
            # SYNDROME
            bonus1 = question("Syndrome's girlfriend?", ['MIRAGE', 'mirage'])
            if(bonus1 == 0):
                break
            else:
                bonus += 1
            
            # MR. WATERNOOSE
            bonus1 = question('A color-changing lizard, who worked for Mr. Waternoose. Second-best scarer?', ['RANDALL', 'randall'])
            if(bonus1 == 0):
                break
            else:
                bonus += 1
            
            # JAFAR
            bonus1 = question("Jafar's pet, and a very colorful bird. Who is he? ", ['IAGO', 'iago'])
            if(bonus1 == 0):
                break
            else:
                bonus += 1
            
            # GASTON
            bonus1 = question("Gaston's minion, with a big nose and small stature. Do you know who he is?", ['LEFOU', 'lefou'])
            if(bonus1 == 0):
                break
            else:
                bonus += 1
            
            # AUTO
            bonus1 = question("Auto used this little robot against EVE and WALL-E. Can you name him?", ['GOPHER', 'gopher'])
            if(bonus1 == 0):
                break
            else:
                bonus += 1
            
            # SILVER
            bonus1 = question("One of Silver's pirates, responsible for the death of Mr. Arrow. Who is this nemisis to Jim Hawkins?", ['SCROOP', 'scroop', 'MR SCROOP', 'mr scroop', 'MRSCROOP', 'mrscroop'])
            if(bonus1 == 0):
                break
            else:
                bonus += 1
                
            print('Sucess! You have named all 10 characters!')
                
        else:
            break
    
    # Exiting the Game
    print()
    print('Thanks for playing Disney Trivia!')
    print()
    main_menu()
        
# MAIN MENU ##################################################################
def main_menu():
    # General Instructions
    print('Howdy! Welcome to the Engineering Arcade Main Menu!')
    print('Here, we have three games for you to choose from:')
    print('A) Choose your own Adventure!')
    print('B) The 12th Man WordSearch!')
    print('C) Disney Trivia!')
    print('Enter the Game option letter to play it!')
    print('Otherwise, enter STOP to exit the Arcade.')
    
    user = input('Which game do you choose? ')
    
    # Check the user inputs a letter, not a number
    try:
        check = user + 15
        
    # HUZZAH! They've entered a letter!
    except TypeError:
        # ADVENTURE
        if ((user == 'A') or (user == 'a')):
            adventure()
            
        # WORDSEARCH
        elif((user == 'B') or (user == 'b')):
            wordsearch()
            
        # TRIVIA
        elif((user == 'C') or (user == 'c')):
            trivia()
            
        # EXIT
        elif((user == 'STOP') or (user == 'stop')):
            print('Aww! Thanks for playing! Come back soon!')
            return 0
        
        else:
            print("Oops! That isn't one of the options! Try again.")
            print()
            main_menu()
        
        
# ACCESS THE ARCADE ##########################################################
main_menu()