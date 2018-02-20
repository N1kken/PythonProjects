import time
print("GRA REFLEKS")
time.sleep(1)

#POWITANIE
print("Witaj, w grze refleks!:")

#GENERACJA OPOZNIENIA
czas=time.time()%8
start=2+czas

#GAMEPLAY
print("Wcisnij enter gdy bedziesz gotowy")
input()
print("Szykuj sie...")
time.sleep(czas)
print("WAL W ENTER!")
x=time.time()
input()
y=time.time()
print ("Twoj czas to {}".format(y-x))

