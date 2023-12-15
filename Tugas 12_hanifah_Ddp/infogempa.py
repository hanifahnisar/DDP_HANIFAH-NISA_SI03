from gempa import *

cianjur = Gempa('cianjur',2.6)
melonguane = Gempa('melonguane',4.9)
aceh = Gempa('aceh',3.2)

cianjur.dampak()
melonguane.dampak()
aceh.dampak()