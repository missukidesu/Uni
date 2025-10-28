from structura import get_tip_cheltuiala,get_suma_cheltuiala,get_ziua_cheltuiala
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
    

def test_suma_totala_dupa_tip():
    assert suma_totala_dupa_tip([[5,24.4,"altele"],[4,100,"altele"]],"altele")-124.4 < 0.000001
    assert suma_totala_dupa_tip([[10,90.43,"mancare"],[6,23.43,"altele"],[7,44.3,"mancare"]],"mancare") - 134.73 < 0.000001
    assert suma_totala_dupa_tip([[7,45,"telefoane"],[1,90,"mancare"],[2,100,"altele"],[3,200,"telefoane"]],"mancare") - 90<0.000001

def test_max_suma_dupa_zii():
    assert max_suma_dupa_zii([[1,200,"altele"],[2,140,"altele"],[3,140,"altele"],[2,59,"altele"]]) == 1
    assert max_suma_dupa_zii([[2,159,"atlele"],[3,200,"altele"],[10,30.4,"altele"],[2,300,"altele"]]) == 2
    assert max_suma_dupa_zii([[1,100,"altele"],[15,150,"altele"],[10,30.4,"altele"],[10,140,"altele"]]) == 10

def test_cheltuiala_cu_sumap():
    assert cheltuiala_cu_sumap([],10) == []
    assert cheltuiala_cu_sumap([[2,20.2,"altele"]],20.2) == [[2,20.2,"altele"]]
    assert cheltuiala_cu_sumap([[3,30.1,"altele"],[4,10.2,"mancare"],[5,30.1,"altele"],[6,30.0,"altele"]],30.1) == [[3,30.1,"altele"],[5,30.1,"altele"]]

def test_sortare_lista_cheltuieli_dupa_tip():
    assert sortare_lista_cheltuieli_dupa_tip([]) == []
    assert sortare_lista_cheltuieli_dupa_tip([[4,1,"telefoane"],[10,20,"altele"],[15,15,"mancare"]]) == [[10,20,"altele"],[15,15,"mancare"],[4,1,"telefoane"]]
    assert sortare_lista_cheltuieli_dupa_tip([[2,10,"altele"],[10,1020,"altele"],[2,4,"altele"]]) == [[2,4,"altele"],[2,10,"altele"],[10,1020,"altele"]]
    assert sortare_lista_cheltuieli_dupa_tip([[10,200,"mancare"],[5,34,"altele"],[12,23,"mancare"],[10,23,"mancare"]]) == [[5,34,"altele"],[10,23,"mancare"],[10,200,"mancare"],[12,23,"mancare"]]

def test_wrapper():
    test_suma_totala_dupa_tip()
    test_max_suma_dupa_zii()
    test_cheltuiala_cu_sumap()
    test_sortare_lista_cheltuieli_dupa_tip()

def main():
    test_wrapper()

main()
