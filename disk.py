class Disk:
    def __init__(self, total, used):
        self.total = total
        self.used = used
    
    @property
    def free(self):
        return self.total - self.used

    @property
    def used_perc(self):
        return self.used / self.total
    
    def __str__(self):
        return f"Disk[total: {self.total} Gb, used: {self.used} Gb]"
    
    def __lt__(self, other):
        # Permet de trier les disques par pourcentage d'espace utilisé
        return self.used_perc < other.used_perc

if __name__ == '__main__':
    # Exemple de création de disques et de tests
    disk1 = Disk(total=10, used=2)
    disk2 = Disk(total=20, used=5)
    
    print(disk1.free)        # Affiche 8
    print(disk2.free)        # Affiche 15
    print(disk1.used_perc)   # Affiche 0.2
    print(disk2.used_perc)   # Affiche 0.25

    # Afficher les disques
    print(disk1)             
    print(disk2)             

    # Tri de la liste de disques
    disks = [disk1, disk2]
    disks_sorted = sorted(disks)  # Trié par ordre croissant du pourcentage d'espace utilisé
    
    # Afficher les disques triés
    for disk in disks_sorted:
        print(disk)
