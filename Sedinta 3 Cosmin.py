#variabila = (1, 2, 3, 4, 5,)
#print(variabila)
#variabila.append('vara')
#print(variabila)
#print(type(variabila))
#print(variabila + (1, 2, 3, 4, 5,))

#variabila2 = (variabila + (1, 2, 3, 4, 5,))
#print(variabila2)

#variabila2 = variabila.count
#print(variabila2)

#masina = {'culoare','roti','lungime','latime'}
#print(masina)
#print(masina[2])
#print(masina.copy())


#dictionar = {'culoare':'rosu','roti':'4','marca':'BMW','specificatii':{'lungime':20, 'latime':10,'inaltime':4}}
#print(dictionar.get('specificatii').get('latime')) #
'''
dictionar = {
   "culoare":"rosu",
   "roti":"4",
   "marca":"BMW",
   "specificatii":{
      "lungime":20,
      "latime":10,
      "inaltime":4
   }
}
print(len(dictionar))
dictionar2 = {
    'putere':1250,
    'model':323,
    }
'''
#print(dictionar['roti'].replace(dictionar2))
#print(dictionar.get('roti').replace('4','6',))
#dictionar3 =dictionar.update('roti').replace('4','6')


# list = ['mere', 10, True, 2.4, 'pere', 66 ]
# list[2] = 'portocale'
# print(list)
#
# list2 =['ananas', 90, 'cirese', 2.65]
#
# list2[1] = list[3]
# print(list2)

dictionar = {
   "culoare":"rosu",
   "roti":"4",
   "marca":"BMW",
   "specificatii":{
      "lungime":20,
      "latime":10,
      "inaltime":5
   }
}

dictionar2 = {
    'putere':125,
    'model':520,
    }
if dictionar.get('specificatii').get('inaltime') == 0:
    dictionar['specificatii']['latimea'] = dictionar2['putere']
    print(dictionar)
elif len(dictionar) <= 1:
    print('am ajuns aici')