import Pyro4

@Pyro4.expose
@Pyro4.behavior(instance_mode="single")

class Palavra(object):
    def __init__(self, palavra, dica):
        self.palavra = palavra
        self.dica = dica

    def conferirLetra(letra):
        if letra in self.palavra:
            return True

    def conferirPalavra(palavra):
        if palavra == self.palavra:
            return True
        else:
            return False
    
palavra = input("Digite a sua palavra:")
dica = input("Digite sua dica:")

deamon = Pyro4.Daemon()
ns = Pyro4.locateNS()
uri = deamon.register(Palavra(palavra,dica))
ns.register("palavra",uri)
deamon.requestLoop()