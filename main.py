import MasterMind as mm


color_matching = {
    "RED": mm.colors.RED,
    "GREEN": mm.colors.GREEN,
    "YELLOW": mm.colors.YELLOW
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
    # print(good_code)
    for i in range(10):
        mm.bar()
        # Affichage du nombre d'essais restants
        print(f"Il vous reste {10 - i} essais")
        # Demande de saisie du code
        answer_code = mm.ask_code()
        # Vérification du code
        if answer_code == good_code:
            print("Bravo, vous avez trouvé le code")
            mm.end_game()
            break
        else:
            result = mm.check_code(answer_code, good_code)
            print("                                       " + color_matching.get(result[0]) + "●" + mm.colors.END + color_matching.get(result[1]) + "●" + mm.colors.END + color_matching.get(result[2]) + "●" + mm.colors.END + color_matching.get(result[3]) + "●" + mm.colors.END)

        # Si le joueur n'a plus d'essais
        if i == 9:
            mm.bar()
            print("Vous n'avez plus d'essais")
            print(f"Le code était {good_code}")
            mm.end_game()
            break


while True:
    main()
