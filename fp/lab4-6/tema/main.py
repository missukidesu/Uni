from meniu import meniu
from inserare import actualizare,inserare
from stergere import stergere_cheltuieli_din_ziua_p, stergere_cheltuieli_din_intervalul_ziua1_ziua2,stergere_cheltuieli_dupa_tip
from cautari import cheltuieli_mai_mari_decat_sumap, cheltuieli_mai_mici_sumap_inainte_ziuap,cheltuieli_dupa_tip

def main():
  lista_cheltuieli = []
  while True:
    meniu.meniu_principal()
    mod = input("mod: ")
    if (mod == '1'):
      while True:
        meniu.meniu_inserare()
        mod = input("mod: ")
        if (mod == '1'):
          ziua,suma,tip = input("Scrieti o zii, o suma si un tip: ").split()
          inserare(lista_cheltuieli,int(ziua),float(suma),tip)
        elif (mod == '2'):
          ziua,suma,tip = input("Actualizati o cheltuiali, scrieti o zii, o suma si un tip: ")
          actualizare(lista_cheltuieli,int(ziua),float(suma),tip)
        elif (mod == '3'):
          break
        else:
          print("Nu am acest mod")
        print(lista_cheltuieli)
    elif (mod == '2'):
      while True:
        meniu.meniu_stergeri()
        mod_stergere = input("mod: ")
        if (mod_stergere == '1'):
          ziua = input("Stergere cheltuieli dupa o ziua. Introduceti o zii: ")
          stergere_cheltuieli_din_ziua_p(lista_cheltuieli,int(ziua))
        elif (mod_stergere == '2'):
          ziua1,ziua2 = input("Stergere cheltuieli din intervalul a 2 zile. Introduceti 2 zile: ").split()
          stergere_cheltuieli_din_intervalul_ziua1_ziua2(lista_cheltuieli,int(ziua1),int(ziua2))
        elif (mod_stergere == '3'):
          tip = input("Stergere cheltuieli dupa tip. Introduceti un tip: ")
          stergere_cheltuieli_dupa_tip(lista_cheltuieli,tip)
        elif (mod_stergere == '4'):
          break
        else:
          print("Nu am acest mod")
        print(lista_cheltuieli)
    elif (mod == '3'):
      while True:
        meniu.meniu_cautari()
        mod_cautari = input("mod: ")
        if mod_cautari == '1':
          suma = input("Cautatai cheltuielile cu o suma mai mare data. Introduceti suma: ")
          subsir = cheltuieli_mai_mari_decat_sumap(lista_cheltuieli,float(suma))
        elif mod_cautari == '2':
          ziua,suma = input("Cautati cheltuielile mai mici decat suma si inainte de o zii data. Introduceti o zii si o suma: ").split()
          subsir = cheltuieli_mai_mici_sumap_inainte_ziuap(lista_cheltuieli,int(ziua),float(suma))
        elif mod_cautari == '3':
          tip = input("Introduceti un tip: ")
          subsir = cheltuieli_dupa_tip(lista_cheltuieli,tip)
        elif mod_cautari == '4':
          break
        else:
          print("Nu am acest mod")
        print(subsir)
        print(lista_cheltuieli)
    elif mod == '4':
      break
    else:
      print("Nu am acest mod")

main()
