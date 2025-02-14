# Description: This program generates a random password based on user input.
from random import randint

animals_3word = ["cat", "dog", "fox", "bat", "rat", "elk"]
animals_4word = ["wolf", "bear", "lion", "shark", "whale", "hare", "mole", "vole", "frog", "toad"]
animals_5word = ["tiger", "horse", "sheep", "mouse", "crab", "shrimp", "clam", "squid", "coral", "eagle"]
animals_6word = ["deer", "moose", "goat", "cow", "pig", "newt", "shark", "whale", "otter", "beaver"]
animals_7word = ["lobster", "oyster", "octopus", "starfish", "urchin", "anemone", "falcon", "sparrow", "robin", "finch"]
animals_8word = ["platypus", "echidna", "kangaroo", "koala", "wombat", "possum", "lemur", "monkey", "gorilla", "chimpanzee"]
animals_9word = ["orangutan", "baboon", "gibbon", "anteater", "armadillo", "pangolin", "aardvark", "hyena", "jackal", "coyote"]
animals_10word = ["chimpanzee", "orangutan", "chimpanzee", "orangutan", "chimpanzee", "orangutan", "chimpanzee", "orangutan", "chimpanzee", "orangutan"]

adjectives = ["happy", "angry", "crazy", "brave", "quiet", "loud", "rough", "smart", "dumb", "clever",
"foolish", "strong", "quick", "small", "short", "chubby", "plain", "fancy", "young", "clean",
"dirty", "neat", "tidy", "moody", "gloomy"]

symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "_", "+", "-", "=", ":", ";", "'", "<", ">", ",", ".", "?", "~" ]

def generate_password():
    animal3 = animals_3word[randint(0, len(animals_3word) - 1)]
    animal4 = animals_4word[randint(0, len(animals_4word) - 1)]
    animal5 = animals_5word[randint(0, len(animals_5word) - 1)]

    adjective = adjectives[randint(0, len(adjectives) - 1)]
    symbol = symbols[randint(0, len(symbols) - 1)]
    number = randint(0, 99)

    print(f"Your password is: {password}")

print("""Welcome to the Password Generator! Would you like to generate a single password or many?"
Controls:
Generate password: 'Enter'
Back: 'b'
Exit: Any other key
""")

while True:
    decision1 = input("How long would you like your passwords to be?")
    try:
        decision1 = int(decision1)
    except ValueError:
        print("Please enter a valid number")
    break
    if decision1 < 12:
        print("")

    decision2 = input("Type 's' or 'm': ")
    
    if decision2 == "s":
        while True:
            inpt = input("Press Enter to generate a password: ")
            if inpt == "":
                generate_password()
            elif inpt == "b":
                break
            else:
                print("Invalid input. Exiting the program.")
                exit()

    elif decision2 == "m":
        while True:
            inpt = input("How many passwords would you like to generate?")
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

            inpt = input("What would you like to do next? ")
            if inpt == "":
                continue
            elif inpt == "b":
                break
            else:
                exit()