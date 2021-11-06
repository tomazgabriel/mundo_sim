import random
import math

pop_inicial = 50

ano = 0

idade_fertil_min = random.randint(14,18)
idade_fertil_max = random.randint(35,40)

lista_pessoas = []
lista_idades = []
lista_inteligencia = []
idade_media = 0
inteligencia_media = 0

taxa_negativa = 1

comida = 0
agricultura = 5

educacao = 0
pesquisa = 0

#trabalhos
trabalhadores_campo, trabalhadores_campo_aposentados = 0, 0
professores, professores_aposentados = 0, 0

class Pessoas:
    def __init__(self, idade):
        self.sexo = random.randint(0,1)
        self.idade = idade
        self.educacao = educacao
        self.emprego = 0
        self.inteligencia = random.randint(0,10)





def reproducao(idade_fertil_min, idade_fertil_max):
    for pessoa in lista_pessoas:
        if pessoa.sexo == 1:
            if pessoa.idade > idade_fertil_min:
                if pessoa.idade < idade_fertil_max:
                    if random.randint(1,5) == 1: # 1 em cada 5 engravidará
                        lista_pessoas.append(Pessoas(0))

def educacao_planeta(comida, agricultura, trabalhadores_campo, professores, educacao, pesquisa, trabalhadores_campo_aposentados, professores_aposentados,taxa_negativa):
    for pessoa in lista_pessoas:
        if pessoa.idade > 25: #idade para profissão//aposentar-se aos 80 anos
            if pessoa.emprego == 2 and pessoa.idade <= 80:
                professores += 1
            elif pessoa.emprego == 2 and pessoa.idade >= 80:
                professores -= 1
        #taxa negativa
        if pessoa.emprego == 0:
            taxa_negativa += math.ceil(1-((educacao+pesquisa)*1.50)) #substituir por ciencia
    educacao += math.ceil((professores*1.50)/taxa_negativa) #substituir por ciencia
    pesquisa += math.ceil((educacao*1.50)) #substituir o 2 por cientistas
    #immpedir divisão por 0 //otimizar dps
    if pesquisa <= 0:
        pesquisa += 1
    if educacao <= 0:
        educacao += 1
    
    def empregos():
        #empregos 0 = aposentado, 1=campo, 2=educacao 3=desemprego
        for pessoa in lista_pessoas:
            if pessoa.inteligencia >= 0 and pessoa.inteligencia <= 5:
                pessoa.emprego = 1
            elif pessoa.inteligencia >= 6 and pessoa.inteligencia <= 8:
                pessoa.emprego = 2
            elif pessoa.inteligencia == 0:
                pessoa.emprego = 3
                
                
    
    empregos()

    def intel(educacao):
    #chances da população ter mais inteligência aumentaram com a quantidade de educação
        for pessoa in lista_pessoas:
            if educacao >= 0 and educacao <= 10:
                int = [0,1,2,3,4,5,6,7,8,9,10]
                peso =[10,10,5,5,2,1,1,0,0,0,0]
                rand_intel = (random.choices(int, weights=peso, k=1))
                pessoa.inteligencia = rand_intel[0]
            elif educacao >= 11 and educacao <= 30:
                int = [0,1,2,3,4,5,6,7,8,9,10]
                peso =[9,10,6,6,2,1,1,1,0,0,0]
                rand_intel = (random.choices(int, weights=peso, k=1))
                pessoa.inteligencia = rand_intel[0]
            elif educacao >= 31 and educacao <= 499:
                int = [0,1,2,3,4,5,6,7,8,9,10]
                peso =[7,10,9,8,5,1,1,1,0,0,0]
                rand_intel = (random.choices(int, weights=peso, k=1))
                pessoa.inteligencia = rand_intel[0]
            elif educacao >= 500 and educacao <= 1000:
                int = [0,1,2,3,4,5,6,7,8,9,10]
                peso =[6,9,8,7,6,5,1,1,1,1,1]
                rand_intel = (random.choices(int, weights=peso, k=1))
                pessoa.inteligencia = rand_intel[0]
            elif educacao >= 3000:
                int = [0,1,2,3,4,5,6,7,8,9,10]
                peso =[1,1,1,1,1,1,1,1,1,1,1]
                rand_intel = (random.choices(int, weights=peso, k=1))
                pessoa.inteligencia = rand_intel[0]
            elif educacao >= 5000:
                int = [0,1,2,3,4,5,6,7,8,9,10]
                peso =[0,1,1,2,2,1,1,1,1,1,1]
                rand_intel = (random.choices(int, weights=peso, k=1))
                pessoa.inteligencia = rand_intel[0]
    
    def techs(pesquisa, agricultura): #tech e atividades gerais
        agricultura = math.ceil(math.sqrt(pesquisa)) + 2 #trocar o 2 por ciencia
        if agricultura <= 1: agricultura += 1 #impedir divisão por 0
        def agricultura_planeta(comida, agricultura, trabalhadores_campo): #agricultura
            trabalhadores_campo = 0
            for pessoa in lista_pessoas:
                if pessoa.idade > 18: #idade para profissão//aposentar-se aos 80 anos
                    if pessoa.emprego == 1 and pessoa.idade <= 60:
                        trabalhadores_campo += 1
                    elif pessoa.emprego == 1 and pessoa.idade >= 60:
                        trabalhadores_campo -= 1
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
    intel(educacao)
    #dados
    for pessoa in lista_pessoas: #aposentadoria/média de idade
        if pessoa.emprego == 1 and pessoa.idade >= 60:
            trabalhadores_campo_aposentados += 1
            pessoa.emprego == 0
        if pessoa.emprego == 2 and pessoa.idade >= 80:
            professores_aposentados += 1
            pessoa.emprego == 0
    return f"Agricultura: Tech(Comida/Trab) ---Educação: Prof:{professores}/Edu:{educacao}/Pes:{pesquisa}/Tax_neg:{taxa_negativa}\n\t    {tech}\n|Trabalhadores rurais aposentados: {trabalhadores_campo_aposentados}| Professores aposentados: {professores_aposentados}"

def sim():
    for x in range(pop_inicial):
        lista_pessoas.append(Pessoas(random.randint(18,50)))

def ano_corrente(idade_fertil_min, idade_fertil_max, professores, educacao, pesquisa, comida, agricultura, trabalhadores_campo, trabalhadores_campo_aposentados, professores_aposentados, taxa_negativa):
    reproducao(idade_fertil_min,idade_fertil_max)
    educacao_planeta(comida, agricultura, trabalhadores_campo,professores, educacao, pesquisa, trabalhadores_campo_aposentados, professores_aposentados, taxa_negativa)
    for pessoa in lista_pessoas:
        if pessoa.idade > 90:
            if pessoa.emprego == 1:
                lista_pessoas.remove(pessoa)
                trabalhadores_campo -= 1
            elif pessoa.emprego == 2:
                lista_pessoas.remove(pessoa)
                professores -= 1
            elif pessoa.emprego == 0:
                lista_pessoas.remove(pessoa)
            else:
                lista_pessoas.remove(pessoa)
        else:
            pessoa.idade += 1
    

sim()

while len(lista_pessoas) < 20000 and len(lista_pessoas) > 1:
    ano += 1
    ano_corrente(idade_fertil_min, idade_fertil_max, professores, educacao, pesquisa, comida, agricultura, trabalhadores_campo, trabalhadores_campo_aposentados, professores_aposentados, taxa_negativa)

    print(f"\nAno: {ano} Pop: {len(lista_pessoas)}")
    print("{}".format(educacao_planeta(comida, agricultura, trabalhadores_campo,professores,educacao,pesquisa, trabalhadores_campo_aposentados, professores_aposentados, taxa_negativa)))

#dados gerais pós simulação
    #média de idade/inteligencia
if len(lista_pessoas) > 0:
    for pessoa in lista_pessoas:
        lista_idades.append(pessoa.idade)
        lista_inteligencia.append(pessoa.inteligencia)
        idade_media = math.ceil(sum(lista_idades)/len(lista_pessoas))
        inteligencia_media = str(sum(lista_inteligencia)/len(lista_pessoas))

    print(f"Média de idade: {idade_media}|Média de inteligência: {inteligencia_media[:4]}")
