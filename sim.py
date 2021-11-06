import random
import math

pop_inicial = 50

ano = 0

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
            if educacao >= 0 and educacao <= 30:
                int = [0,1,2,3,4,5,6,7,8,9,10]
                peso =[10,9,8,7,6,3,2,1,0,0,1]
                rand_intel = (random.choices(int, weights=peso, k=1))
                self.inteligencia = rand_intel[0]
            elif educacao >= 31 and educacao <= 40:
                int = [0,1,2,3,4,5,6,7,8,9,10]
                peso =[9,8,7,6,5,4,3,1,0,0,1]
                rand_intel = (random.choices(int, weights=peso, k=1))
                self.inteligencia = rand_intel[0]
            elif educacao >= 41 and educacao <= 90:
                int = [0,1,2,3,4,5,6,7,8,9,10]
                peso =[7,6,5,5,4,4,2,2,2,1,1]
                rand_intel = (random.choices(int, weights=peso, k=1))
                self.inteligencia = rand_intel[0]
            elif educacao >= 91 and educacao <= 100:
                int = [0,1,2,3,4,5,6,7,8,9,10]
                peso =[4,4,4,4,5,5,5,5,3,3,2]
                rand_intel = (random.choices(int, weights=peso, k=1))
                self.inteligencia = rand_intel[0]
            elif educacao >= 101:
                int = [0,1,2,3,4,5,6,7,8,9,10]
                peso =[1,1,1,1,1,2,2,2,3,3,3]
                rand_intel = (random.choices(int, weights=peso, k=1))
                self.inteligencia = rand_intel[0]
            elif educacao >= 300:
                int = [0,1,2,3,4,5,6,7,8,9,10]
                peso =[1,1,1,2,2,3,3,3,4,4,4]
                rand_intel = (random.choices(int, weights=peso, k=1))
                self.inteligencia = rand_intel[0]
                
        def empregos(self):
            #empregos 0 = desempregado, 1=campo, 2=educacao
            for pessoa in lista_pessoas:
                if pessoa.inteligencia >= 0 and pessoa.inteligencia <= 5:
                    self.emprego = 1
                elif pessoa.inteligencia >=6:
                    self.emprego = 2


        self.emprego = 0
        self.inteligencia = 0

        empregos(self)
        intel(self)



def reproducao(idade_fertil_min, idade_fertil_max):
    for pessoa in lista_pessoas:
        if pessoa.sexo == 1:
            if pessoa.idade > idade_fertil_min:
                if pessoa.idade < idade_fertil_max:
                    if random.randint(1,5) == 1: # 1 em cada 5 engravidará
                        lista_pessoas.append(Pessoas(0))

def educacao_planeta(comida, agricultura, trabalhadores_campo, professores, educacao, pesquisa):
    for pessoa in lista_pessoas:
        if pessoa.idade > 25: #idade para profissão
            if pessoa.emprego == 2:
                professores += 1
    educacao += int(professores *1.50)
    pesquisa += int(educacao*2) #substituir o 2 por cientistas
    #immpedir divisão por 0
    if pesquisa <= 0:
        pesquisa += 1
    if educacao <= 0:
        educacao += 1

    def techs(pesquisa, agricultura): #tech e atividades gerais
        agricultura = math.ceil(math.sqrt(pesquisa))
        def agricultura_planeta(comida, agricultura, trabalhadores_campo): #agricultura
            trabalhadores_campo = 0
            for pessoa in lista_pessoas:
                if pessoa.idade > 18: #idade para profissão
                    if pessoa.emprego == 1:
                        trabalhadores_campo += 1
            comida += trabalhadores_campo*agricultura 
            if comida < len(lista_pessoas):
                del lista_pessoas[0:int(len(lista_pessoas)-comida)]
                comida = 0
            else:
                comida -= len(lista_pessoas)
            return comida, trabalhadores_campo
        agri= agricultura_planeta(comida, agricultura, trabalhadores_campo)
        return agricultura, agri
    tech = techs(pesquisa, agricultura)
    return f"Agricultura: Tech(Comida/Trab) ---Educação: Prof:{professores}/Edu:{educacao}/Pes:{pesquisa}\n\t    {tech}"

def sim():
    for x in range(pop_inicial):
        lista_pessoas.append(Pessoas(random.randint(18,50)))

def ano_corrente(idade_fertil_min, idade_fertil_max, professores, educacao, pesquisa, comida, agricultura, trabalhadores_campo):
    reproducao(idade_fertil_min,idade_fertil_max)
    educacao_planeta(comida, agricultura, trabalhadores_campo,professores, educacao, pesquisa)
    for pessoa in lista_pessoas:
        if pessoa.idade > random.randint(60,100):
            if pessoa.emprego == 1:
                lista_pessoas.remove(pessoa)
                trabalhadores_campo -= 1
            elif pessoa.emprego == 2:
                lista_pessoas.remove(pessoa)
                professores -= 1
            else:
                lista_pessoas.remove(pessoa)
        else:
            pessoa.idade += 1
    

sim()

while len(lista_pessoas) < 5000 and len(lista_pessoas) > 1:
    ano += 1
    ano_corrente(idade_fertil_min, idade_fertil_max, professores, educacao, pesquisa, comida, agricultura, trabalhadores_campo)

    print(f"\nAno: {ano} Pop: {len(lista_pessoas)}")
    print("{}".format(educacao_planeta(comida, agricultura, trabalhadores_campo,professores,educacao,pesquisa)))


    