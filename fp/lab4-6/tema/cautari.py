from structura import get_suma_cheltuiala,get_ziua_cheltuiala,get_tip_cheltuiala
def cheltuieli_mai_mari_decat_sumap(lista_cheltuieli,suma_p):
  '''
  functia returneaza subsirul care are suma mai mare decat suma_p
  :parem lista_cheltuieli, lista de cheltuieli
  :parem suma_p
  :return subsirul care are suma mai mare decat suma_p
  '''

  subsir =[]
  for cheltuiala in lista_cheltuieli:
    if get_suma_cheltuiala(cheltuiala) >= suma_p:
      subsir.append(cheltuiala)

  return subsir

def cheltuieli_mai_mici_sumap_inainte_ziuap(lista_cheltuieli,suma_p,ziua_p):
  '''
  functia returneaza un subsir care are suma mai mica decat suma_p si inainte de ziua_p
  :parem lista_cheltuieli, lista de cheltuieli
  :parem suma_p
  :parem ziua_p
  :return subsirul care are suma mai mica decat suma_p si inainte de ziua_p
  '''

  subsir =[]
  for cheltuiala in lista_cheltuieli:
    if get_suma_cheltuiala(cheltuiala) <= suma_p and get_ziua_cheltuiala(cheltuiala) <= ziua_p:
      subsir.append(cheltuiala)

  return subsir

def cheltuieli_dupa_tip(lista_cheltuieli,tip):
  '''
  functia returneaza subsirul cu cheltuielile de un anumit tip
  :parem lista_cheltuieli, lista de cheltuieli
  :parem tip, tipul
  :return subsirul
  '''
  
  subsir = []
  for cheltuiala in lista_cheltuieli:
    if get_tip_cheltuiala(cheltuiala) == tip:
      subsir.append(cheltuiala)

  return subsir
    
def test_cheltuieli_mai_mari_decat_sumap():
  lista_cheltuieli = [[10,144.5,"altele"],[5,50,"altele"],[12,80.94,"altele"],[15,223.45,"altele"]]
  assert cheltuieli_mai_mari_decat_sumap(lista_cheltuieli,144.6) == [[15,223.45,"altele"]]
  assert cheltuieli_mai_mari_decat_sumap(lista_cheltuieli,80.93) == [[10,144.5,"altele"],[12,80.94,"altele"],[15,223.45,"altele"]]
  assert cheltuieli_mai_mari_decat_sumap([],100) == []

def test_cheltuieli_mai_mici_sumap_inainte_ziuap():
  lista_cheltuieli = [[12,50.45,"altele"],[5,76.34,"altele"],[6,40.20,"altele"],[10,120.4,"altele"]]
  assert cheltuieli_mai_mici_sumap_inainte_ziuap(lista_cheltuieli,100,8) == [[5,76.34,"altele"],[6,40.20,"altele"]]
  assert cheltuieli_mai_mici_sumap_inainte_ziuap(lista_cheltuieli,40,2) == []
  assert cheltuieli_mai_mici_sumap_inainte_ziuap(lista_cheltuieli,150,11) == [[5,76.34,"altele"],[6,40.20,"altele"],[10,120.4,"altele"]]
  assert cheltuieli_mai_mici_sumap_inainte_ziuap([],200,20) == []

def test_cheltuieli_dupa_tip():
  lista_cheltuieli = [[10,20.4,"altele"],[30,19,"telefoane"],[2,90,"altele"],[7,1000,"mancare"],[1,634,"mancare"],[24,431,"altele"]]
  assert cheltuieli_dupa_tip(lista_cheltuieli,"altele") == [[10,20.4,"altele"],[2,90,"altele"],[24,431,"altele"]]
  assert cheltuieli_dupa_tip(lista_cheltuieli,"telefoane") == [[30,19,"telefoane"]]
  assert cheltuieli_dupa_tip(lista_cheltuieli,"mancare") == [[7,1000,"mancare"],[1,634,"mancare"]]

def test_wrapper():
  test_cheltuieli_mai_mari_decat_sumap()
  test_cheltuieli_mai_mici_sumap_inainte_ziuap()
  test_cheltuieli_dupa_tip()

def main():
  test_wrapper()

main()
