class Masina:
    culoare = None
    roti = None
    tractiune = None
    forma = None

    def putere(self):
        if self.tractiune == 4:
            print('puterea creste cu 50 cp')

object = Masina()
object.tractiune = 4
object.putere()

class Floare:
    petale = 4
    culoare = 'Rosie'
    inaltime = 5

    def __init__(self, a, b):  # definire constructor
        self.culoare = a
        self.inaltime = b

    def verifica_floarea(self):
        if self.culoare == 'Rosie':
            print('Floarea este trandafir')
        elif self.culoare == 'Galben':
            print('Floarea este galbena')

    def verifica_inaltimea(self):
        if not self.inaltime == 0:
            print('Floarea este vie')
        else:
            print('Floarea este moarta')