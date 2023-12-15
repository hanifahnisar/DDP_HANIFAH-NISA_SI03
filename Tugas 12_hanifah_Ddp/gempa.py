class Gempa:
    # atribut class
    lokasi = ''
    skala = 0
    
     # constructure
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala
        
    # method untuk menampilkan dampaknya
    def dampak(self):
        if self.skala <= 2:
            keterangan = 'dampak gempa tidak berasa'
            
        elif self.skala < 2 and self.skala > 4:
            keterangan ='dampak gempa bangunan retak-retak'
            
        elif self.skala <4 and self.skala > 6:
            keterangan ='dampak gempa bangunan roboh'
            
        else:
            keterangan ='dampak gempa bangunan roboh dan berpotensi tsunami'
                
        print(f'lokasi gempa:{self.lokasi}')
        print(f'skala gempa:{self.skala}')
        print(f'keterangan:{keterangan}')
    
    

