# Description: This program generates a random password based on user input.
from random import randint

animals_3letter = ["fox", "bat", "rat", "elk", "cow", "pig", "hen", "emu"]
animals_4letter = ["wolf", "bear", "lion", "hare", "mole","frog", "toad"]
animals_5letter = ["tiger", "horse", "sheep", "crane", "coral", "eagle, otter"]
animals_6letter = ["beaver", "donkey", "monkey", "gibbon", "baboon", "lemur", "oyster", "falcon",]
animals_7letter = ["lobster", "oyster", "octopus", "urchin", "sparrow", "penguin"]
animals_8letter = ["platypus", "kangaroo", "elephant", "antelope", "chipmunk", "dormouse"]
animals_9letter = ["orangutan", "pangolin", "aardvark", "armadillo", "porcupine"]
animals_10letter = ["bloodhound", "wildebeest", "woodpecker", "chimpanzee", "chinchilla"]

adjectives = ["happy", "angry", "crazy", "brave", "quiet", "rough", "smart", "quick", "small", "short", "chubby", "plain", "fancy", "young", "clean",
"dirty", "moody", "gloomy", "agape", "alone", "alien", "alive", "alert", "amuck", "awake", "aware", "awful", "axial", "basic", "batty", "beady", "beamy",]

symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "_", "+", "-", "=", ":", ";", "'", "<", ">", ".", "?", "~" ]

animal_dict = {
    10: "",
    11: "",
    12: "",
    13: "",
    14: "",
    15: "",
    16: "",
    17: ""
}

animal3 = 0
animal4 = 0
animal5 = 0
animal6 = 0
animal7 = 0
animal8 = 0
animal9 = 0
animal10 = 0

def generate_password():

    global adjective
    global symbol
    global number 
    global animal1
    global animal2
    global animal3
    global animal4
    global animal5
    global animal6
    global animal7
    global animal8
    global animal9
    global animal10
    global animal_dict
    
    animal4 = animals_4letter[randint(0, len(animals_4letter) - 1)]
    animal5 = animals_5letter[randint(0, len(animals_5letter) - 1)]
    animal6 = animals_6letter[randint(0, len(animals_6letter) - 1)]
    animal7 = animals_7letter[randint(0, len(animals_7letter) - 1)]
    animal8 = animals_8letter[randint(0, len(animals_8letter) - 1)]
    animal9 = animals_9letter[randint(0, len(animals_9letter) - 1)]
    animal10 = animals_10letter[randint(0, len(animals_10letter) - 1)] 

    adjective = adjectives[randint(0, len(adjectives) - 1)]
    symbol = symbols[randint(0, len(symbols) - 1)]
    number = randint(10, 99)

    animal_dict = {
    10: animal3,
    11: animal4,
    12: animal5,
    13: animal6,
    14: animal7,
    15: animal8,
    16: animal9,
    17: animal10
    }

    password = f"{adjective}{symbol}{animal_dict[decision1]}{number}"
    print(f"Your password is: {password}")

    password = 0
    adjective = 0
    symbol = 0
    number = 0
 
print("""Welcome to the Password Generator! You can generate a single password or many!"
Controls:
Generate password: 'Enter'
Back: 'b'
Exit: 'e' (or often any other key)
""")


while True:
    
    while True:

        decision1 = input("How long should your passwords be? (10-17): ")
        try:
            decision1 = int(decision1)
        except ValueError:
            if decision1 == "b":
                break
            elif decision1 == "e":
                exit()
            else:
                print("Please enter a valid number")
                break

        if decision1 not in animal_dict:
            print("Please enter a number between 10 and 17.")
            break

        decision2 = input("Type 's' or 'm': ")
        
        if decision2 == "s": 
            generate_password()
            break

        elif decision2 == "m":
            inpt = input("How many passwords would you like to generate?: ")
            try:
                inpt = int(inpt)
            except ValueError:
                print("Please enter a valid number.")
                break
            if 1 < inpt < 1000:
                    for i in range(inpt):
                        generate_password()
            elif inpt > 1000:
                print("Please enter a number between 1 and 1000.")
                break    

            inpt = input("Type 's' or 'm': ")
            if inpt == "":
                continue
            elif inpt == "b":
                break
            elif inpt == "s" or "m":
                decision2 = inpt
            else:
                exit()
        else: 
            exit()