class Biblioteka:

  def __init__(self):
    self.tytul = []
    self.autor = []
    self.rok = []

  def dodaj_ksiazke(self, ksiazka):
    self.rok.append(ksiazka)

  def dodaj_egzemplarz(self, egzemplarz):
    temp = list(egzemplarz)

    if temp [0:2] in self.rok:

      self.autor.append(temp[0:2])
      self.tytul.append(temp[0])

    else:
            
      biblioteka.dodaj_ksiazke(temp[0:2])
      self.autor.append(temp[0:2])
      self.tytul.append(temp[0])



  def zliczanie(self):
    lista = []
    posortowane = []


    for ksiazka in self.rok:
      k = self.autor.count(ksiazka)
      ksiazka = [ksiazka[0], ksiazka[1], k]
      lista.append(ksiazka)
      posortowane = sorted(lista, key = lambda x: x[0])

    
    for obj in posortowane:
      obj_1 = (obj[0], obj[1], obj[2])
      print(obj_1)
      

    
biblioteka = Biblioteka()
n = int(input())
for i in range(0,n):
    wejscie = eval(input())
    biblioteka.dodaj_egzemplarz(wejscie)

biblioteka.zliczanie()
    
