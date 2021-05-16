class WrongAnswer(Exception):
    def __init__(self, msg):
        super().__init__(msg)

print("Welcome to Jumanji")
cdesign = input("What persona do you want, the embodiment of strength or stealth? ")

character = "fish"
if cdesign.lower() == "strength":
    print("A wise choice strong fellow.") 
    character = "strength"
elif cdesign.lower() == "stealth":
    print("Sneaky and wise good sir.")
    character = "stealth"
else:
    raise WrongAnswer("stealth/strength")

class JumanjiChar:
    def __init__(self, name, ability):
        self.name = name.title()
        self.ability = ability

nombre = input("What will be your name brave sir? ")
character1 = JumanjiChar(nombre, character)
health = 100
print(f"{character1.name} you are in the lush Amazon Rainforest.")
print(f"Be aware your health is currently at {health} but that could change soon.")
firstoption = input("Do you cross the murky river or forge a path through the jungle? river/jungle ")
if firstoption.lower() == "river" and character == "strength":
    print("A crocodile comes your way but luckily you use your strength to hits its snout.")
    print("The crocodile dies from shock and you safely make it across.")
elif firstoption.lower() == "jungle" and character == "strength":
    print("You enter the jungle and a jaguar attacks you from above!")
    print("Lucily you use your strength to fling it across the forest.")
    print("Sadly, it caused some damage and hurt your health.")
    health -= 20
elif firstoption.lower() == "river" and character == "stealth":
    print("A crocodile comes after you. You begin fighting and luckily scare it off.")
    print("Sadly it bit your leg and you lost some health.")
    health -= 20
elif firstoption.lower() == "jungle" and character == "stealth":
    print("You see a jaguar above but you sneak past it and make it out of the thick jungle.")
else:
    raise WrongAnswer("river/jungle")

print(f"{character1.name} you reach a clearing in the jungle and spot an outpost.")
secondoption = input("Do you attack or move in for a better advantage? attack/move ")
if secondoption.lower() == "attack" and character == "strength":
    print("You storm in and 10 enemies come at you with machetes!")
    print("You use your strength to hoist one up and swing him around like a hammer.")
    print("Everyone becomes unconcious and you loot a body and find a map ...")
elif secondoption.lower() == "move" and character == "strength":
    print("You try to move in for a better advantage but you are very large and guards notice you!")
    print("An archer hits you in your foot but you leap in and incapacitate everyone!")
    print("Sadly, it caused some damage and hurt your health. But you find a map on the ground ...")
    health -= 40
elif secondoption.lower() == "move" and character == "stealth":
    print("You sneak in across enemy lines and see many guards. You slowly take them out one by one.")
    print("The last guard spots you but its too late, you knock him to the ground and loot his body.")
    print("You find a map of Jumanji ...")
elif secondoption.lower() == "attack" and character == "stealth":
    print("You attack fast but they see you coming. A fight ensues and you knock out 5 enemies.")
    print("Your hand to hand is amazing and you win but you see a dagger has hurt you.")
    print("On the upside you find a map ...")
    health -= 40
else:
    raise WrongAnswer("attack/move")

print(f"{character1.name} the map you found leads you back to reality!")
print("You must reach the temple of Doom and from there you can escape!")
print("Only you must choose which path to take, through the caves east or the western trail!")
thirdoption = input("caves/trail")
if thirdoption.lower() == "caves" and character == "strength":
    print("You lumber into the caves but you cannot see anything!")
    print("A swarm of bats attacks you and bites you!")
    print("Your take damage but you exit and you can see the temple in the distance.")
    health -= 20
elif thirdoption.lower() == "trail" and character == "strength":
    print("You take the trail and two jaguars jump in front of you!")
    print("Only this time you are prepared and pound them both while they leap!")
    print("You move on unscathed and spot the temple ...")
elif thirdoption.lower() == "caves" and character == "stealth":
    print("Like a thief in the night, you sneak through the caves and even bypass some enemies.")
    print("You finally exit the cave and spot your ticket out.")
elif thirdoption.lower() == "trail" and character == "stealth":
    print("You take the trail but suddenly two monkeys throw spears at you.")
    print("One of them hits your abdomen but you manage to escape.")
    print("You are hurt but finally you see the temple in the distance.")
    health -= 20
else:
    raise WrongAnswer("caves/trail")
