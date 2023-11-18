import math
num = float(input('Digite o angulo: '))
print(f'''O angulo de {num} tem o SENO de {math.sin(math.radians(num)):.2f}
COSSENO de {math.cos(math.radians(num)):.2f}
e a TANGENTE DE {math.tan(math.radians(num)):.2f}''')
#usa o math.radians para converter em radiando