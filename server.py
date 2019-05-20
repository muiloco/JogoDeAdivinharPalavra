import Pyro4

@Pyro4.expose
@Pyro4.behavior(instance_mode="single")

class Palavra(object):
    def __init__(self, palavra, dica):
        self.palavra = palavra
        self.dica = dica

deamon = Pyro4.Daemon()
ns = Pyro4.locateNS()
uri = deamon.register(Palavra)
ns.register("palavra",uri)
deamon.requestLoop()