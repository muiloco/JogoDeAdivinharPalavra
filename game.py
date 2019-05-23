import Pyro4

rodaroda = Pyro4.Proxy("PYRONAME:palavra")
while True:
    adivinhar=""
    for letra in rodaroda.palavra:
        adivinhar += letra if letra in rodaroda.acerto else "_"
    print(adivinhar)
    print(rodaroda.dica)
    if rodaroda.conferirPalavra(adivinhar):
        print("Voce acertou miseravi!!!")
        break
    chute = input("Digite uma letra:\n").lower().strip()
    if chute in rodaroda.erros:
        print("Vc já chutou isso tenta outra tipo b!!\n")
        continue
    else:
        rodaroda.erros += chute
        if chute in rodaroda.palavra:
            rodaroda.acerto += chute
        else:
            erro += 1
    if rodaroda.chances == erro:
        print("Erou, vc e ruim começa de novo!!")
        break
