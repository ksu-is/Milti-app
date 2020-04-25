import random
import os
import sys
from time import *

answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'You may rely on it', 'My sources say no', 'Outlook not so good', 'Very doubtful']
def Magic8Ball():
    print('What is your question? (q to quit) ')
    print()
    reply = input()
    if reply == "q":
        restart()
    else:
        print(reply)
        print (answers[random.randint(0, len(answers)-1)] )
        print()
        Replay()
    
def Replay():
    Magic8Ball()

def madlibs():
    adjective1=input("type an adjective: ")
    adjective2=input("type an adjective: ")
    noun1=input("type a noun: ")
    noun2=input("type a noun: ")
    pluralnoun1=input("type a plural noun: ")
    game=input("name a game: ")
    pluralnoun2=input("type a plural noun: ")
    verb1=input("type a verb ending in 'ing': ")
    verb2=input("type a verb ending in 'ing': ")
    pluralnoun3=input("type a plural noun: ")
    verb3=input("type a verb ending in 'ing': ")
    noun3=input("type a noun: ")
    plant=input("name a type of plant: ")
    partofbody=input("name a body part: ")
    place=input("name a place: ")
    verb4=input("type a verb ending in 'ing': ")
    adjective3=input("name a adjective: ")
    number=input("type a number: ")
    pluralnoun4=input("type a plural noun: ")
    print()
    print("A vacation is when you take a trip to some", adjective1, "place with your", adjective2, "family.\nUsually you go to some place that is near a/an", noun1, "or up on a/an", noun2,".\nA good vacation place is one where you can ride", pluralnoun1, "or play", game,"or go hunting for",pluralnoun2,".\nI like to spend my time", verb1, "or", verb2,".\nWhen parents go on vacation, they spend their time eating three", pluralnoun3, "a day, and fathers play golf, and mothers sit around", verb3,".\nLast summer, my little brother fell in a/an", noun3, "and got poison", plant, "all over his", partofbody,".\nMy family is going to go to the", place, ", and I will practice" ,verb4,".\nParents need vacations more than kids because parents are always very", adjective3, "and because they have to work", number,"hours every day all year making enough", pluralnoun4, "to pay for the vacation.")
    print()
    restart()

def madlib2():
    item=input("Enter an object: ")
    person=input("Enter a person: ")
    activity1=input("Enter an activity: ")
    state=input("Enter a state: ")
    activity2=input("Enter an activity: ")
    time=input("Enter a time: ")
    name2=input("Enter a name: ")
    name3=input("Enter a name: ")
    name4=input("Enter a name: ")
    number=input("Enter a number: ")
    action=input("Entery an action: ")
    print()
    print("It is the year 2020. A new virus called Corona has taken over the", item,".", person, "has told you today is your last day of freedom. What will you do? You decide to go", activity1, "drive to", state, "and go", activity2, ". Fast forward....... it is", time, "o’clock. You last adventure for the day is dinner with" ,name2, name3, "and", name4, ". You all go to restaurant and order", number, "of everything on the menu! As the day come to an end you decide to take a risk and", action, "a puppy! *Gasp* Well hopefully you enjoyed your freedom!")
    print()
    restart()

def madlibs_start():
    print ("Pick a story")
    print()
    print ("Funny vacation story: press 1")
    print ("Worst bedtime story: press 2")
    print("Conrona: press 4 ")
    print("Quit: press q")
    story = input('story: ')
    if story == '1': 
        madlibs()
    elif story == '2':    
        madlibs2()
    elif story == 'q':
        clrscr()
        restart()
    else:
        print("Pick a number or q to quit.")

#  classic game - Rock, Paper, Scissors
#  tuples list of win combinations
WIN_LIST_RPS = [('ROCK', 'SCISSORS'),  # who can be defeated by ROCK
                ('SCISSORS', 'PAPER'),  # who can be defeated by SCISSORS
                ('PAPER', 'ROCK')]  # who can be defeated by PAPER

SELECTIONS_LIST_RPS = ['ROCK', 'PAPER', 'SCISSORS']

#  an expansion of classic game - Rock, Paper, Scissors, Lizard, Spock
#  tuples list of win combinations
WIN_LIST_RPSLS = [('ROCK', 'SCISSORS'), ('ROCK', 'LIZARD'),  # who can be defeated by ROCK
                  ('SCISSORS', 'LIZARD'), ('SCISSORS', 'PAPER'),  # who can be defeated by SCISSORS
                  ('LIZARD', 'PAPER'), ('LIZARD', 'SPOCK'),  # who can be defeated by LIZARD
                  ('PAPER', 'SPOCK'), ('PAPER', 'ROCK'),  # who can be defeated by PAPER
                  ('SPOCK', 'ROCK'), ('SPOCK', 'SCISSORS')]  # who can be defeated by SPOCK

#  list of selections
SELECTIONS_LIST_RPSLS = ['ROCK','PAPER','SCISSORS','LIZARD','SPOCK']

#  Corona version
#  tuples list of win combinations
WIN_LIST_RPSLS = [('CORONA', 'STUPID'), ('CORONA', 'NO MASK'),  # who can be defeated by CORONA
                  ('MASK', 'CORONA'), ('MASK', 'NO MASK'), # who can be defeated by MASK
                  ('NO MASK', 'STUPID')]  # who can be defeated by NO MASK
                  

#  list of selections
SELECTIONS_LIST_RPSLS = ['CORONA','MASK','NO MASK','STUPID']


#  dictionary that saves wins of both player and computer, and ties
stats_count = {'player':0, 'computer':0, 'ties':0}

def clrscr():
  """ Clears the console in order to make a more pleasant game """
  if os.name == "posix":  # compatible with Unix/Linux/MacOS/BSD/etc
    os.system('clear')
  elif os.name in ("nt", "dos", "ce"):  # compatible with DOS/Windows
    os.system('CLS')

def RPS():
    """ Main menu """
    clrscr()
    while True:
        option = input(
        "-------------- Welcome to my Rock-Paper-Scissors based Games ------------------"
        "\n  [1] - (Classic) Rock Paper Scissors                                          "
        "\n  [2] - (Expansion) Rock Paper Scissors Lizard Spock                           "
        "\n  [3] - (NEW) CORONA 2020                                                      "
        "\n  [4] - Home                                                                   "                   
        "\n-------------------------------------------------------------------------------"
        "\n Please select an option (1, 2, or 3): ")
        if option == '1' or option == '2' or option == '3':  #  if options 1, 2 or 3 are selected, it will call lets_play function
            lets_play(option)
        elif option == '4':  # if option is 4, exits the program
            print("Bye bye")
            exit()
        else:  #  if there's an invalid option, the menu will start again
            input("Invalid option. Try again... Please press ENTER to continue")
            clrscr()
    
def lets_play(option):
  """ A function that sets which game is going to be played based on the option selected """
  clrscr()
  
  if option == '1':  #  if option 1 is selected, it will play Rock + Paper + Scissors game
    intro = (" Welcome to Rock + Paper + Scissors game!")  
    option_help = ("\n This game is simple and goes as following:"  
          "\n *You can choose between: Rock, Paper or Scissors."
          "\n\n You must take in consideration that:"
          "\n *Rock crushers Scissors."
          "\n *Scissors cut Paper."
          "\n *Paper covers Rock."
          "\n\n Notes: *The first one that scores 5 points WINS the game!"
          "\n        *If you forgot the rules, just type 'help'."
          "\n        *If you want to go to main menu to try the other games, just type 'quit'."
          "\n        *If you want to exit because you're afraid of loosing, just type 'exit' you coward!\n")
    selections_list = SELECTIONS_LIST_RPS  #  selections are assigned based on the game
    win_list = WIN_LIST_RPS  #  win list is assigned based on the game
  
  elif option == '2':  #  if option 2 is selected, it will play Rock + Paper + Scissors + Lizard + Spock game
    intro = (" Welcome to Rock + Paper + Scissors + Lizard + Spock game!")
    option_help = ("\n This game is simple and goes as following:"
          "\n *You can choose between: Rock, Paper, Scissors, Lizard or Spock."
          "\n\n You must take in consideration that:"
          "\n *Rock crushers Scissors and Lizard."
          "\n *Scissors cut Paper and decapitate Lizard."
          "\n *Lizard eats Paper and poisons Spock."
          "\n *Paper disproves Spock and covers Rock."
          "\n *Spock vaporizes Rock and smashes Scissors."
          "\n\n Notes: *The first one that scores 5 points WINS the game!"
          "\n        *If you forgot the rules, just type 'help'."
          "\n        *If you want to go to main menu to try the other games, just type 'quit'."
          "\n        *If you want to exit because you're afraid of loosing, just type 'exit' you coward!\n")
    selections_list = SELECTIONS_LIST_RPSLS  #  selections are assigned based on the game
    win_list = WIN_LIST_RPSLS  #  win list is assigned based on the game
  
  elif option == '3':  #  if option 2 is selected, it will play Rock + Paper + Scissors + Lizard + Spock game
    intro = (" Welcome to Rock + Paper + Scissors: Corona Edition!")
    option_help = ("\n This game is simple and goes as following:"
          "\n *You can choose between: Corona, Mask, Stupid, No mask, Home, and Soap."
          "\n\n You must take in consideration that:"
          "\n *Corona defeats Stupid and No mask."
          "\n *Mask defeats Corona and Stupid."
          "\n *Stupid defeats No Mask."
          "\n Mask cannot be defeated."
          "\n\n Notes: *The first one that scores 5 points WINS the game!"
          "\n        *If you forgot the rules, just type 'help'."
          "\n        *If you want to go to main menu to try the other games, just type 'quit'."
          "\n        *If you want to exit because you're afraid of loosing, just type 'exit' you coward!\n")
    selections_list = SELECTIONS_LIST_RPSLS  #  selections are assigned based on the game
    win_list = WIN_LIST_RPSLS  #  win list is assigned based on the game
  
      
  print(intro)  #  displays the intro information based on the option selected
  print(option_help)  # displays the help information based on the option selected
    
  while True:
    player_selection = input("Your Selection {}: ".format(selections_list))
    player_selection = player_selection.upper()
    
    if player_selection in selections_list:
      clrscr()
      computer_selection = random.choice(selections_list)
      
      print("Player Selection: {}".format(player_selection))
      print("Computer Selection: {}".format(computer_selection))
      
      match = player_selection, computer_selection  #  converts the player's and computer's selection into a tuple to compare it to win list
      
      if player_selection == computer_selection:  #  if both selections (player and computer) are the same, a tie count is added to the dictionary
        stats_count['ties'] += 1
        print("\nResult: Both are {}! So that's a Tie!".format(player_selection))
      elif match in win_list:  #  if the tuple is the same as the win_list, player wins and a player count is added to the dictionary
        stats_count['player'] += 1
        print("\nResult: The power of {} beats {}! You won!".format(player_selection, computer_selection))
      else:  #  if none of the conditions above are true, computer wins and a computer count is added to the dictionary
        stats_count['computer'] += 1
        print("\nResult: The power of {} is stronger than {}! You lost!".format(computer_selection, player_selection))
      print("-------  STATS  -------"
            "\n YOU  | COMPUTER | DRAW"
            "\n  {player}        {computer}        {ties}"
            "\n-----------------------".format(**stats_count))
      if stats_count['player'] == 5:  #  if player gets 5 points, he wins
        print("The game is DONE! You won! Congratulations!")
        restart()
      elif stats_count['computer'] == 5:  #  if computer gets 5 points, he wins
        print("The game is DONE! You lost against a perfectly designed AI! You're now in the wall of shame!")
        restart()
    elif player_selection == 'HELP':  #  if the user doesn't remember the rules, it will show them again
      clrscr()
      print(option_help)
    elif player_selection == 'QUIT':  #  if the user wants to play another game, it will take him to main menu, stats are again
      stats_count['player'] = 0
      stats_count['computer'] = 0
      stats_count['ties'] = 0
      input("Let's try another game mode then. I hope you enjoyed! Please press ENTER to continue...")
      clrscr()
      break
    elif player_selection == 'EXIT':  #  if the user wants to exit the game
      print("Bye bye... YOU COWARD!")
      exit()
    else:
      print("Invalid selection. Try again...")  #  if there's an invalid choice, the input will show again

def restart():
        print("Choose 1: - Magic 8 | 2 -  MadLib | 3 - Rock, Paper, Scissors! | q - quit")

        choice = input()
        if choice == "1":
            Magic8Ball()
        elif choice == "2":
            madlibs_start()
        elif choice == "3":
            RPS()
        elif choice == "q":
            print("Byeeeeeee")
            exit()
        else:
            quit
    

def main_code():
    clrscr()
    print("Do you want to play a game? (yes/no)")
    print()
    answer = input()
    if answer.lower() == "yes" or answer.lower() == "y":
        print("Choose: 1 - Magic 8 | 2 -  MadLib | 3 - Rock, Paper, Scissors! | q - quit")

        choice = input()
        if choice == "1":
            print('  __  __          _____ _____ _____    ___  ')
            print(' |  \/  |   /\   / ____|_   _/ ____|  / _ \ ')
            print(' | \  / |  /  \ | |  __  | || |      | (_) |')
            print(' | |\/| | / /\ \| | |_ | | || |       > _ < ')
            print(' | |  | |/ ____ \ |__| |_| || |____  | (_) |')
            print(' |_|  |_/_/    \_\_____|_____\_____|  \___/ ')
            print('')
            print('')
            print('')
            print('I am the Magic 8 Ball, What is your name?')
            print()
            name = input()
            print('hello ' + name)

            Magic8Ball()
        elif choice == "2":
            madlibs_start()
        elif choice == "3":
            RPS()
        elif choice == "q":
            exit()
        else:
            print("Enter vaild number")
    elif answer.lower() == "no":
        print("Okay")
    else:
        print("Please enter yes or no.")

main_code()

 