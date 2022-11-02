class Carta:
  listaFiguras = ["Treboles", "Diamantes", "Corazones", "Picas"]
  listaValores = ["vacio", "A", "2", "3", "4", "5", "6", "7","8", "9", "10", "J", "Q", "K"]
  
  def __int__(self, figura=0, valor=0):
    self.figura = figura
    self.valor = valor

  def __str__(self):
    return (self.listaValores[self.valor] + " de " +
    self.listaFiguras[self.figura])

  def __cmp__(self, otro):
    if self.figura > otro.figura: return 1
    if self.figura < otro.figura: return -1
    if self.valor > otro.valor: return 1
    if self.valor < otro.valor: return -1
    return 0
    
class Mazo:
  def __init__(self):
    self.cartas = []
    for figura in range(4):
      for valor in range(1, 14):
          self.cartas.append(Carta(figura, valor))

  def __str__(self):
    s = ""
    for i in range(len(self.cartas)):
      s = s + " "*i + str(self.cartas[i]) + "\n"
    return s

  def imprimirMazo(self):
    for carta in self.cartas:
      print (carta)

#SE BARAJAN LAS CARTAS
    def barajar(self):
      import random
      nCartas = len(self.cartas)
      for i in range(nCartas):
        j = random.randrange(i, nCartas)
        self.cartas[i], self.cartas[j] = self.cartas[j], self.cartas[i]

mazo = Mazo()
mazo.imprimirMazo()
