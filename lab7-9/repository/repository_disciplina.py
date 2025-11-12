from domeniu.disciplina import Disciplina
from exceptii.EroareRepo import EroareRepo


class RepoDisciplina:
    def __init__(self):
        self.__disciplina = {}

    def adaugare_disciplina(self, disciplina: Disciplina):
        '''
        functie care adauga o disciplina noua
        :parem disciplina -> disciplina
        :return -
        '''
        id_disciplina = disciplina.get_id_disciplina()

        if id_disciplina in self.__disciplina:
            raise EroareRepo("Id exista deja!\n")

        self.__disciplina[id_disciplina] = disciplina
        print(f"Am adaugat disciplina cu succes cu id {id_disciplina}")

    def stergere_disciplina(self, disciplina: Disciplina):
        '''
        functie care sterge disciplina din repo
        :parem disciplina -> disciplina
        :return -
        '''
        id_disciplina = disciplina.get_id_disciplina()

        if id_disciplina not in self.__disciplina:
            raise EroareRepo("Id nu exista!\n")

        del self.__disciplina[id_disciplina]

    def update_disciplina(self, disciplina: Disciplina):
        '''
        actualizeaza o disciplina deja inserata
        :parem disciplina -> disciplina
        :return -
        '''

        id_disciplina = disciplina.get_id_disciplina()

        if id_disciplina not in self.__disciplina:
            raise EroareRepo("Id nu exista!\n")

    def get_all_disciplina(self):
        return list(self.__disciplina.values())

    def creare_id_disciplina(self):
        id_existente = list(self.__disciplina.keys())
        if len(id_existente) == 0:
            return 1
        id_existente.sort()
        id_prev = id_existente[0]
        for id in id_existente:
            if (id-id_prev > 1):
                return id_prev+1

        return len(id_existente)+1
