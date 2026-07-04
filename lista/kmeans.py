from random import randint


values = [
    (1,1),
    (1,3),
    (1,5),
    (2,4),
    (3,2),
    (3,5),
    (9,8),
    (10,9),
    (10,11), 
    (11,8),
    (11,9),
    (11,12), 
    (20,0),
    (7,6),
    (50,68),
]


K = 2 
epocas = 5

#cria um quadrado 50x50
limx_init  = limy_init = 0
limx_final = limy_final = 50

def create_random_center():
    global  limx_init, limx_final, limy_init, limy_final
    return (randint(limx_init, limy_final), randint(limx_init, limy_final))

def mean_squared_error(p1, p2): 
    return ((p1[0]-p2[0])**2 +  ((p1[0]-p2[0]))**2)**0.5

#(0, 2) (0, 4)
#distancia = 0-0


centro_inicial = [create_random_center() for _ in range (2)]
print(centro_inicial)
print(mean_squared_error(centro_inicial[0], centro_inicial[1]))
for epoca in range(epocas): 
    for value in values: 
        