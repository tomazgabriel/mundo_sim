import random
import math

pop_inicial = 50

idade_fertil_min = random.randint(14,18)
idade_fertil_max = random.randint(35,40)

lista_pessoas = []


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
        self.educacao = educacao

        def intel(self):
            #chances da população ter mais inteligência aumentaram com a quantidade de educação
            if educacao >= 0 and educacao <= 10:
                int = [0,1,2,3,4,5,6,7,8,9,10]
                peso =[10,9,8,7,6,5,4,3,2,1,1]
                rand_intel = (random.choices(int, weights=peso, k=1))
                self.inteligencia = rand_intel[0]
            elif educacao >= 11 and educacao <= 20:
                int = [0,1,2,3,4,5,6,7,8,9,10]
                peso =[9,8,7,6,5,4,3,3,2,2,1]
                rand_intel = (random.choices(int, weights=peso, k=1))
                self.inteligencia = rand_intel[0]
            elif educacao >= 21 and educacao <= 70:
                int = [0,1,2,3,4,5,6,7,8,9,10]
                peso =[7,6,5,5,4,4,3,3,3,2,2]
                rand_intel = (random.choices(int, weights=peso, k=1))
                self.inteligencia = rand_intel[0]
            elif educacao >= 71 and educacao <= 80:
                int = [0,1,2,3,4,5,6,7,8,9,10]
                peso =[4,4,4,4,5,5,5,5,3,3,3]
                rand_intel = (random.choices(int, weights=peso, k=1))
                self.inteligencia = rand_intel[0]
            elif educacao >= 81:
                int = [0,1,2,3,4,5,6,7,8,9,10]
                peso =[1,1,1,1,1,2,2,2,3,3,3]
                rand_intel = (random.choices(int, weights=peso, k=1))
                self.inteligencia = rand_intel[0]
            elif educacao >= 100:
                int = [0,1,2,3,4,5,6,7,8,9,10]
                peso =[1,1,1,2,2,3,3,3,4,4,4]
                rand_intel = (random.choices(int, weights=peso, k=1))
                self.inteligencia = rand_intel[0]
                
        def empregos(self):
            #empregos 0 = desempregado, 1=campo, 2=educacao
            for pessoa in lista_pessoas:
                if pessoa.inteligencia >= 0 and pessoa.inteligencia <= 5:
                    self.emprego = 1
                elif pessoa.inteligencia >=8:
                    self.emprego = 2


        self.emprego = 0
        self.inteligencia = 0

        empregos(self)
        intel(self)


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
    educacao += int(professores *1.50)
    pesquisa += int(educacao*2) #substituir o 2 por cientistas
    #immpedir divisão por 0
    if pesquisa <= 0:
        pesquisa += 1
    if educacao <= 0:
        educacao += 1
    return professores, educacao, pesquisa

def techs(pesquisa, agricultura): #corrigir obtenção de pontos de pesquisa
    limite_tech = pesquisa
    for t in range(agricultura, limite_tech):
        agricultura += t
    return agricultura

def sim():
    for x in range(pop_inicial):
        lista_pessoas.append(Pessoas(random.randint(18,50)))

def ano_corrente(comida, agricultura, idade_fertil_min, idade_fertil_max, trabalhadores_campo, professores, educacao, pesquisa):
    agricultura_planeta(comida, agricultura, trabalhadores_campo)
    reproducao(idade_fertil_min,idade_fertil_max)
    educacao_planeta(professores, educacao, pesquisa)
    techs(pesquisa, agricultura)
    for pessoa in lista_pessoas:
        if pessoa.idade > 80:
            lista_pessoas.remove(pessoa)
        else:
            pessoa.idade += 1
    

sim()

while len(lista_pessoas) < 1000 and len(lista_pessoas) > 1:
    ano_corrente(comida, agricultura, idade_fertil_min, idade_fertil_max, trabalhadores_campo, professores, educacao, pesquisa)

    print("pop: ", len(lista_pessoas), "\nComida/Trabalhadores {}".format(agricultura_planeta(comida, agricultura,trabalhadores_campo)))
    print("professores/educação/pesquisa {}".format(educacao_planeta(professores,educacao,pesquisa)))
    print("Tech:\nagricultura: {}".format(techs(pesquisa,agricultura)))


    