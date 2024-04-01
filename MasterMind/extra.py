import random
import os


def bar():
    print("------------------------------------------------")


def generate_random_numbers():
    # Génération d'un code de 5 chiffres compris entre 1 et 9
    code = ""
    for i in range(4):
        code += str(random.randint(1, 9))
    return code


def show_rules():
    print("Bienvenue dans le jeu du Mastermind !\nDans ce jeux vous devez trouver un code à 4 chiffres généré aléatoirement en 10 essaie.\n- La pastille verte signifie que le chiffre est bon et bien placé\n- La pastille jaune signifie que le chiffre est bon mais mal placé\n- La pastille rouge signifie que le chiffre n'est pas le code secret.\nBonne chance !")


def end_games():
    print("Merci d'avoir joué à notre MasterMind")
    # Attendre 5 secondes
    os.system("pause")
    # Vider le terminal
    os.system('cls' if os.name == 'nt' else 'clear')
