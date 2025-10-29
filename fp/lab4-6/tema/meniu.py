from functionalitati import *
from structura import verificare_cheltuiala
def afisare_comenzi():
    pass

def ui_inserare(context):
    lista_cheltuieli = context["lista_cheltuieli"]
    parametri_comanda = context["parametri"]
    if len(parametri_comanda) != 3:
        raise ValueError("numar de parametri invalid")

    ziua =int( parametri_comanda[0])
    suma = float(parametri_comanda[1])
    tip = parametri_comanda[2]
    
    cheltuiala = [ziua,suma,tip]
    try:
        verificare_cheltuiala(cheltuiala)
    except ValueError as eroare:
        print(eroare)

    return inserare(lista_cheltuieli,ziua,suma,tip)

def ui_actualizare(context):
    lista_cheltuieli = context["lista_cheltuieli"]
    parametri_comanda = context["parametri"]
    if len(parametri_comanda) != 3:
        raise ValueError("numar de parametri invalid")

    ziua = int(parametri_comanda[0])
    suma = float(parametri_comanda[1])
    tip = parametri_comanda[2]

    cheltuiala = [ziua,suma,tip]
    try:
        verificare_cheltuiala(cheltuiala)
    except ValueError as eroare:
        print(eroare)

    return actualizare(lista_cheltuieli,ziua,suma,tip)

def ui_stergere_cheltuieli_din_ziua_p(context):
    lista_cheltuieli = context["lista_cheltuieli"]
    parametri_comanda = context["parametri"]
    if len(parametri_comanda) != 1:
        raise ValueError("numar de parametri invalid")

    ziua =int( parametri_comanda[0])

    cheltuiala = [ziua,1,"altele"]
    try:
        verificare_cheltuiala(cheltuiala)
    except ValueError as eroare:
        print(eroare)

    return stergere_cheltuieli_din_ziua_p(lista_cheltuieli,ziua)

def ui_stergere_cheltuieli_din_intervalul_ziua1_ziua2(context):
    lista_cheltuieli = context["lista_cheltuieli"]
    parametri_comanda = context["parametri"]
    if len(parametri_comanda) != 2:
        raise ValueError("numar de parametri invalid")

    ziua1 = int(parametri_comanda[0])
    ziua2 = int(parametri_comanda[1])

    cheltuiala1 = [ziua1,1,"altele"]
    cheltuiala2 = [ziua2,1,"altele"]

    try:
        verificare_cheltuiala(cheltuiala1)
        verificare_cheltuiala(cheltuiala2)
    except ValueError as eroare:
        print(eroare)

    return stergere_cheltuieli_din_intervalul_ziua1_ziua2(lista_cheltuieli,ziua1,ziua2)

def ui_stergere_cheltuieli_dupa_tip(context):
    lista_cheltuieli = context["lista_cheltuieli"]
    parametri_comanda = context["parametri"]
    if len(parametri_comanda) != 1:
        raise ValueError("numar de parametri invalid")

    tip = parametri_comanda[0]

    cheltuiala = [1,1,tip]
    try:
        verificare_cheltuiala(cheltuiala)
    except ValueError as eroare:
        print(eroare)

    return stergere_cheltuieli_dupa_tip(lista_cheltuieli,tip)

def ui_cheltuieli_mai_mari_decat_sumap(context):
    lista_cheltuieli = context["lista_cheltuieli"]
    parametri_comanda = context["parametri"]
    if len(parametri_comanda) != 1:
        raise ValueError("numar de parametri invalid")

    suma = float(parametri_comanda[0])

    cheltuiala = [1,suma,"altele"]
    try:
        verificare_cheltuiala(cheltuiala)
    except ValueError as eroare:
        print(eroare)

    subsir = cheltuieli_mai_mari_decat_sumap(lista_cheltuieli,suma)
    print(subsir)

def ui_cheltuieli_mai_mici_sumap_inainte_ziuap(context):
    lista_cheltuieli = context["lista_cheltuieli"]
    parametri_comanda = context["parametri"]
    if len(parametri_comanda) != 2:
        raise ValueError("numar de parametri invalid")

    ziua = int(parametri_comanda[0])
    suma = float(parametri_comanda[1])

    cheltuiala = [ziua,suma,"altele"]

    try:
        verificare_cheltuiala(cheltuiala)
    except ValueError as eroare:
        print(eroare)

    subsir = cheltuieli_mai_mici_sumap_inainte_ziuap(lista_cheltuieli,ziua,suma)
    print(subsir)

def ui_cheltuieli_dupa_tip(context):
    lista_cheltuieli = context["lista_cheltuieli"]
    parametri_comanda = context["parametri"]
    if len(parametri_comanda) != 1:
        raise ValueError("numar de parametri invalid")

    tip = parametri_comanda[0]

    cheltuiala = [1,1,tip]

    try:
        verificare_cheltuiala(cheltuiala)
    except ValueError as eroare:
        print(eroare)

    subsir = cheltuieli_dupa_tip(lista_cheltuieli,tip)
    print(subsir)

def ui_suma_totala_dupa_tip(context):
    lista_cheltuieli = context["lista_cheltuieli"]
    parametri_comanda = context["parametri"]
    if len(parametri_comanda) != 1:
        raise ValueError("numar de parametri invalid")

    tip = parametri_comanda[0]
    cheltuiala = [1,1,tip]

    try:
        verificare_cheltuiala(cheltuiala)
    except ValueError as eroare:
        print(eroare)
    total = suma_totala_dupa_tip(lista_cheltuieli,tip)
    print(total)

def ui_max_suma_dupa_zii(context):
    lista_cheltuieli = context["lista_cheltuieli"]
    parametri_comanda = context["parametri"]
    if len(parametri_comanda) != 0:
        raise ValueError("numar de parametri invalid")

    cheltuiala = [1,1,"altele"]

    try:
        verificare_cheltuiala(cheltuiala)
    except ValueError as eroare:
        print(eroare)
    max = max_suma_dupa_zii(lista_cheltuieli)

def ui_cheltuiala_cu_sumap(context):
    lista_cheltuieli = context["lista_cheltuieli"]
    parametri_comanda = context["parametri"]
    if len(parametri_comanda) != 1:
        raise ValueError("numar de parametri invalid")

    suma = float(parametri_comanda[0])
    cheltuiala = [1,suma,"altele"]

    try:
        verificare_cheltuiala(cheltuiala)
    except ValueError as eroare:
        print(eroare)
    return cheltuiala_cu_sumap(lista_cheltuieli,suma)

def ui_sortare_lista_cheltuieli_dupa_tip(context):
    lista_cheltuieli = context["lista_cheltuieli"]
    parametri_comanda = context["parametri"]
    if len(parametri_comanda) != 0:
        raise ValueError("numar de parametri invalid")

    cheltuiala = [1,1,"altele"]

    try:
        verificare_cheltuiala(cheltuiala)
    except ValueError as eroare:
        print(eroare)
    return sortare_lista_cheltuieli_dupa_tip(lista_cheltuieli)

def ui_filtrarea_cheltuielilor_cu_tip_p(context):
    lista_cheltuieli = context["lista_cheltuieli"]
    parametri_comanda = context["parametri"]
    if len(parametri_comanda) != 1:
        raise ValueError("numar de parametri invalid")

    tip = parametri_comanda[0]
    cheltuiala = [1,1,tip]

    try:
        verificare_cheltuiala(cheltuiala)
    except ValueError as eroare:
        print(eroare)
    
    return filtrarea_cheltuielilor_cu_tip_p(lista_cheltuieli,tip)


def ui_filtrarea_cheltuielilor_cu_suma_mai_mica_sumap(context):
    lista_cheltuieli = context["lista_cheltuieli"]
    parametri_comanda = context["parametri"]
    if len(parametri_comanda) != 1:
        raise ValueError("numar de parametri invalid")

    suma = float(parametri_comanda[0])
    cheltuiala = [1,suma,"altele"]

    try:
        verificare_cheltuiala(cheltuiala)
    except ValueError as eroare:
        print(eroare)
    
    return filtrarea_cheltuielilor_cu_suma_mai_mica_sumap(lista_cheltuieli,suma)

def help():
    print("1. insereaza_cheltuiala_noua {ziua} {suma} {tip} - insereaza o cheltuiala noua in lista cu parametrii dati")
    print("2. actualizeaza_o_cheltuiala {ziua} {suma} {tip} - actualizeaza cheltuiala care are ziua si tipul la fel cu suma data, dar daca nu ii nu se intampla nimica")
    print("3. sterge_o_cheltuiala_dintro_zi {ziua} - sterge toate cheltuielile din ziua {ziua}")
    print("4. stergere_cheltuielile_din_intervalul_a_2zile {ziua1} {ziua2} - sterge toate cheltuielile din intervalul [min(ziua1,ziua2),max(ziua1,ziua2)")
    print("5. stergere_cheltuielile_de_un_anumit_tip {tip} - sterge toate cheltuielile de tipul {tip}")
    print("6. sorteaza_lista_dupa_tip - sorteaza lista de cheltuieli dupa tip, zii, suma")
    print("7. filtrarea_cheltuielilor_care_au_tipul_dat {tip} - elimina toate cheltuielile care au tipul {tip}")
    print("8. filtrarea_cheltuielilor_cu_suma_mai_mica_decat_o_suma {suma} - elimina toate cheltuielile mai mici decat suma {suma}")
    print("9. afiseaza_cheltuielile_mai_mari_decat_o_suma {suma} - afiseaza toate cheltuielile care au suma strict mai mare decat {suma}")
    print("10. afiseaza_cheltuielile_mai_mici_decat_o_suma_inainte_de_o_zii {ziua} {suma} - afiseaza toate cheltuielile care au ziua mai mica decat {ziua} si suma mai mica decat {suma}")
    print("11. afiseaza_cheltuielile_cu_tipul_dat {tip} - afiseaza toate cheltuielile care au tipul {tip}")
    print("12. afiseaza_ziua_cu_suma_maxima - afiseaza ziua care are suma maxima")
    print("13. afiseaza_cheltuielile_care_au_suma_egala_cu_una_data {suma} - afiseaza toate cheltuielile care au suma egala cu {suma}")
    print("14. exit - se inchide programu")

def run():
    lista_cheltuieli = []
    comenzi_modificare = {
        "insereaza_cheltuiala_noua":ui_inserare,
        "actualizeaza_o_cheltuiala":ui_actualizare,
        "sterge_o_cheltuiala_dintro_zi":ui_stergere_cheltuieli_din_ziua_p,
        "stergere_cheltuielile_din_intervalul_a_2zile":ui_stergere_cheltuieli_din_intervalul_ziua1_ziua2,
        "stergere_cheltuielile_de_un_anumit_tip": ui_stergere_cheltuieli_dupa_tip,
        "sortareaza_lista_dupa_tip": ui_sortare_lista_cheltuieli_dupa_tip,
        "filtrarea_cheltuielilor_care_au_tipul_dat": ui_filtrarea_cheltuielilor_cu_tip_p,
        "filtrarea_cheltuielilor_cu_suma_mai_mica_decat_o_suma": ui_filtrarea_cheltuielilor_cu_suma_mai_mica_sumap
    }
    comenzi_afisare = {
        "afiseaza_cheltuielile_mai_mari_decat_o_suma": ui_cheltuieli_mai_mari_decat_sumap,
        "afiseaza_cheltuielile_mai_mici_decat_o_sumap_inainte_de_o_zii": ui_cheltuieli_mai_mici_sumap_inainte_ziuap,
        "afiseaza_cheltuieli_cu_tipul_dat": ui_cheltuieli_dupa_tip,
        "afiseaza_suma_totala_a_cheltuielilor_cu_tipul_dat": ui_suma_totala_dupa_tip,
        "afiseaza_ziua_cu_suma_maxima": ui_max_suma_dupa_zii,
        "afiseaza_cheltuielile_cu_o_suma": ui_cheltuiala_cu_sumap,
    }   
    while True:
        print(lista_cheltuieli)
        text_comanda = input(">>>")
        text_comanda = text_comanda.strip()
        if text_comanda == "":
            continue
        if text_comanda == "exit":
            print("Sayonara, user!")
            break
        if text_comanda == "help":
            help()
            continue
        elemente_comanda = text_comanda.split()
        nume_comanda = elemente_comanda[0]
        parametri_comanda = elemente_comanda[1:]
        if nume_comanda in comenzi_modificare:
            context ={
                "lista_cheltuieli": lista_cheltuieli,
                "parametri": parametri_comanda
                }
            try:
                lista_cheltuieli = comenzi_modificare[nume_comanda](context)
            except ValueError as eroare:
                print(eroare)
        elif nume_comanda in comenzi_afisare:
            context ={
                    "lista_cheltuieli": lista_cheltuieli,
                    "parametri": parametri_comanda
            }
            try:
                comenzi_afisare[nume_comanda](context)
            except ValueError as eroare:
                print(eroare)
        else:
            print("nu am aceasta comanda")

def main():
    run()

if __name__ == "__main__":
    main()
