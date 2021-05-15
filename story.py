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
print("Almost there")
print(health)