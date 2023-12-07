import rando m

def lancer_de():
    return random.randint(1, 6)

def main():
    nombre_de_lancers = 5
    somme_points = 0

    for _ in range(nombre_de_lancers):
        resultat_lancer = lancer_de()
        print(f'Résultat du lancer : {resultat_lancer}')
        somme_points += resultat_lancer

    print(f'\nNombre total de points : {somme_points}')

if __name__ == "__main__":
    main()