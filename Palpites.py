import random

lista_palpite = []
contador = 0

while contador < 6:
    palpite = random.randint(1, 60)
    if palpite not in lista_palpite:
        contador += 1
        lista_palpite.append(palpite)
    else:
        pass

lista_palpite.sort()

print('{},{},{},{},{},{}'.format(lista_palpite[0], lista_palpite[1],
                                 lista_palpite[2], lista_palpite[3],
                                 lista_palpite[4], lista_palpite[5]))
