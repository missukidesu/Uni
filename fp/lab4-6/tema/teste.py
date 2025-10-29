from functionalitati import *

def test_inserare():
  lista_cheltuieli = [[1,1.0,"altele"]]
  assert inserare (lista_cheltuieli,20,100.0,"mancare") == [[1,1.0,"altele"],[20,100.0,"mancare"]]
  assert inserare (lista_cheltuieli,30,100.0,"mancare") == [[1,1.0,"altele"],[20,100.0,"mancare"],[30,100.0,"mancare"]]

def test_actualizare():
  lista_cheltuieli = [[1,1.0,"altele"],[2,2.0,"mancare"],[10,124.4,"telefoane"]]
  assert actualizare(lista_cheltuieli,1,10.2,"altele") == [[2,2.0,"mancare"],[10,124.4,"telefoane"],[1,10.2,"altele"]]

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

def test_filtrarea_cheltuielilor_cu_tip_p():
    assert filtrarea_cheltuielilor_cu_tip_p([],"altele") == []
    assert filtrarea_cheltuielilor_cu_tip_p([[5,10,"mancare"],[1,4,"altele"],[2,123,"mancare"]],"mancare") == [[5,10,"mancare"],[2,123,"mancare"]]
    assert filtrarea_cheltuielilor_cu_tip_p([[14,203,"altele"],[21,21,"mancare"],[30,20,"telefoane"]],"altele") == [[14,203,"altele"]]

def test_filtrarea_cheltuielilor_cu_suma_mai_mica_sumap():
    assert filtrarea_cheltuielilor_cu_suma_mai_mica_sumap([],100) == []
    assert filtrarea_cheltuielilor_cu_suma_mai_mica_sumap([[4,4,"mancare"],[10,24,"mancare"],[9,51,"altele"],[3,12,"altele"]],12.1) == [[4,4,"mancare"],[3,12,"altele"]]
    assert filtrarea_cheltuielilor_cu_suma_mai_mica_sumap([[10,20,"telefoane"],[7,15,"altele"],[12,32,"altele"],[12,30.43,"altele"]],12) == []
    assert filtrarea_cheltuielilor_cu_suma_mai_mica_sumap([[8,14.42,"altele"],[9,15.43,"mancare"],[10,320.413,"altele"],[1,43,"altele"]],18.3) == [[8,14.42,"altele"],[9,15.43,"mancare"]]

def test_wrapper():
    test_inserare()
    test_actualizare()
    test_stergere_cheltuieli_din_ziua_p()
    test_stergere_cheltuieli_din_intervalul_ziua1_ziua2()
    test_stergere_cheltuieli_dupa_tip()
    test_cheltuieli_mai_mari_decat_sumap()
    test_cheltuieli_mai_mici_sumap_inainte_ziuap()
    test_cheltuieli_dupa_tip()
    test_suma_totala_dupa_tip()
    test_max_suma_dupa_zii()
    test_cheltuiala_cu_sumap()
    test_sortare_lista_cheltuieli_dupa_tip()
    test_filtrarea_cheltuielilor_cu_tip_p()
    test_filtrarea_cheltuielilor_cu_suma_mai_mica_sumap()

def main():
    test_wrapper()

main()
