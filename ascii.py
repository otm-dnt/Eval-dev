# Fonction de décryptage
def decrypt(message: [int]) -> str:
    # Convertir chaque code ASCII en caractère et les joindre pour créer une chaîne
    return ''.join(chr(num) for num in message)

# Bloc de test
if __name__ == '__main__':
    # Liste de codes ASCII fournie
    ascii_codes = [84, 104, 105, 115, 32, 101, 120, 101, 114, 99, 105, 99, 
                  101, 32, 105, 115, 32, 97, 119, 101, 115, 111, 109, 101, 32, 33]

    # Appeler la fonction decrypt et afficher le résultat
    print(decrypt(ascii_codes))  
