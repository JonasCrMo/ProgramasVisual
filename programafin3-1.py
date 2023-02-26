print("bienvenido a hambburgesa grasosa, enseguida desplegaremos el menu para que escoja su hamburguesa preferida")
print("--------------------------------------------------------------------------------------------------------------------------------------------------")
class Menu:#abstraccion
    def __init__(self, combo, nombre, precio, ingredientes, acompañamiento ):
        self.nombre = nombre 
        self.__precio= precio 
        self.ingredientes = ingredientes
        self.__acompañamiento = acompañamiento
        self.combo = combo
   
    def presentar(self):
        print(f'el combo {self.combo}, es la hamburguesa {self.nombre} cuesta {self.__precio} pesos tiene {self.ingredientes} y cuenta con {self.__acompañamiento}')
    
    def getprecio(self):
        print(self.__precio)

    def getacompañamiento(self):
        print(self.__acompañamiento)

class ordenando:
    def describir(self):
        print("cuantos combos quiere ?")
        numeroorden= input()

        if numeroorden== "1":
            print("Que combo quiere ordenar, favor de escribir el numero del combo?")
            ordencli = input() 
            
            print("la hamburguesa con todo?, (si o no)")
            noquiero=input()

            if noquiero == "no":
                print("que ingredientes desea quitar")
                quitar=input()
            


            if ordencli == "1":
                print("promo de solitarios, desea añadirle mas papas y un hotdog a su horden por 30 pesos mas?, (si o no )")
                extra= input()
                

                if extra == "si":
                    print("el hotdog con todo?, (si o no)")
                    noquieroh=input()
                    if noquieroh == "si":
                        print("su total a pagar es de 75 pesos, su pedido estara listo en un momento")
                    else:
                        print("que ingredientes desea quitar ")
                        sinh=input()
                        print("su total a pagar es de 75 pesos, su pedido estara listo en un momento")


                else:
                    print("su total a pagar es de 45 pesos, su pedido estara listo en un momento")
                
            elif ordencli== "2":
                
                print("promo de solitarios, desea añadirle mas papas y un hotdog a su horden por 30 pesos mas?, (si o no )")
                extra= input()

                if extra == "si":
                    print("el hotdog con todo?, (si o no)")
                    noquieroh=input()
                    if noquieroh == "si":
                        print("su total a pagar es de 85 pesos, su pedido estara listo en un momento")
                    else:
                        print("que ingredientes desea quitar ")
                        sinh=input()
                        print("su total a pagar es de 85 pesos, su pedido estara listo en un momento")
                
                else:
                    
                    print("su total a pagar es de 55 pesos, su pedido estara listo en un momento")

            else:
                print("promo de solitarios, desea añadirle mas papas y un hotdog a su horden por 30 pesos mas?, (si o no )")
                extra= input()
                

                if extra == "si":
                    print("el hotdog con todo?, (si o no)")
                    noquieroh=input()
                    if noquieroh == "si":
                        print("su total a pagar es de 90 pesos, su pedido estara listo en un momento")
                    else:
                        print("que ingredientes desea quitar ")
                        sinh=input()
                        print("su total a pagar es de 85 pesos, su pedido estara listo en un momento")


                else:
                    print("su total a pagar es de 60 pesos, su pedido estara listo en un momento")


        else:
            print("cuantos combos 1 quiere ordenar?")
            com1= int(input())

            if com1 > 0:
                print("la o las hamburguesas con todo?, (si o no)")
                noquiero1=input()
                if noquiero1 == "no":
                    print("que ingredientes desea quitar")
                    quitar1=input()

            print("cuantos combos 2 quiere ordenar?")
            com2= int(input())
            if com2 > 0:
                print("la o las  hamburguesas con todo?, (si o no)")
                noquiero2=input()
                if noquiero2 == "no":
                    print("que ingredientes desea quitar")
                    quitar2=input()

            print("cuantos combos 3 quiere ordenar?")
            com3= int(input())
            if com3 > 0:
                print("la o las hamburguesas con todo?")
                noquiero3=input()
                if noquiero3 == "no":
                    print("que ingredientes desea quitar")
                    quitar3=input()
            
            
            res1= 45 * com1
            res2= com2*55
            res3= com3*60
            cuentaf= res1 + res2 + res3

            print("El total a pagar es", cuentaf, "su pedido estara listo en un momento")

class otras(Menu):#herencia
    def __init__(self, combo, nombre, precio, ingredientes, acompañamiento, maspapas, hotd):
        super().__init__(combo, nombre, precio, ingredientes, acompañamiento)
        self.mas = maspapas
        self.mas = hotd


class despedida:
    def describir(self):
        print("Gracias vuelva pronto")
  
#polimorfismo
class Tarjeta():
    def pago(self):
        print("introdusca la tarjeta")
        pagot = input()

class Efectivo():
    def pago(self):
        print("introdusca el efectivo")

class Cupon():
    def pago(self):
        print("introdusca el cupon")

def VoyaPagar(credito):
    credito.pago()



def definircombo(combo):
    combo.describir()



hamsencilla= Menu(1," sencilla", 45, "[pan, lechuga, jitomate, ketchup, mayonesa, mostaza, y cebolla]", "[papas y refresco]")
hamsencilla.presentar()

hamdoble= Menu(2,"doble carne", 55, "[pan, lechuga, jitomate, ketchup, mayonesa, mostaza, doble carne y cebolla]", "[papas y refresco]")
hamdoble.presentar()

hamtocino=Menu(3,"puercoburguer", 60, "[pan, lechuga, jitomate, ketchup, mayonesa, mostaza, tocino y cebolla]", "[papas y refresco]")
hamtocino.presentar()
print("--------------------------------------------------------------------------------------------------------------------------------------------------")
print("si quiere ordenar escriba si, si quiere salir escriba bye")
decicion= input()
print("--------------------------------------------------------------------------------------------------------------------------------------------------")

if decicion == "si":
    clase = ordenando()
    definircombo(clase)
elif decicion == "bye":
    clase =despedida()
    definircombo(clase)

else:
    print("favor de seleccionar si o bye")

print ("seleccione el metodo de pago, 1 para pago con tarjeta, 2 para pago con efectivo, 3 pago con cupon")
elpago=input()

if elpago == "1":
    pagot = Tarjeta()
    VoyaPagar(pagot)
elif elpago == "2":
    pagot = Efectivo()
    VoyaPagar(pagot)
else:
    pagot = Cupon()
    VoyaPagar(pagot)