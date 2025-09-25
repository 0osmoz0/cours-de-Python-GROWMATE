
import random

response_ninon = [

    "j'aime les pomme",
    "non dingue",
    "je deteste coder",
    "le 92 c'est de la merde",
]

print("tu peut parler a ninon mais attention elle est sont champi : (tape 'exit' pour quitter)")
while True:
    msg = input("Toi > ")
    if msg.lower() == 'exit':
        print("ninon vas dodo")
        break
    print("ninon > ", random.choice(response_ninon))