class Animal:
    def __init__(self, nama, makanan, habitat, berkembangbiak):
        self.nama = nama
        self.makanan = makanan
        self.habitat = habitat
        self.berkembangbiak = berkembangbiak 
        
    
    def cetak(self):
        print(f"hewan ini adalah {self.nama}")
        print(f"makanannya adalah {self.makanan}")
        print(f"habitatnya di {self.habitat}")
        print(f"berkembang biak dengan cara {self.berkembangbiak}")

class Badak(Animal):
    def __init__(self, nama, makanan, habitat, berkembangbiak):
        super().__init__(nama, makanan, habitat, berkembangbiak)
        print(Animal)
a =Badak("Badak", "Daging", "darat", "Melahirkan")
a.cetak()

class Ikan(Animal):
    def __init__(self, nama, makanan, habitat, berkembangbiak):
        super().__init__(nama, makanan, habitat, berkembangbiak)
        print(Animal)
b =Ikan("Ikan", "Cacing", "Air", "Bertelur")
b.cetak()
        
class Ular(Animal):
    def __init__(self, nama, makanan, habitat, berkembangbiak):
        super().__init__(nama, makanan, habitat, berkembangbiak)
        print(Animal)
c =Ular("Ular", "Daging", "Darat", "Bertelur")
c.cetak()
        

        
        
        
    

