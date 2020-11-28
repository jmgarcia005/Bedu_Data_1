'''
----------------------------------------------
id - nombre - a_paterno - a_materno - edad
----------------------------------------------
190 - galileo - guzman - ibañez - 31
----------------------------------------------
a132 - edmundo - ochoa - varguez - 33
----------------------------------------------
45 - dalai - aguirre - jimenez - 26
----------------------------------------------
89 - dilan - ortiz - granados - 25
'''
galileo = {
    'nombre': 'galileo',
    'a_paterno': 'guzman',
    'a_materno': 'ibañez',
    'edad': '31',
}
edmundo = {
    'nombre': 'edmundo',
    'a_paterno': 'ochoa',
    'a_materno': 'varguez',
    'edad': '33',
}
dalai = {
    'nombre': 'dalai',
    'a_paterno': 'aguirre',
    'a_materno': 'jimenez',
    'edad': '26',
}
dilan = {
    'nombre': 'dilan',
    'a_paterno': 'ortiz',
    'a_materno': 'granados',
}
print(type(dilan))
# print(dilan)
# print(dilan['edad'])
print(dilan.get('edad', '100'))
print('fin')