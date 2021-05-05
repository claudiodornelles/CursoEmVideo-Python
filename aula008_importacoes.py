import math
import random
import emoji


num = random.randint(1, 100)
raiz = math.sqrt(num)

print(num)
print(f'A raiz quadrada de {num} é igual a {raiz}.')

print(emoji.emojize("Olá, mundo :sunglasses:", use_aliases=True))