# numar=3
#
# try:
#
#     assert numar %2==0,'pacat'
#
# except AssertionError as e:
#     print(e)

#from abc import abstractmethod


# ______________________________________________
# def masina():
#     try:
#         numar_roti=int(input('introdu nr de roti'))
#     except ValueError:
#         print('nu e nr')
#     culoare=None
#     try:
#
#         return numar_roti
#     except UnboundLocalError:
#         print('nr de roti e gol')
# masina()
# -------------------------------------------------------------------------------
# class om():
#     def __init__(self,inaltime,greutate,culoare_ochi):
#         self.inaltime = inaltime
#         self.greutate = greutate
#         self.culoare_ochi = culoare_ochi
#     __tip_vestimentatie = 'elegant'  #vizibil doar in clasa om (incapsulare)
# ion = om(180,80,'caprui')
#
# class elev(om):
#     def __init__(self, inaltime, greutate, culoare_ochi,clasa):
#         super().__init__(inaltime, greutate, culoare_ochi)
#         self.clasa  =clasa
#     def invata(self):
#         print('eu invat it')
#
#
# class elev_absolvent(elev):
#     def __init__(self, inaltime, greutate, culoare_ochi,clasa):
#         super().__init__(inaltime, greutate, culoare_ochi,clasa)
#     def invata(self):
#         print('eu invat it avansat')
# elev1 = elev(120,60,'verde',12)
# elev2 = elev_absolvent(130,50,'verde',12)
# elev1.invata()
# elev2.invata()


# ____________________________________________________________________________________
# class figura_geo():
#     @abstractmethod
#     def defineste_forma(self):
#         raise NotImplementedError
#
#     @abstractmethod
#     def stabileste_perimetrul(self):
#         raise NotImplementedError
#
#
# class patrat(figura_geo):
#     def defineste_forma(self):
#         numar_laturi = input('introdu nr laturilor')
#
# patrat1  =patrat()
# patrat1.defineste_forma()
# patrat2 = figura_geometrica() # eroare deoarece face apel la clasa abstracta care nu este definita
# patrat2.defineste_forma()
# patrat2.stabileste_perimetrul()

# class Angajat:
#     nume = None
#     prenume = None
#     salariu = None
#
#     def __init__(self, a,b,c):
#         self.nume = a
#         self.prenume = b
#         self.salariu = c
#
#     def descrie(self):
#         print(f'Numele angajatului este: {self.nume} ')
#         print(f'Prenumele angajatului este: {self.prenume}')
#         print(f'Are salariul {self.salariu}')
#
#     def nume_complet(self):
#         print(self.nume +' ' + self.prenume)
#
#     def salariu_lunar(self):
#         print(f'salariul lunar este de
