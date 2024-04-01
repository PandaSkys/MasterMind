import MasterMind as mm
from colorama import init, Fore

# Init colorama pour Windows
init()
color_matching = {
    "RED": Fore.RED,
    "GREEN": Fore.GREEN,
    "YELLOW": Fore.YELLOW
}


def main():
    print("Bienvenue dans le jeu du MasterMind !")
    rules = input("Voulez-vous les règles ? [Oui] : ").lower().strip()
    if rules == "oui":
        mm.show_rules()
    elif rules == "":
        mm.show_rules()
    # Génération du code à trouver
    good_code = mm.generate_random_numbers()
    # Affichage du vrai code
    print(good_code)
    for i in range(10):
        mm.bar()
        # Affichage du nombre d'essais restants
        print(f"Il vous reste {10 - i} essais")
        # Demande de saisie du code
        answer_code = mm.ask_code()
        # Vérification du code
        if answer_code == good_code:
            print("Bravo, vous avez trouvé le code")
            mm.end_games()
            break
        else:
            result = mm.check_code(answer_code, good_code)
            print("                                       " + color_matching.get(result[0]) + "●" + Fore.RESET + color_matching.get(result[1]) + "●" + Fore.RESET + color_matching.get(result[2]) + "●" + Fore.RESET + color_matching.get(result[3]) + "●" + Fore.RESET)

        # Si le joueur n'a plus d'essais
        if i == 9:
            mm.bar()
            print("Vous n'avez plus d'essais")
            print(f"Le code était {good_code}")
            mm.end_games()
            break


while True:
    main()
