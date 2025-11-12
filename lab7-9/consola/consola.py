from domeniu.student import Student
from domeniu.disciplina import Disciplina

from servicii.service_student import ServiceStudenti
from servicii.service_note import ServiceNote
from servicii.service_disciplina import ServiceDisciplina

from exceptii.EroareUI import EroareUI


class Consola:

    def __init__(self, service_studenti: ServiceStudenti, service_note: ServiceNote, service_disciplina: ServiceDisciplina):
        self.__service_studenti = service_studenti
        self.__service_note = service_note
        self.__service_disciplina = service_disciplina
        self.__comenzi = {
            "adauga_student": [self.ui_adauga_student, 1, [str]],
            "afiseaza_studenti": [self.ui_afiseaza_student, 0, []],
            "sterge_student": [self.ui_sterge_student, 2, [int, str]],
            "update_student": [self.ui_update_student, 2, [int, str]],
            "adauga_disciplina": [self.ui_adauga_disciplina, 2, [str, str]],
            "sterge_disciplina": [self.ui_sterge_disciplina, 3, [int, str, str]],
            "afiseaza_disciplina": [self.ui_afisare_discipline, 0, []],
            "update_disciplina": [self.ui_update_disciplina, 3, [int, str, str]],
        }

    def run(self):
        while True:
            text_comanda = input(">>>>")
            text_comanda = text_comanda.strip()
            if text_comanda == "":
                continue
            if text_comanda == "exit":
                print("Sayonara, User")
                break

            if text_comanda == "help":
                self.ui_help()
                continue

            rezultat = text_comanda.split()
            comanda = rezultat[0]
            parametri_comanda = rezultat[1:]

            if comanda in self.__comenzi:
                try:
                    parametri_comanda = self.verificare_parametru(
                        comanda, parametri_comanda)
                    self.__comenzi[comanda][0](parametri_comanda)
                except EroareUI as eroare_ui:
                    print(f"eroare_ui: {eroare_ui}")

            else:
                print("Nu exista comanda")

    def ui_help(self):
        print(
            "1. adauga_student {nume} - adauga un nou student cu numele {nume}")
        print("2. afiseaza_studenti - afiseaza studentii")
        print(
            "3. sterge_student {id_student} {nume} - sterge studentul cu id_student = {id_student} si nume = {nume}")
        print(
            "4. update_student {id_student} {nume} - actualizeaza studentul cu idul {id_student} schimband numele in {nume}")
        print(
            "5. adauga_disciplina {nume_disciplina} {nume_profesor} - adauga o disciplina noua in repo cu un id unic")
        print("6. afiseaza_disciplina - afiseaza disciplinele")
        print(
            "7. sterge_disciplina {id_disciplina} {nume_disciplina} {nume_profesor} - sterge disciplina cu id ul dat")
        print(
            "8. update_disciplina {id_disciplina} {nume_disciplina} {nume_profesor} - actualizeaza disciplina cu {id_disciplina} cu numele introduse")

    def verificare_parametru(self, comanda, parametri_comanda):
        '''
        verifica daca parametrii comenzii sunt bune ca numar si tip
        :parem comanda -> comanda
        :parem parametri_comanda -> parametrii comenzii
        :return -
            raise eroare daca numarul de parametrii sunt gresit sau tipul parametrilor sunt gresit
        '''
        numarul_parametri_comanda = self.__comenzi[comanda][1]

        if len(parametri_comanda) != numarul_parametri_comanda:
            raise EroareUI("Numar gresit de parametri")

        instantele_comanda = self.__comenzi[comanda][2]

        erori = ""
        for i in range(numarul_parametri_comanda):
            instanta_buna = instantele_comanda[i]
            parametru = parametri_comanda[i]
            try:
                parametru = instanta_buna(parametru)
                parametri_comanda[i] = parametru
            except:
                erori += f"Parametrul {i+1} nu este de tipul {instanta_buna}"

        if len(erori) != 0:
            raise EroareUI(erori)

        return parametri_comanda

    def ui_adauga_student(self, parametri_comanda):
        '''
        adauga student nou in repository
        :parem parametri_comanda -> parametrii comenzii
        :return -
        '''

        nume_student = parametri_comanda[0]
        id_student = self.__service_studenti.creare_id_student()
        student = Student(id_student, nume_student)
        self.__service_studenti.adauga_student(student)

    def ui_afiseaza_student(self, parametri_comanda):
        '''
        afiseaza studentii memorati
        :parem paremetri_comanda -> parametrii comenzii
        :return lista de stundeti
        '''
        print(self.__service_studenti.afiseaza_studentii())

    def ui_sterge_student(self, parametri_comanda):
        '''
        sterge student din student repo
        :parem parametri_comanda -> parametrii comenzii
        :return -
        '''
        id_student = parametri_comanda[0]
        nume = parametri_comanda[1]
        student = Student(id_student, nume)

        self.__service_studenti.stergere_student(student)

    def ui_update_student(self, parametri_comanda):
        '''
        update la un student deja existent schimband numele
        :parem parametri_comanda -> parametrii comenzii
        :return -
        '''
        id_student = parametri_comanda[0]
        nume = parametri_comanda[1]
        student = Student(id_student, nume)

        self.__service_studenti.update_student(student)

    def ui_adauga_disciplina(self, parametri_comanda):
        '''
        adauga o noua disciplina in repo_disciplina
        :parem parametri_comanda -> parametrii comenzii
        :return -
        '''
        id_disciplina = self.__service_disciplina.creeare_id_disciplina()
        nume_disciplina = parametri_comanda[0]
        nume_profesor = parametri_comanda[1]
        disciplina = Disciplina(id_disciplina, nume_disciplina, nume_profesor)

        self.__service_disciplina.adauga_disciplina(disciplina)

    def ui_sterge_disciplina(self, parametri_comanda):
        '''
        sterge o disciplina din repo
        :parem parametri_comanda -> parametrii comenzii
        '''
        id_disciplina = parametri_comanda[0]
        nume_disciplina = parametri_comanda[1]
        nume_profesor = parametri_comanda[2]
        disciplina = Disciplina(id_disciplina, nume_disciplina, nume_profesor)

        self.__service_disciplina.sterge_disciplina(disciplina)

    def ui_afisare_discipline(self, parametri_comanda):
        '''
        afiseaza toate disciplinele
        :parem parametrii comanda -> parametrii comenzii
        :return -
        '''
        self.__service_disciplina.afiseaza_discipline()

    def ui_update_disciplina(self, parametri_comanda):
        '''
        da update la o disciplina
        :parem parametri_comanda -> parametrii comenzi
        '''
        id_disciplina = parametri_comanda[0]
        nume_disciplina = parametri_comanda[1]
        nume_profesor = parametri_comanda[2]

        disciplina = Disciplina(id_disciplina, nume_disciplina, nume_profesor)
        self.__service_disciplina.update_disciplina(disciplina)
