from repository.repository_disciplina import RepoDisciplina
from domeniu.disciplina import Disciplina
from exceptii.EroareRepo import EroareRepo


class ServiceDisciplina:

    def __init__(self, repo_disciplina: RepoDisciplina):
        self.__repo_disciplina = repo_disciplina

    def adauga_disciplina(self, disciplina: Disciplina):
        '''
        adauga o noua disciplina in repo_disciplina
        :parem disciplina -> disciplina
        :return -
        '''
        try:
            self.__repo_disciplina.adaugare_disciplina(disciplina)
        except EroareRepo as eroare:
            print("EroareRepo>>", eroare)

    def sterge_disciplina(self, disciplina: Disciplina):
        '''
        sterge o disciplina din repo
        :parem disciplina -> disciplina
        :return -
        '''
        try:
            self.__repo_disciplina.stergere_disciplina(disciplina)
        except EroareRepo as eroare:
            print("EroareRepo>>", eroare)

        print("Am sters cu succes disciplina")

    def update_disciplina(self, disciplina: Disciplina):
        '''
        actualizeaza o disciplina din repo
        :param disciplina -> Disciplina
        :return -
        '''
        try:
            self.__repo_disciplina.update_disciplina(disciplina)
        except EroareRepo as eroare:
            print("EroareRepo>>", eroare)

        print("Am actualizat cu succes disciplina")

    def afiseaza_discipline(self):
        '''
        afiseaza toate disciplinele
        :return -
        '''
        print(self.__repo_disciplina.get_all_disciplina())

    def creeare_id_disciplina(self):
        '''
        returneaza cel mai mic id nefolosit
        :return cel mai mic id nefolosit
        '''
        return self.__repo_disciplina.creare_id_disciplina()
