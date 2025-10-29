from structura import creeaza_cheltuiala,verificare_cheltuiala,get_ziua_cheltuiala,get_tip_cheltuiala,get_suma_cheltuiala
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

def suma_totala_dupa_tip(lista_cheltuieli,tip):
    '''
    fuctie care returneaza suma totala dupa tip
    :parem lista_cheltuieli, lista de cheltuieli
    :parem tip, tipul
    :return suma totala
    '''
    total_suma = 0
    for cheltuiala in lista_cheltuieli:
        if get_tip_cheltuiala(cheltuiala) == tip:
            total_suma += get_suma_cheltuiala(cheltuiala)
    return total_suma

def max_suma_dupa_zii(lista_cheltuieli):
    '''
    functie care returneaza suma maxima dupa zii
    :parem lista_cheltuieli, lista de cheltuieli
    :return suma maxima
    '''
    suma_dupa_zii = []
    for index in range(31):
        suma_dupa_zii.append(0)

    for cheltuiala in lista_cheltuieli:
        suma_dupa_zii[get_ziua_cheltuiala(cheltuiala)] += get_suma_cheltuiala(cheltuiala)

    suma_max = 0
    index = 0
    index_max = 0
    for suma in suma_dupa_zii:
        if suma>suma_max:
            index_max = index
            suma_max = suma
        index+=1

    return index_max

def cheltuiala_cu_sumap(lista_cheltuieli,sumap):
    '''
    functie care returneaza cheltuielile care au suma exacta cu o suma data
    :parem lista_cheltuieli, lista de cheltuieli
    :parem sumap, suma
    :return returneaza un subsir cu cheltuielile care au suma egala cu sumap
    '''
    subsir = []
    for cheltuiala in lista_cheltuieli:
        if abs(get_suma_cheltuiala(cheltuiala) - sumap) < 0.000001:
            subsir.append(cheltuiala)

    return subsir

def sortare_lista_cheltuieli_dupa_tip(lista_cheltuieli):
    '''
    functie care returneaza lista de cheltuieli ordonata
    :parem lista_cheltuieli, lista de cheltuieli
    :return lista nou sortata
    '''
    lista_cheltuieli_sortata = sorted(lista_cheltuieli, key=lambda cheltuiala: (get_tip_cheltuiala(cheltuiala),get_ziua_cheltuiala(cheltuiala),get_suma_cheltuiala(cheltuiala)))
    return lista_cheltuieli_sortata

def filtrarea_cheltuielilor_cu_tip_p(lista_cheltuieli,tip):
    '''
    functie care returneaza subsirul filtrat pe tip
    :parem lista_cheltuieli, lista de cheltuieli
    :parem tip, tipul pe care vrem sa l pastram
    :return returneaza subsirul filtrat
    '''
    subsir = []
    for cheltuiala in lista_cheltuieli:
        if get_tip_cheltuiala(cheltuiala) != tip:
            subsir.append(cheltuiala)

    return subsir

def filtrarea_cheltuielilor_cu_suma_mai_mica_sumap(lista_cheltuieli,sumap):
    '''
    functie care returneaza subsirul filtrat care au suma mai mica decat sumap
    :parem lista_cheltuieli, lista de cheltuieli
    :parem sumap, o suma data
    :return subsir care cheltuielile sunt mai mici decat sumap
    '''
    subsir = []
    for cheltuiala in lista_cheltuieli:
        if get_suma_cheltuiala(cheltuiala) - sumap >= 0.000001:
            subsir.append(cheltuiala)

    return subsir

