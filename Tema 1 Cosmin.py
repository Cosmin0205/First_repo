# 1.variabila este o zona din memorie care retine date

# 2.declarare si initializare variabile
fructe = 'mere'
luna = 10
zecimala = 3.5
raspuns = True
# se printeaza toate variabilele cu virgula intre ele
print(fructe, ',', luna, ',', zecimala, ',', raspuns, ',')
# 3.se afiseaza tipul variabilei
print(type(fructe))
print(type(luna))
print(type(zecimala))
print(type(raspuns))

# 4.suprascriere zecimala
zecimala = round(zecimala)
print(zecimala)
print(type(zecimala))

# 5.printare propozitii cu variabile
print('Ana are ', fructe)
print('Octombrie este luna a', luna)
print('Nota lui Ion este', zecimala)
print('Raspunsul calculatorului a fost', raspuns)

# 6.afisare nume si prenume
nume = (input('Numele este='))
prenume = (input('Prenumele este='))
print('Numele complet are', len(nume + prenume), 'caractere')

# 7.aflare arie dreptunghi
lungime = int(input('lungimea='))
latime = int(input('latime='))
print('aria dreptungiului este', lungime * latime)

# 8.de cate ori apare 'the'
propozitie = 'Coral is either the stupidest animal or the smartest rock'
print(propozitie.count('the'))

# 9.inlocuieste 'the' cu 'THE'
propozitie = 'Coral is either the stupidest animal or the smartest rock'
print(propozitie.replace('the', 'THE'))

# 10.daca stringul contine doar numere
propozitie = 'Coral is either the stupidest animal or the smartest rock'
assert propozitie == str(propozitie)
print('contine lit')
assert propozitie == int(propozitie)
print('contine cif')
# -----------------------------------------------------------------------------------------------------
# OPTIONALE SEDINTA 1

# ex 1 mijloc cuvant impar
cuvant = str(input('Scrie un cuvant impar='))
print(len(cuvant))
y = round(len(cuvant) // 2)
print(y)
print(cuvant[y])

# ex 2 string este palindrom
pal = str(input('Scrie un cuvant:'))
assert pal == pal[::-1]
print('este palindrom')

# #ex 3 3. Folosind o singură linie de cod :
# - citește un string de la tastatură (ex: 'alabala portocala');
# - salvează fiecare cuvânt într-o variabilă;
# - printează ambele variabile pentru verificare.

x, y = (str(input('Introduceti o propozitie din 2 cuvinte: '))).split()
print(f' x = {x} \n y = {y}')

# #ex 4. Exercițiu:
# - citește un string de la tastatură (ex: alabala portocala);
# - salvează primul caracter într-o variabilă - indiferent care este el, încearcă
# cu 2 stringuri diferite;
# - capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul
# caracter => alAbAlA portocAla.

prop = str(input('Inserati o propozitie: '))
first = prop[0]
x = prop[1:(len(prop) - 1)]
print(first, x.replace(first, first.upper()), prop[(len(prop) - 1)])

# ex 5
# 5.Exercițiu:
# - citește un user de la tastatură;
# - citește o parolă;
# - afișează: 'Parola pt user x este ***** și are x caractere';
# - ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să
# afișeze corect.
# eg: parola abc => ***
# parola abcd => ****

user = input('User=')
parola = input('Parola=')
nr = len(parola)
print('Parola pt userul ' + user + ' este ' + parola.replace(parola, '*') * len(parola) + ' si are ' + str(
    nr) + ' caractere')
