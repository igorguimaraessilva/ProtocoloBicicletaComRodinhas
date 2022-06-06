def sorteiaDezena():
    import random

    unidades = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    dezenas = ["0", "1", "2", "3", "4", "5"]
    random.shuffle(unidades)
    random.shuffle(dezenas)
    return random.choice(dezenas)+random.choice(unidades)


def megaSena():
    dezenaSorteada = []
    while len(dezenaSorteada) < 6:
        dezenaSorteada.append(sorteiaDezena())
        if dezenaSorteada.count(dezenaSorteada[len(dezenaSorteada)-1]) > 1:
            del dezenaSorteada[len(dezenaSorteada)-1]
            if dezenaSorteada.__contains__('00'):
                dezenaSorteada.__delitem__(dezenaSorteada.index('00'))
                dezenaSorteada.append('60')
                return dezenaSorteada


dezenasMegaSena = []
dezenasMegaSena = megaSena()
dezenasMegaSena.sort()

for i in dezenasMegaSena:
    print(i)
