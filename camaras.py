print("Bienvenido al sistema de multas por exceso de velocidad por favor ingre los siguiente datos")
for i in range(100):
    print("*", end="")
print()

def recibirData():
    global distancia, velocidad, tiempo

    while True:
        try: 
            distancia = float (input("Digite la distancia en metros que separa las dos camaras: "))
            velocidad = float (input("Digite la velocidad máxima permitida en ese tramo en (Km/h): "))
            tiempo = float (input("Digite el tiempo en segundos que tarda el conductor en recorrer el trayecto: "))
        
        except ValueError:
            print("Por favor verifique que todos los datos ingresados sean de tipo númerico")
            continue
        else: 
            print("****************Información ingresada correctamente*********************")
            break

recibirData()

velocidadMetros = (velocidad*1000)/3600
velocidadMulta = velocidadMetros*1.20

if (distancia>0 and tiempo > 0 and velocidad>0) :
    velocidadRecorrido = distancia/tiempo
    error = False
else:
    error = True
    print("ERROR")
    velocidadRecorrido=0


if (velocidadRecorrido <= velocidadMetros and not error  ):
    print("OK")

if (velocidadRecorrido <= velocidadMulta and velocidadRecorrido > velocidadMetros and not error  ):
    print("MULTA")

if (velocidadRecorrido > velocidadMulta and not error ):
    print ("SENSIBILIZACION")
