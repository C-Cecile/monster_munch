#Imports necessary modules
import emoji
import sys
import time

#Creates a slow-typing function for text outputs.
def slow_print(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.04)

#Creates dictionaries and relevant variables for future use.
player = {"name": "", "attack": 15, "super_attack":25, "heal": 20, "health": 100}
monster = {"name": "Monster Munch", "attack": 15, "health": 100}
game_running = player["health"] != 0

#Asks for player name
slow_print("Please enter your name:")
print("")
player["name"] = input()

#Prints intro to the game and asks the player to make a first move.
slow_print("\nAlright " + player["name"] + ", let's fight that monster!")

while game_running == True:
    #Options when player attacks and Monster health <= 0hp.
    if monster["health"] <= 0:
        print(emoji.emojize("You've defeated Monster Munch, oorah!! :punch:", use_aliases=True))
        print("Thanks for playing!")
        game_running == False
        break
    elif player["health"] <= 0:
        print(emoji.emojize("\nNoOoOOooOOoO. You're dead. :broken_heart:\nThanks for playing!!", use_aliases=True))
        game_running == False
        break
    #Options when player attacks and Monster health > 25hp.
    elif monster["health"] > 25:
        slow_print("\nWhat do you want to do?")
        print("\n1 - Attack")
        print("2 - Heal")
        print("")
        player_choice = input()

        #Prints what happens when player attacks and Monster health > 25hp.
        if player_choice == "1":
            print("\nIncoming!")
            monster["health"] = monster["health"] - player["attack"]
            slow_print(emoji.emojize("\nAwesome, Monster Munch took a hit and lost " + str(player["attack"]) + "hp!\nWe like that, Monster Munch now has " + str(monster["health"]) + "hp left. :sunglasses:\nBut wait! Monster Munch is fighting back!!", use_aliases=True ))
            player["health"] = player["health"] - monster["attack"]
            slow_print(emoji.emojize("\nDannnnnnng, he just cost you " + str(monster["attack"]) + " points and now you have " + str(player["health"]) + "hp.\nWe like that a little bit less. :scream:", use_aliases=True))
            print("")

        #Options when player heals and Player Health > 90hp
        elif player_choice == "2" and player["health"] >= 90:
            slow_print("\nAre you sure you want to do that? You've got " + str(player["health"]) + "hp already.")
            print("\n1 - I know what I'm about, son.")
            print("2 - Ehhhhh nevermind I'll spend my move on some sick attack skills instead.")
            print("")
            player_heal_choice = input()
            if player_heal_choice == "1":
                new_health= player["health"] + player["heal"]
                slow_print(emoji.emojize("\nMkay, well you went from " + str(player["health"]) + "hp to " + str(new_health) + "hp. Congrats!! :clap:", use_aliases=True))
                slow_print("\nAnnnnnd there we have it, Monster Munch is attacking you.")
                player["health"] = new_health - monster["attack"]
                print("\nYou now have " + str(player["health"]) + "hp.")
            else:
                print("\nOkeydok!")
                break

        #Prints what happens when health is below 90 and player heals.
        elif player_choice == "2" and player["health"] < 90:
            print(emoji.emojize("\nLet's heal these wounds! :ambulance:", use_aliases=True))
            player["health"] = player["health"] + player["attack"]
            slow_print(emoji.emojize("\nAll right you just gained back " + str(player["heal"]) + "hp and now have a total of " + str(player["health"]) + "hp :heart:", use_aliases=True))
            slow_print("\nSooooooo turns out Monster Munch enjoys kicking a man down...")
            print("")
            player["health"] = player["health"] - monster["attack"]
            print("\nYou now have " + str(player["health"]) + "hp left.")

    #Enables the Super Attack when Monster Munch health <= 25hp.
    elif monster["health"] <= 25:
        slow_print("\nWould you look at that, Monster Munch is extremely weak, do you want to finish him?")
        print("\n1 - Yeah, I've waisted enough time already, let's end this")
        print("2 - This is actually enjoyable and the idea of slowly killing an imaginary monster is quite pleasant.")
        print("")
        player_attack = input()
        if player_attack == "1":
            monster["health"] = monster["health"] - player["super_attack"]
            slow_print("\nYou're such fun to be around!!")
            slow_print("\nHere lies the corpes of Monster Munch who,\nWhile he drew breath,\nIn the midst of his life \nWas in quest of is death.")
            print("\nThanks for playing!")
            game_running == False
            break
        else:
            slow_print("Cool. Cool, cool, cool! So...")
            print("\nWhat do you want to do now?")
            print("\n1 - Attack, duh")
            print("2 - Heal")
            print("")
            player_choice = input()
            if player_choice == "1" and monster["health"] - player["attack"] <= 0:
                monster["health"] = 0
                slow_print("\nAnnnnnnnnd you just killed Monster Munch. Hope you did't get too attached to its loving personnality.")
                print("\nThanks for playing!")
                game_running == False
                break
            elif player_choice == "1" and monster["health"] - player["attack"] > 0:
                slow_print("\nTHIS IS SPARTA!")
                monster["health"] = monster["health"] - player["attack"]
                slow_print(emoji.emojize("\nTurns out you are also capable of hitting a man down and took " + str(player["attack"]) + "hp! We like that, Monster Munch now has " + str(monster["health"]) + "hp left. :sunglasses:", use_aliases=True ))
                print("")
                slow_print(emoji.emojize("\n... Do you hear that...? Nothing, Monster Munch isn't attacking anymore :eyes:", use_aliases=True))
            else:
                print(emoji.emojize("\nLet's heal these wounds! :ambulance:", use_aliases=True))
                player["health"] = player["health"] + player["attack"]
                slow_print(emoji.emojize("All right you just gained back " + str(player["heal"]) + "hp and now have a total of " + str(player["health"]) + "hp :heart: \nSooooooo turns out Monster Munch enjoys kicking a man down...", use_aliases=True))
                slow_print(emoji.emojize("\n... Do you hear that...? Nothing, Monster Munch isn't attacking anymore :eyes:", use_aliases=True))

    #Prints what happens when player neither chooses Attack or Heal.
    else:
        print("Invalid input")
