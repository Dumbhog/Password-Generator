# Description: This program generates a random password based on user input.
from random import randint

animals = ["cat", "dog", "fox", "wolf", "bear", "lion", "tiger", "shark", "whale", "horse"
"deer", "moose", "goat", "sheep", "cow", "pig", "bat", "rat", "mouse", "hare",
"elk", "lynx", "mole", "vole", "frog", "toad", "newt", "salamander", "crab", "lobster",
"shrimp", "clam", "oyster", "squid", "octopus", "jellyfish", "starfish", "urchin", "coral", "anemone",
"eagle", "hawk", "falcon", "owl", "sparrow", "robin", "finch", "wren", "lark", "dove",
"pigeon", "crow", "raven", "magpie", "jay", "swallow", "swift", "gull", "tern", "albatross",
"penguin", "seal", "walrus", "otter", "beaver", "platypus", "echidna", "kangaroo", "koala", "wombat",
"possum", "lemur", "monkey", "ape", "gorilla", "chimpanzee", "orangutan", "baboon", "gibbon", "sloth",
"anteater", "armadillo", "pangolin", "aardvark", "hyena", "jackal", "coyote", "dingo", "ferret", "weasel",
"mink", "stoat", "ermine", "badger", "skunk", "raccoon", "opossum", "porcupine", "hedgehog", "shrew" ]

adjectives = ["happy", "sad", "angry", "mad", "glad", "silly", "funny", "serious", "crazy", "wild", 
"calm", "brave", "shy", "bold", "lazy", "active", "quiet", "loud", "gentle", "rough",
"kind", "mean", "friendly", "unfriendly", "polite", "rude", "smart", "dumb", "clever", "foolish",
"strong", "weak", "fast", "slow", "big", "small", "tiny", "huge", "short", "tall",
"thin", "fat", "chubby", "skinny", "beautiful", "ugly", "handsome", "pretty", "plain", "fancy",
"rich", "poor", "young", "old", "new", "ancient", "modern", "classic", "trendy", "outdated",
"clean", "dirty", "neat", "messy", "tidy", "sloppy", "organized", "disorganized", "happy-go-lucky", "moody",
"cheerful", "gloomy", "optimistic", "pessimistic", "hopeful", "hopeless", "confident", "insecure", "fearless", "fearful",
"adventurous", "cautious", "curious", "indifferent", "energetic", "lethargic", "enthusiastic", "apathetic", "creative", "unimaginative" ]

symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "_", "+", "-", "=", ":", ";", "'", "<", ">", ",", ".", "?", "~" ]

def generate_password():
    animal = animals[randint(0, len(animals) - 1)]
    adjective = adjectives[randint(0, len(adjectives) - 1)]
    symbol = symbols[randint(0, len(symbols) - 1)]
    number = randint(0, 99)
    password = f"{adjective.title()}{symbol.title()}{animal.title()}{number}"
    print(f"Your password is: {password}")

print("""Welcome to the Password Generator! Would you like to generate a single password or many?"
Controls:
Generate password: 'Enter'
Back: 'b'
Exit: Any other key
""")

while True:
    decision = input("Type 's' or 'm': ")
    
    if decision == "s":
        while True:
            inpt = input("Press Enter to generate a password: ")
            if inpt == "":
                generate_password()
            elif inpt == "b":
                break
            else:
                print("Invalid input. Exiting the program.")
                exit()

    elif decision == "m":
        while True:
            inpt = input("How many passwords would you like to generate? ")
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