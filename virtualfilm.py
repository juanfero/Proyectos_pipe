#Juan Felipe Rojas 
#Proyecto cine primera parte 



print("\t!Bienvenido a cine colombia ")
cliente=str(input('digite usuario => '))
password=str(input('digite contraseña => '))


while password != 'crack':
  print('contraseña icorrecta ')
  password=str(input('digite contraseña => '))

print("contraseña correcta ")


print("\telegir pelicula")
print("\n1. Avatar ")
print("2. Avengers")
opcion=str(input('digite opcion => '))

if opcion=='1':
  price=100
  print(price)
elif opcion=='2':
  price=200
  print(price)
else:
  print('pelicula no disponible')
  exit()
  
print("\t elegir teatro ")
print("1. chile ")
print("2. gran estacion ")
print("3. hayuelos ")
print("4. titan")
print("5. colina ")
option=str(input('digite opcion => '))

if option =='1':
  price=(price*100.0)/100
  print('$', price)
elif option =='2':
  price=(price*90.0)/100
  print('$', price)
elif option =='3':
  price=(price*80.0)/100
  print('$', price)
elif option =='4':
  price=(price*60.0)/100
  print('$', price)
elif option =='5':
  price=(price*40.0)/100
  print('$', price)
else:
  print('opcion invalida')
  exit()

print('desea comida ')
print("si o no")
opciones=str(input('digite => '))

if opciones =='si':
  price+=20
  print(price)
else:
  print(price)
  exit()
