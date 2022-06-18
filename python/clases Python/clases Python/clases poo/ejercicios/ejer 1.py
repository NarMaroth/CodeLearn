class Pizzeras():
    codigo=1
    alto=2
    diametro=30
    material="Acero"

class Vasos():
    codigo=1
    alto=10
    diametro=5
    material="Vidrio"

    def calcular_Vol(self):
        self.vol= (3.14*(self.diametro/2)**2) * self.alto
        print("El volumen es", self.vol)

class Ollas():
    codigo=1
    alto=20
    diametro=40
    material="Acero"

    def calcular_Vol(self):
        self.vol= (3.14*(self.diametro/2)**2) * self.alto
        print("El volumen es", self.vol)

pizzera_1= Pizzeras()
pizzera_2= Pizzeras()
pizzera_3= Pizzeras()
pizzera_4= Pizzeras()
pizzera_5=  Pizzeras()
pizzera_2.codigo= 2
pizzera_3.codigo= 3
pizzera_4.codigo= 4
pizzera_5.codigo= 5 

vaso_1= Vasos()
vaso_2= Vasos()
vaso_3= Vasos()
vaso_4 = Vasos()
vaso_5 = Vasos()
vaso_2.codigo = 2
vaso_3.codigo = 3
vaso_4.codigo = 4
vaso_5.codigo = 5
vaso_2.alto= 15
vaso_3.alto = 15
vaso_3.diametro = 4.5
vaso_4.diametro = 4.5
vaso_4.material = "Plastico"


olla_1 = Ollas()
olla_2 = Ollas()
olla_3 = Ollas()
olla_4 = Ollas()
olla_5 = Ollas()
olla_2.codigo = 2
olla_3.codigo = 3
olla_4.codigo = 4
olla_5.codigo = 5
olla_2.alto = 5
olla_3.alto = 15
olla_4.alto = 10
olla_5.alto = 25
olla_2.diametro = 15
olla_3.diametro = 20
olla_4.diametro = 25
olla_5.diametro = 35
olla_2.material = "Aluminio"
olla_3.material = "Barro"
olla_4.material = "Cobre"
olla_5.material = "Ceramica"