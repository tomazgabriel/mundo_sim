import random
import math

pop_inicial = 50
fator_crescimento = 1.0005
mortalidade_infantil = 25
idade_fertil_min = random.randint(14,18)
idade_fertil_max = random.randint(35,40)

lista_pessoas = []

chance_disastre = 10

comida = 0
agricultura = 5

educacao = 0
pesquisa = 0

#trabalhos
trabalhadores_campo = 0
professores = 0

class Pessoas:
    def __init__(self, idade):
        self.sexo = random.randint(0,1)
        self.idade = idade
        #chances da população ter mais inteligência aumentaram com a quantidade de educação
        self.educacao = educacao
        self.inteligencia = random.randint(0,10)
        self.emprego = 0
        #empregos 0 = desempregado, 1=campo, 2=educacao
        for pessoa in lista_pessoas:
            if pessoa.inteligencia >= 8:
                self.emprego = 2
            elif pessoa.inteligencia >= 1:
                self.emprego = 1
            else:
                self.emprego = 0

def agricultura_planeta(comida, agricultura, trabalhadores_campo):
    trabalhadores_campo = 0
    for pessoa in lista_pessoas:
        if pessoa.idade > 18:
            if pessoa.emprego == 1:
                trabalhadores_campo += 1
    comida += trabalhadores_campo*agricultura #ajustar agricultura para nível tecnológico posteriormente
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
                    if random.randint(1,5) == 1: # 1 em cada 5 engravidará
                        lista_pessoas.append(Pessoas(0))

def educacao_planeta(professores, educacao, pesquisa):
    for pessoa in lista_pessoas:
        if pessoa.idade > 25:
            if pessoa.emprego == 2:
                professores += 1
    educacao += professores
    pesquisa += math.ceil(educacao*2) #substituir o 2 por cientistas
    #immpedir divisão por 0
    if pesquisa <= 0:
        pesquisa += 1
    if educacao <= 0:
        educacao += 1
    return professores, educacao, pesquisa

def sim():
    for x in range(pop_inicial):
        lista_pessoas.append(Pessoas(random.randint(18,50)))

def ano_corrente(comida, agricultura, idade_fertil_min, idade_fertil_max, trabalhadores_campo, professores, educacao, pesquisa):
    agricultura_planeta(comida, agricultura, trabalhadores_campo)
    reproducao(idade_fertil_min,idade_fertil_max)
    educacao_planeta(professores, educacao, pesquisa)

    for pessoa in lista_pessoas:
        if pessoa.idade > 80:
            lista_pessoas.remove(pessoa)
        else:
            pessoa.idade += 1
    

sim()

while len(lista_pessoas) < 100 and len(lista_pessoas) > 1:
    ano_corrente(comida, agricultura, idade_fertil_min, idade_fertil_max, trabalhadores_campo, professores, educacao, pesquisa)
    print("pop: ", len(lista_pessoas), "\nComida/Trabalhadores: {}".format(agricultura_planeta(comida, agricultura,trabalhadores_campo)))
    print("professores/educação/pesquisa {}".format(educacao_planeta(professores,educacao,pesquisa)))


    