from domeniu.student import Student
from repository.repositoryStudent import RepoStudent
from exceptii.EroareRepo import EroareRepo
# from validare.validare_student import EroareValidare


class ServiceStudenti:
    def __init__(self, repo_student: RepoStudent):
        self.__repo_student = repo_student

    def adauga_student(self, student: Student):
        '''
        adauga un student in repo
        :parem student -> Student
        :return -
        '''
        try:
            self.__repo_student.adaugare_student_repo(student)
        except EroareRepo as eroare:
            print("EroareRepo>>", eroare)

    def afiseaza_studentii(self):
        '''
        returneaza lista de studenti
        :return lista de studenti
        '''
        return (self.__repo_student.get_all_studenti())

    def stergere_student(self, student: Student):
        '''
        sterge un student din repo
        ;parem student -> Student
        :return -
        '''
        try:
            self.__repo_student.stergere_student(student)
        except EroareRepo as eroare:
            print("EroareRepo>>", eroare)

    def update_student(self, student: Student):
        '''
        actualizeaza un student din repo
        :parem studen -> Student
        :return -
        '''
        try:
            self.__repo_student.update_student(student)
        except EroareRepo as eroare:
            print("EroareRepo>>", eroare)
        print("Am actualizat cu succes")

    def creare_id_student(self):
        '''
        returneaza cel mai mic id nefolosit
        return cel mai mic id nefolosit
        '''
        return self.__repo_student.creare_id_student()
