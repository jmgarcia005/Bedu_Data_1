nombre = input('¿Cual es tu nombre?\n') #Solicitar el nombre al usuario

peso = input(f'{nombre}, ¿cual es tu peso? (En Kilogramos)\n') #Solicitar el peso al usuario
peso = float(peso)

altura = input(f'{nombre}, una cosa mas, ¿cual es tu altura? (En Metros)\n') #Solicitar altura al usuario
altura =float(altura)

IMC = peso / (altura*altura)

if IMC >= 40:
    Grado_obesidad = 'Obesidad muy severa (Obesidad Morbida).'
elif IMC >= 35:
    Grado_obesidad = 'Obesidad Severa.'
elif IMC >= 30 :
    Grado_obesidad = 'Obesidad Moderada.'
elif IMC >= 25 :
    Grado_obesidad = 'Sobrepeso.'
elif IMC >= 18.5 :
    Grado_obesidad = 'Peso Saludable.'
elif IMC >= 16 :
    Grado_obesidad = 'Delgadez.'
elif IMC >= 15.5 :
    Grado_obesidad = 'Delgadez Severa.'


Resultado = f'{nombre} tu IMC es {IMC:.2f}, quiere decir que tienes {Grado_obesidad}'

print(Resultado)