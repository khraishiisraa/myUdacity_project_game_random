# لعبة المغامرة تم تسليمها بنجاح لكن يمكن اضافة تعديل بحيث يفحص هزيمة الوحوش
import time
import random


def tale(message):
    print(message)
    time.sleep(2)


treasures = []
weapons = []
weapon = " "
required_treasures = ["gold coins", "diamond", "magic carpet"]


def choice_weapon(weapons):
    return random.choice(weapons) if weapons else "nothing"


def check_win():
    if set(treasures) == set(required_treasures):
        tale("you have all required treasures\n")
        tale("congratulation, you win\n")
        tale("you could leave the island,")

        tale("return to your home\n")
        win_choice()


def win_choice():
    choice = input("do you want 1.play again\n or\n 2.exit (1/2)\n")
    if choice == "1":
        treasures.clear()
        weapons.clear()
        play_game()
    elif choice == "2":
        out_game()
    else:
        tale("Invalid choice, the game end")
        out_game()


def play_game():
    while True:
        inter()
        player()
        choice_place()


def inter():
    tale("welcome to new Adventure\n")
    tale("after you lost in the sea\n")
    tale("you found your self in an island\n")
    tale("you have to find three treasurs  to return home\n")
    tale("in front of you.")
    tale("There is a majestic temple made of fiery red stones\n")
    tale("Next to the temple there is a lake and\n")
    tale("in the other side there is")
    tale("green forest with long hanging branches like ropes\n")


def player():
    tale("""choose your player\n1. Ali\n2.Yasmeena\n """)
    choice = input("choose '1 or '2':\n")
    if choice == "1":
        name = "Ali"
    elif choice == "2":
        name = "Yasmeena"
    else:
        tale("Invalid choice")
        return player()
    tale(f"welcome to our adventure, {name}")
    tale(f"{name}, you need to obtain the three treasures\n")
    tale("But beware of the monsters gurding the treasurs\n")
    tale("you have to kill the gurdianes to win the hidden prices\n")


def choice_place():
    tale("where do you want to go?")
    print("""1. to go the Temple
     2. to go to the Lake
     3. to go to the Forest""")
    choice = input("choose: '1' or '2.' or '3.'\n")
    if choice == "1":
        temple()
    elif choice == "2":
        lake()
    elif choice == "3":
        forest()
    else:
        print("Invalid choice")
        choice_place()


def scorpion():
    tale("you  are facing  a giant scorpion \n")
    tale("its weak point is 'magical fire'")
    weapon = choice_weapon(weapons)
    print(f"you have: {weapon}")
    if weapon == "magical fire":
        tale("you defeated the scorpion\n" "you win a magical spear!\n")
        weapons.append("magical spear")
        tale("the spear's tip contains scorpion venom\n")
        tale("do you want to go to the' right' or 'out' the Temple")
        right_choice()
    else:
        print("GAME OVER!")
        start_exit()


def right_choice():
    choice = input("(right/out)").strip().lower()
    if choice == "right":
        if "gold coins" not in treasures:
            tale("congratulation, you have received achest of gold coins\n")
            treasures.append("gold coins")
        check_win()
        start_exit()
    elif choice == "out":
        start_exit()
    else:
        tale("Invalid choice.")
        right_choice()


def snake():
    tale("you facing with a giant snake ,\n")
    tale("its weak point is 'magical mirror\n")
    weapon = choice_weapon(weapons)
    print(f"you have: {weapon}")
    if weapon == "magical mirror":
        tale("you defeat the snake,\n""the snake become stone statue\n")
        tale("a magical word appeard: 'HOME',\n")
        tale("you can use it to open the wood chest in the tiger den\n")
        print("1.go to the top of the tower\n")
        print("2.go to the begining and choose place again\n")
        choice = input("choose '1' or '2':\n")
        if choice == "1":
            take_fire()
        else:
            start_exit()
    else:
        tale("GAME OVER")
        start_exit()


def temple():
    tale("Inside the Temple there is a chest of gold coins.\n")
    tale("Beware: the huge scorpion inside, its weakness is 'magical fire'\n")
    tale("in front of you there are two entrances")
    tale("on the right and left,\n")
    tale("and between them there is a magical mirror.\n")
    take_mirror()


def take_mirror():
    if "magical mirror" in weapons:
        print("You already have the magical mirror.")
        left_right()
    choice = input("Do you want to take the mirror? 'yes', or 'no'\n")
    if choice == "yes":
        weapons.append("magical mirror")
        print("you got a magical weapon, use it to kill the gurdians.")
        left_right()
    elif choice == "no":
        left_right()
    else:
        print("Invalid choice")
        take_mirror()


def left_right():
    choice = input("do you want to go 'left' or 'right'\n").lower()
    if choice == "left":
        scorpion()
    elif choice == "right":
        if "gold coins" not in treasures:
            tale("Congratulation, you have received a chest of gold coins")
            treasures.append("gold coins")
        check_win()
        second_choice()
    else:
        tale("Invalid choice")
        left_right()


def second_choice():
    tale("do you want go 'left' or 'out' the temple\n")
    next_choice = input("choose(left/out):\n").lower()
    if next_choice == "left":
        scorpion()
    elif next_choice == "out":
        start_exit()
    else:
        temple()


def lake():
    tale("in front of you, a boat at the edge of the lake and \n")
    tale("a paved stones extending from the shore to the middle of the lake\n")
    tale("in the middle of the lake  you will see a tall Tower\n")
    tale("magic carpet at the top of the tower\n")
    tale("Beware:of disturbing the snake in the lake.\n")
    tale("1.do you want git in the boat\n")
    tale("2.or to walk on the paved stons\n")
    choice = input("choose '1.' or '2.'\n")
    if choice == "1":
        tale("you git in the boat, the boat become closer to the tower\n")
        tale("you git off the boat,the boat started to sink in the lake\n")
        tale("because of the hole, you won't be able to use it again\n")
        tale("Next to the entrance of the tower,")
        tale("you will see a torch of magical fire\n")
        take_fire()
    elif choice == "2":
        snake()
    else:
        tale("Invalid choice")
        lake()


def take_fire():
    if "magical fire" in weapons:
        print("you already have the magical fire")
        top_tower()
    print("do you want to take the magical fire?\n")
    choice = input("choose 'yes' or 'no'\n")
    if choice == "yes":
        weapons.append("magical fire")
        tale("you got a magical weapon, use it to kill the gurdians")
    top_tower()


def top_tower():
    tale("you go up the stairs towards the top of the tower\n")
    if "magic carpet" not in treasures:
        tale("congratulation, you have received the magical carpet\n")
        treasures.append("magic carpet")
    check_win()
    out_tower()


def out_tower():
    tale("you can leave the tower by:\n")
    tale("1. the carpit or \n""2.go back through the paved stons\n")
    choice = input("choose '1' or '2'\n")
    if choice == '1':
        tale("you are fly on the carpet back to the beginig\n")
        start_exit()
    elif choice == "2":
        snake()
    else:
        out_tower()


def forest():
    tale("in front of you a green forest with long brunches like a rops\n")
    tale("walk through the trees until reach the Tiger's den\n")
    tale("you have to kill the tiger to enter his den\n")
    tale("the tiger weak point is 'magical spear'\n")
    weapon = choice_weapon(weapons)
    print(f"you have: {weapon}")
    if weapon == "magical spear":
        tale("you defeat the tiger, you can enter to the den\n")
        tale("you are inside the den there is a magic wood chest\n")
        tale("you need to say a magic word\n")
        choice = input("say the magic word\n").upper()
        if choice == "HOME":
            if "diamond" not in treasures:
                tale("the wood chest is open, inside a large diamond\n")
                tale("congratulatio, you win a treasure\n")
                treasures.append("diamond")
            check_win()
            start_exit()
        else:
            tale("Wrong word. you need to defeat the snake first\n")
            start_exit()
    else:
        tale("you could not kill the tiger\n")
        tale("GAME OVER")
        start_exit()


def start_exit():
    tale("do you want to start again or exit\n")
    choice = input("choose 'start' or 'exit'\n").lower()
    if choice == "start":
        choice_place()
    elif choice == "exit":
        out_game()
    else:
        start_exit()


def out_game():
    tale("thank you for playing\n ,goodbye!")
    exit()

play_game()