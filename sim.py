import random

pop_inicial = 50
fator_crescimento = 1.0005
mortalidade_infantil = 25
idade_fertil_min = random.randint(14,18)
idade_fertil_max = random.randint(35,40)

lista_pessoas = []

chance_disastre = 10

comida = 0
agricultura = 5

#trabalhos
trabalhadores_campo = 0

class Pessoas:
    def __init__(self, idade):
        self.sexo = random.randint(0,1)
        self.idade = idade

def agricultura_planeta(comida, agricultura, trabalhadores_campo):
    trabalhadores_campo = 0
    for pessoa in lista_pessoas:
        if pessoa.idade > 18:
            trabalhadores_campo += 1
    comida += trabalhadores_campo*agricultura
    if comida < len(lista_pessoas):
        del lista_pessoas[0:int(len(lista_pessoas)-comida)]
        comida = 0
    else:
        comida -= len(lista_pessoas)
    return comida, trabalhadores_campo

def reproducao(idade_fertil_min, idade_fertil_max):
    for pessoa in lista_pessoas:
        if pessoa.sexo == 1:
            if pessoa.idade > idade_fertil_min:
                if pessoa.idade < idade_fertil_max:
                    if random.randint(1,5) == 1:
                        lista_pessoas.append(Pessoas(0))

def sim():
    for x in range(pop_inicial):
        lista_pessoas.append(Pessoas(random.randint(18,50)))

def ano_corrente(comida, agricultura, idade_fertil_min, idade_fertil_max, trabalhadores_campo):
    agricultura_planeta(comida, agricultura, trabalhadores_campo)
    reproducao(idade_fertil_min,idade_fertil_max)

    for pessoa in lista_pessoas:
        if pessoa.idade > 80:
            lista_pessoas.remove(pessoa)
        else:
            pessoa.idade += 1
    

sim()

while len(lista_pessoas) < 10000 and len(lista_pessoas) > 1:
    ano_corrente(comida, agricultura, idade_fertil_min, idade_fertil_max, trabalhadores_campo)
    print("pop: ", len(lista_pessoas), "\nComida/Trabalhadores: {}".format(agricultura_planeta(comida, agricultura,trabalhadores_campo)))
    