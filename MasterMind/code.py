def ask_code():
    code = input("Veuillez saisir un code à 4 chiffres : ")
    # Verification de la longueur du code
    if len(code) != 4:
        print("Le code doit être composé de 4 chiffres")
        return ask_code()
    else:
        return code
    

def check_code(answer_code, good_code):
    # Décomposition du code 
    code = list(answer_code)
    code_to_find = list(good_code)
    result = []
    # Verification si les chiffres sont dans le code
    for i in range(4):
        if code[i] == code_to_find[i]:
            result.append("GREEN")
        if code[i] in code_to_find and code[i] != code_to_find[i]:
            if code.count(code[i]) > code_to_find.count(code[i]):
                result.append("RED")
            else:
                result.append("YELLOW")
            
        if code[i] not in code_to_find: 
            result.append("RED")
        
    return result