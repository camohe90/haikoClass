class Persona:
    def __init__(self,nombre,edad,estatura, fruta):
        self.nombre = nombre
        self.edad = edad
        self.estatura = estatura
        self.fruta = fruta
    def presentar(self):
        return [self.nombre, self.edad, self.estatura, self.fruta]
    
persona, edades, alturas, frutas  = [], [] , [], []

for i in range(2):
    print("Por favor ingrese la siguiente informacion de las persona", i+1)
    nombre= input("Digite el nombre: ")
    edad = input("Digite la edad: ")
    estatura = input("Digite la estatura: ")
    fruta = input("Digite la fruta favorita: ")
    persona.append(Persona(nombre,int(edad), float(estatura),fruta))

for i in range(len(persona)):
    print(persona[i].presentar())

for i in range (len(persona)):
    edades.append(persona[i].presentar()[1])
    alturas.append(persona[i].presentar()[2])
    frutas.append(persona[i].presentar()[3])

edades.sort()
alturas.sort()
print(edades)
print(alturas)

for i in range (len(persona)):
    if (persona[i].presentar()[1] == edades[0]):
        menor = persona[i].presentar()[0]
    if (persona[i].presentar()[1] == edades[-1]):
        mayor = persona[i].presentar()[0]
    if (persona[i].presentar()[2] == alturas[0]):
        alturaMenor = persona[i].presentar()[0]
    if (persona[i].presentar()[2] == alturas[-1]):
        alturaMayor = persona[i].presentar()[0]
    

print("La persona menor es: ", menor)
print("La persona mayor es: ", mayor)
print("La persona más baja es: ", alturaMenor)
print("La persona más alta es: ", alturaMayor)
