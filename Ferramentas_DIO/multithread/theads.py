from threading import Thread
from time import sleep

def carro(vel, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto += vel
        sleep(0.5)
        print(f'Piloto: {piloto} Km:{trajeto}\n')

t_carro1 = Thread(target=carro, args=[10, 'Mei'])
t_carro2 = Thread(target=carro, args=[20, 'Python'])

t_carro1.start()
t_carro2.start()
