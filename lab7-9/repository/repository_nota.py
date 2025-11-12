from domeniu.note import Note
from domeniu.student import Student
from domeniu.disciplina import Disciplina
from exceptii.EroareRepo import EroareRepo


class RepoNote:
    def __init__(self):
        self.__repo_note = {}

    def verificare_id_exista(self, id_nota):
        if id_nota in self.__note.keys():
            raise EroareRepo("id exista deja!\n")

    def adauga_nota(self, nota: Note):
        '''
        adauga o nota nou in repo
        :parem nota -> nota
        :return -
        '''

        id_nota = (nota.get_id_student(), nota.get_id_disciplina())

        try:
            self.verificare_id_exista(id_nota)
        except EroareRepo as e:
            print("eroareRepo >>", e)
            return

        self.__repo_note[id_nota] = nota

    def sterge_nota(self, nota: Note):
        '''
        sterge o nota din repo
        :parem nota -> nota
        :return -
        '''

        id_nota = (nota.get_id_student(), nota.get_id_disciplina())

        try:
            self.verificare_id_exista(id_nota)
        except EroareRepo as e:
            print("eroareRepo >>", e)
            return

            del self.__note[id_nota]

    def update_nota(self, nota: Note):
        '''
        actualizeaza o nota din repo
        :parem nota -> nota
        :return -
        '''

        id_nota = (nota.get_id_student(), nota.get_id_disciplina())

        try:
            self.verificare_id_exista(id_nota)
        except EroareRepo as e:
            print(" eroareRepo >>", e)
            return

        self.__repo_note[id_nota] = nota

    def get_all(self):
        '''
        returneaza lista de note
        :return lista de note
        '''
        return list(self.__repo_note.values())
