import random

try:

    numero = int(input(" numero qual dessa vez"))

    acao = ["bom", "ruim", "medio", numero]

    letrasnum = [random.sample([random.randint(1, 4), random.sample(acao)]) for __ in range(4)]
    
    random.shuffle(letrasnum)

    print(letrasnum)

    if isinstance(letrasnum, int) and isinstance(letrasnum, str):

        raise ValueError("invalido deu errado")

except Exception as e:

    print(f"outro jeito {e}", e)

