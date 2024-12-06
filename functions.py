# Fonction several_zeros
def several_zeros():
    # Retourne une liste de 10 zéros
    return [0] * 10

# Fonction several_zeros_custom
def several_zeros_custom(nb_zeros=10):
    # Retourne une liste de nb_zeros zéros
    return [0] * nb_zeros

# Fonction matrix
def matrix(rows, cols):
    # Retourne une matrice de taille rows x cols remplie de zéros
    return [[0 for _ in range(cols)] for _ in range(rows)]

# Classe Matrix
class Matrix:
    def __init__(self, rows, cols):
        # Initialise une matrice de taille rows x cols remplie de zéros
        self.__matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    def get_value(self, row, col):
        # Retourne la valeur à la position (row, col) de la matrice
        return self.__matrix[row][col]

    def __eq__(self, other):
        # Compare deux matrices pour vérifier leur égalité
        return self.__matrix == other.__matrix

    def __str__(self):
        # Retourne une représentation en chaîne de la matrice pour un affichage clair
        return '\n'.join([' '.join(map(str, row)) for row in self.__matrix])

# Bloc pour tester les fonctions et la classe
if __name__ == '__main__':
    # Tests pour la fonction several_zeros
    print(several_zeros())  # Affiche une liste de 10 zéros

    # Tests pour la fonction several_zeros_custom
    print(several_zeros_custom(5))  # Affiche une liste de 5 zéros
    print(several_zeros_custom())   # Affiche une liste de 10 zéros (valeur par défaut)

    # Tests pour la fonction matrix
    result = matrix(2, 3)
    print(result)                   # Affiche une matrice de 2 lignes et 3 colonnes remplies de zéros
    print(result[1][2])             # Affiche 0 (2ème ligne, 3ème colonne)
    print(result[0])                # Affiche la première ligne [0, 0, 0]

    try:
        print(result[2][3])         # Devrait provoquer une erreur (indice hors limites)
    except IndexError as e:
        print("Erreur : ", e)

    # Tests pour la classe Matrix
    m1 = Matrix(2, 3)
    m2 = Matrix(2, 3)
    print(m1 == m2)  # Devrait afficher True (matrices identiques)

    # Afficher la matrice m1 en utilisant la méthode __str__
    print(m1)  # Affiche la matrice de m1 de manière lisible

    # Tester la méthode get_value
    print(m1.get_value(1, 2))  
