



lista_prioridad=[]
prioridad_alta=[]
prioridad_media=[]
prioridad_baja=[]
def ordenar_prioridad(nivel,auto):
    if nivel==1:
        prioridad_alta.append(auto)
    if nivel==2:
        prioridad_media.append(auto)
    if nivel==3:
        prioridad_baja.append(auto)
    lista_prioridad=prioridad_alta+prioridad_media+prioridad_baja
    print (lista_prioridad)



nivel=0
alta=["ambulancia"]
media=["trailer","cargamento","mini-bus","micro"]
bajo=["uso-exclusivo","taxi"]
contador=0
while True:
    auto=input("ntrodusca que vehiculo a ingresado a la gasolineria:").lower()
    for prioridad in alta:
        if prioridad==auto:
            print("Tiene prioridad alta")
            nivel=1
    for prioridad in media:
        if prioridad==auto:
            print("Tiene una prioridad media (por debajo que emergencias y por encima de particulares)")  
            nivel=2
    for prioridad in bajo:
        if prioridad==auto:
            print("Tiene prioridad baja (por debajo de automoviles de emergencias, abastecimiento y particulares)")
            nivel=3
    print("-------------------orden de atencion-----------------")
    ordenar_prioridad(nivel,auto)
    print("------------------------------------------------------")














'''
prioridades={'emergencias':'alta','abastecimiennto':'alto','publico':'medio','particular':"bajo"}

def agregarAuto(colaGeneral):
    colaAlta=[]
    colaMedia=[]
    colaBaja=[]
    for auto in colaGeneral:
        if auto.tipo=="alta":
            colaAlta.append(auto)
        elif auto.tipo=="medio":
            colaMedia.append(auto)
        else:
            colaBaja.append(auto)
            colaGeneral=[colaAlta+colaMedia+colaBaja]
    return colaGeneral

class automovil():
    def __init__ (self,matricula,tipo):
        self.matricula=matricula
        self.tipo=tipo

auto1 = automovil("ABC123", "alta")
auto2 = automovil("XYZ789", "medio")
auto3 = automovil("LMN456", "bajo")
auto4 = automovil("DEF321", "alta")

'''
