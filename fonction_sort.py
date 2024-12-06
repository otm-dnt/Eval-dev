# Fonction de tri à bulles
def my_sort(my_list: [int]) -> [int]:
    # Copie de la liste pour ne pas modifier l'original
    sorted_list = my_list[:]
    n = len(sorted_list)
    
    # Algorithme de tri à bulles
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_list[j] > sorted_list[j + 1]:
                # Échanger les éléments si nécessaire
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
    
    return sorted_list

# Bloc de test pour vérifier la fonction
if __name__ == '__main__':
    # Exemple de test pour la fonction my_sort
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    print(my_sort(unsorted_list))  # Devrait afficher [11, 12, 22, 25, 34, 64, 90]
