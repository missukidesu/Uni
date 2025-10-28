from structura import creeaza_cheltuiala,verificare_cheltuiala,get_ziua_cheltuiala,get_tip_cheltuiala
def inserare(lista_cheltuieli, ziua, suma, tip):
  '''
  insereaza o noua cheltuiala la sfarsitul listei de cheltuieli
  :param lista_cheltuieli, lista de cheltuieli
  :param ziua, ziua cheltuielii
  :param suma, suma cheltuielii
  :param tip, tipul cheltuielii
  :return lista de cheltuieli updatata
  :raise ValueError - daca voia sa se insereze valori invalide
  '''
  try:
    cheltuiala = creeaza_cheltuiala(ziua,suma,tip)
    verificare_cheltuiala (cheltuiala)
    lista_cheltuieli.append(cheltuiala)
    return lista_cheltuieli
  except ValueError as e:
    print("Eroare:")
    print(e)

def actualizare(lista_cheltuieli, ziua, suma, tip):
  """
  se actualizeaza cheltuiala de pe ziua si tipul dat si se inlocuieste suma cu suma noua
  :parem lista_cheltuieli, lista de cheltuieli
  :parem ziua, ziua cheltuielii
  :parem suma, suma cheltuielii
  :parem tip, tipul cheltuielii
  :return lista de cheltuieli updatata
  :raise ValueError - daca s au introdus valori invalide
  """
  cheltuiala_actualizata = creeaza_cheltuiala(ziua,suma,tip)
  for cheltuiala in lista_cheltuieli:
    if (get_ziua_cheltuiala(cheltuiala) == ziua) and (get_tip_cheltuiala(cheltuiala) == tip):
      lista_cheltuieli.remove(cheltuiala)
      lista_cheltuieli.append(cheltuiala_actualizata)
      return lista_cheltuieli

  print("Nu am gasit cheltuiala")
  return lista_cheltuieli

def test_inserare():
  lista_cheltuieli = [[1,1.0,"altele"]]
  assert inserare (lista_cheltuieli,20,100.0,"mancare") == [[1,1.0,"altele"],[20,100.0,"mancare"]]
  assert inserare (lista_cheltuieli,30,100.0,"mancare") == [[1,1.0,"altele"],[20,100.0,"mancare"],[30,100.0,"mancare"]]

def test_actualizare():
  lista_cheltuieli = [[1,1.0,"altele"],[2,2.0,"mancare"],[10,124.4,"telefoane"]]
  assert actualizare(lista_cheltuieli,1,10.2,"altele") == [[2,2.0,"mancare"],[10,124.4,"telefoane"],[1,10.2,"altele"]]

def test_wrapper():
  test_inserare()
  test_actualizare()
  
def main():
  test_wrapper()
  lista_cheltuieli = []

main()
