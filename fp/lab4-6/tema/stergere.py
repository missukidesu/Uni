from structura import get_ziua_cheltuiala,get_tip_cheltuiala

def stergere_cheltuieli_din_ziua_p(lista_cheltuieli,ziua_p):
  '''
  Sterge toate cheltuielile facute in ziua p
  :parem lista_cheltuieli, lista de cheltuieli
  :parem ziua_p, ziua pe care vrea sa stearga utilizatorul
  :return lista de cheltuieli updatata
  '''

  for cheltuiala in lista_cheltuieli:
    if get_ziua_cheltuiala(cheltuiala) == ziua_p:
      lista_cheltuieli.remove(cheltuiala)

  return lista_cheltuieli

def stergere_cheltuieli_din_intervalul_ziua1_ziua2(lista_cheltuieli,ziua1,ziua2):
  '''
  Sterge toate cheltuielile facute in intervalul ziua1 si ziua2, unde ziua1 <= ziua2
  :parem lista_cheltuieli, lista de cheltuieli
  :parem ziua1, ziua inferioara
  :parem ziua2, ziua superioara
  :return lista de cheltuieli updatata
  '''
  
  if (ziua2<ziua1):
    ziua1,ziua2 = ziua2,ziua1

  index = 0
  while index< len(lista_cheltuieli):
    cheltuiala = lista_cheltuieli[index]
    if (get_ziua_cheltuiala(cheltuiala)>=ziua1) and (get_ziua_cheltuiala(cheltuiala)<=ziua2):
      lista_cheltuieli.remove(cheltuiala)
    else:
        index+=1

  return lista_cheltuieli

def stergere_cheltuieli_dupa_tip(lista_cheltuieli,tip_p):
  '''
  Sterge toate cheltuielile de un anumit tip
  :parem lista_cheltuieli, lista de cheltuieli
  :parem tip_p, tipul pe care vreau sa l sterg
  :return lista de cheltuieli updatata
  '''
  
  index = 0
  while index<len(lista_cheltuieli):
    cheltuiala = lista_cheltuieli[index]
    if get_tip_cheltuiala(cheltuiala) == tip_p:
      lista_cheltuieli.remove(cheltuiala)
    else:
      index+=1

  return lista_cheltuieli

def test_stergere_cheltuieli_din_ziua_p():
  assert stergere_cheltuieli_din_ziua_p([[1,10,"altele"],[2,15,"altele"]],1) == [[2,15,"altele"]]
  assert stergere_cheltuieli_din_ziua_p([[1,22,"altele"],[4,40,"altele"],[1,20,"mancare"]],1) == [[4,40,"altele"]]
  assert stergere_cheltuieli_din_ziua_p([[3,24,"altele"],[1,20,"altele"],[2,5,"altele"]],3) == [[1,20,"altele"],[2,5,"altele"]]
  assert stergere_cheltuieli_din_ziua_p([],20) == []

def test_stergere_cheltuieli_din_intervalul_ziua1_ziua2():
  assert stergere_cheltuieli_din_intervalul_ziua1_ziua2([[1,10,"altele"],[2,15,"altele"],[3,20,"altele"],[4,25,"altele"]],1,3) == [[4,25,"altele"]]
  assert stergere_cheltuieli_din_intervalul_ziua1_ziua2([[2,30,"altele"],[3,5,"altele"],[1,15,"altele"]],3,3) == [[2,30,"altele"],[1,15,"altele"]]
  assert stergere_cheltuieli_din_intervalul_ziua1_ziua2([],3,10) == []

def test_stergere_cheltuieli_dupa_tip():
  assert stergere_cheltuieli_dupa_tip([],"altele") == []
  assert stergere_cheltuieli_dupa_tip([[2,20,"altele"],[1,15,"altele"],[2,10,"mancare"]],"altele") == [[2,10,"mancare"]]
  assert stergere_cheltuieli_dupa_tip([[3,10,"altele"],[2,5,"telefoane"],[10,20,"mancare"]],"telefoane") == [[3,10,"altele"],[10,20,"mancare"]]

if __name__ == "__main__":
  test_stergere_cheltuieli_din_ziua_p()
  test_stergere_cheltuieli_din_intervalul_ziua1_ziua2()
  test_stergere_cheltuieli_dupa_tip()
