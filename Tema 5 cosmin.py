# 1.Funcție care să calculeze și să returneze suma a două numere

x, y = float(input('Numar 1:')), float(input('Numar 2:'))


def suma(a, b):
    z = a + b  # calcul suma
    return z


print(suma(x, y))

# 2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar
x = int(input('Introdu un numar:'))


def par_impar(a):
    if a % 2 == 0 and a > 0:  # conditie obligatorie
        return 'TRUE'
    else:
        return 'FALSE'


print(par_impar(x))

# 3. Funcție care returnează numărul total de caractere din numele tău complet.
# (nume, prenume, nume_mijlociu)

nume = input('Nume=')
prenume = input('Prenume=')
nume_mijlociu = input('Nume_mijlociu=')


def caractere(x, y, z):
    numar = len(x) + len(y) + len(z)  # calcul nr caractere totale
    return numar


print('Numarul total de caractere este ', caractere(nume, prenume, nume_mijlociu))

# 4. Funcție care returnează aria dreptunghiului

lungime = float(input('Lungimea:'))
latime = float(input('Latimea:'))


def aria(x, y):
    if x > 0 and y > 0:  # conditii obligatorii
        rezultat = x * y  # formula de calcul
        return rezultat
    else:
        print('Introdu date valide')


print(aria(lungime, latime))

# 5. Funcție care returnează aria cercului

pi = 3.14
raza = float(input('Introdu raza cercului:'))


def arie_cerc(x):
    if x > 0:
        rezultat = pi * (x ** 2)  # ridicare la puterea 2:  **2
        return rezultat
    else:
        print('Introdu date valide')


print(arie_cerc(raza))

# 6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
# și Talse dacă nu găsește.

string = input('String:')
cr = input('Introdu un caracter:')


def caracter(i, car):
    for i in string:
        if i == car:  # se verifica daca caracterul cerut se regaseste in string
            print('True')
            return i
    else:
        print('False')


caracter(string, cr)


# 7. Funcție fără return, primește un string și printează pe ecran:
# ● Nr de caractere lower case este x
# ● Nr de caractere upper case exte y

def lower_upper(string):
    char_upper = 0
    char_lower = 0
    for char in string:
        if char.isupper():
            char_upper = char_upper + 1
        elif char.islower():
            char_lower = char_lower + 1
    print(f'Numarul de caractere mari este: {char_upper}')
    print(f'Numarul de caractere mici este: {char_lower}')


lower_upper('abc1ABCD!')

# 8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu
# numerele pozitive
list1 = []
list2 = []


def fct(l1, l2):
    n = int(input('Cate numere doresti in lista?'))
    for i in range(0, n):
        element = int(input())
        l1.append(element)  # formare lista initiala (citire de la tastatura si adaugare)
    print('Lista initiala este:', l1)
    for j in l1:
        if j > 0:  # verificare daca nr e pozitiv si apoi adaugare in lista de nr pozitive
            l2.append(j)
            j += 1
    return l2


print('Numerele pozitive:', fct(list1, list2))

# 9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
# ● Primul număr x este mai mare decat al doilea nr y
# ● Al doilea nr y este mai mare decat primul nr x
# ● Numerele sunt egale.

x, y = int(input('Scrie primul nr:')), int(input('Scrie al doilea nr:'))


def mare(a, b):
    if a > b:
        print(f'Primul numar({a}) este mai mare ca al doilea({b}).')
    elif b > a:
        print(f'Al doilea numar({b}) este mai mare decat primul({a}).')
    else:  # daca numerele sunt egale
        print(f'Numerele introduse sunt egale')


mare(x, y)

# 10. Funcție care primește un număr și un set de numere.
# ● Printeaza ‘am adaugat numărul nou în set’ + returnează True
# ● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
# returnează False

numere = set({})  # setul initial
a = int(input('Cate numere doriti in set?(numere unice)'))  # nr de pozitii ale setului

for i in range(0, a):  # se citeste de la tastatura setul numar cu numar (valori unice)
    element = int(input('Introdu numar:'))
    numere.add(element)  # se adauga fiecare nr in set
print(f'Setul este:{numere}')

x = int(input('Scrie un nr:'))  # numarul verificat


def functie(j, nr):
    if j in nr:  # se verifica daca j este in set deja
        print('Nu am adaugat numarul in set.Acesta exista deja')
        return 'False'
    else:
        numere.add(j)  # se adauga j in set
        print(f'Am adaugat numarul nou in setul de numere {nr}.')
        return 'True'


print(functie(x, numere))
#______________________________________________________________________________________________________________
#################################OPTIONAL######################################


# 1. Funcție care primește o lună din an și returnează câte zile are acea luna


l31 = ['ianuarie', 'martie', 'mai', 'iulie', 'august', 'octombrie', 'decembrie']
l30 = ['aprilie', 'iunie', 'septembrie', 'noiembrie']
l28_29 = ['februarie']


def an(luna):
    if luna in l31:
        print(f'Luna {luna} are 31 de zile')
    elif luna in l30:
        print(f'Luna {luna} are 30 de zile')
    elif luna in l28_29:
        print(f'Luna {luna} are 28 sau 29 de zile')
    else:
        print('Introdu o luna valida!')


an(input('Scrie te rog o luna din an:'))


# 2. Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea,
# împărțirea a două numere.
# În final vei putea face:
# a, b, c, d = calculator(10, 2)
# ● print("Suma: ", a)
# ● print("Diferenta: ", b)
# ● print("Inmultirea: ", c)
# ● print("Impartirea: ", d)

def calculator(a, b):
    print(f'Suma:{a + b}')
    print(f'Diferenta:{a - b}')
    print(f'Inmultirea:{a * b}')
    print(f'Impartirea:{a / b}')


calculator(int(input('Introdu primul numar:')), int(input('Introdu al doilea numar:')))


# 3. Funcție care primește o lista de cifre (adică doar 0-9)
# Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returnează un DICT care ne spune de câte ori apare fiecare cifră
# => dict {
# 0: 0
# 1 :2
# 2: 0
# 3: 1
# 4: 0
# 5: 3
# 6: 0
# 7: 2
# 8: 0
# 9: 1
# }

def lista(cifre):
    dictionar = {}
    for i in range(len(cifre) + 1):
        dictionar[i] = str(cifre.count(i))
    return dictionar


numere = lista([1, 3, 1, 5, 9, 7, 7, 5, 5])
print(numere)


# 4. Funcție care primește 3 numere. Returnează valoarea maximă dintre ele
def maxim(a, b, c):
    print(max(a, b, c))


maxim(int(input('Adauga primul numar: ')), int(input('Adauga al doilea numar: ')),
      int(input('Adauga al treilea numar: ')))
maxim(5, 8, 1)


# 5. Funcție care să primească un număr și să returneze suma tuturor numerelor
# de la 0 la acel număr
# Exemplu: daca dam nr 3. Suma va fi 6 (0+1+2+3)

def nr(a):
    print(sum(range(0, a + 1)))


nr(int(input('Alege un numar: ')))
