from datetime import time, datetime
from datetime import timedelta
from time import sleep
import winsound
print('Entrez votre miniteur')

heure = int(input('H:'))
minute = int(input('MIN:'))
seconde = int(input('S:'))

temps = time(heure, minute, seconde)

maintenant = datetime.now()
duree = timedelta(hours= heure, minutes= minute, seconds= seconde)
futur = maintenant + duree


print('Début du minuteur',maintenant)

sleep(duree.total_seconds())
winsound.PlaySound("SystemHand", winsound.SND_LOOP)
print(futur)
