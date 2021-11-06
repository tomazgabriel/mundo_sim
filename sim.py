import random
import math

pop_inicial = random.randint(20,50)

ano = 0

idade_fertil_min = random.randint(14,18)
idade_fertil_max = random.randint(35,40)

lista_pessoas = []
lista_idades = []
lista_inteligencia = []
idade_media = 0
inteligencia_media = 0

taxa_negativa = 1

comida = random.randint(10,50)
agricultura = 0

educacao = 0
pesquisa = 0
ciencia = 1

#trabalhos
trabalhadores_campo, trabalhadores_campo_aposentados = 0, 0
professores, professores_aposentados = 0, 0
cientistas, cientistas_aposentados = 0, 0

class Pessoas:
    def __init__(self, idade):
        self.sexo = random.randint(0,1)
        self.idade = idade
        self.educacao = educacao
        self.emprego = 0
        self.inteligencia = random.randint(0,10)
        self.sorte = random.randint(0,10)




def reproducao(idade_fertil_min, idade_fertil_max):
    for pessoa in lista_pessoas:
        if pessoa.sexo == 1:
            if pessoa.idade > idade_fertil_min:
                if pessoa.idade < idade_fertil_max:
                    if pessoa.sorte <= 2:
                        if random.randint(1,10) == 1: # 1 em cada 10 changes
                            lista_pessoas.append(Pessoas(0))
                    elif pessoa.sorte > 2 and pessoa.sorte <= 5:
                        if random.randint(1,7) == 1: 
                            lista_pessoas.append(Pessoas(0))
                    elif pessoa.sorte > 5:
                        if random.randint(1,5) == 1: 
                            lista_pessoas.append(Pessoas(0))
                    

def educacao_planeta(comida, agricultura, trabalhadores_campo, professores, educacao, pesquisa, trabalhadores_campo_aposentados, professores_aposentados,taxa_negativa, cientistas, cientistas_aposentados, ciencia):
    #professores e cientistas
    for pessoa in lista_pessoas:
        if pessoa.idade > 25: #idade para profissão//aposentar-se aos 80 anos
            if pessoa.emprego == 2 and pessoa.idade <= 80: #professores
                professores += 1
            elif pessoa.emprego == 2 and pessoa.idade >= 80:
                professores -= 1

            if pessoa.emprego == 4 and pessoa.idade <= 80: #cientists
                cientistas += 1
            elif pessoa.emprego == 4 and pessoa.idade >= 80:
                cientistas -= 1
        
        if pessoa.inteligencia == 0:
            taxa_negativa += 1
            
    taxa_negativa = math.ceil(taxa_negativa/10)
    ciencia += cientistas/taxa_negativa
    educacao += math.ceil(professores + ciencia)
    pesquisa += math.ceil((educacao + ciencia)) 
    #immpedir divisão por 0 //otimizar dps
    if pesquisa <= 0:
        pesquisa += 1
    if educacao <= 0:
        educacao += 1
    
    def empregos():
        #empregos 0 = aposentado, 1=campo, 2=educacao 3=desemprego 4=cientista
        for pessoa in lista_pessoas:
            if pessoa.inteligencia >= 0 and pessoa.inteligencia <= 5: #campo
                pessoa.emprego = 1
            elif pessoa.inteligencia >= 6 and pessoa.sorte < 10: #professor
                pessoa.emprego = 2
            elif pessoa.inteligencia >= 6 and pessoa.sorte == 10: #cienctista
                pessoa.emprego = 4
            elif pessoa.inteligencia == 0: #desempregado
                pessoa.emprego = 3
                
                
    
    empregos()

    def intel(educacao):
    #chances da população ter mais inteligência aumentaram com a quantidade de educação
        for pessoa in lista_pessoas:
            if educacao >= 0 and educacao <= 10:
                int = [0,1,2,3,4,5,6,7,8,9,10]
                peso =[10,10,5,5,2,2,1,1,1,1,1]
                rand_intel = (random.choices(int, weights=peso, k=1))
                pessoa.inteligencia = rand_intel[0]
            elif educacao >= 11 and educacao <= 30:
                int = [0,1,2,3,4,5,6,7,8,9,10]
                peso =[9,10,6,6,2,2,2,1,1,1,1]
                rand_intel = (random.choices(int, weights=peso, k=1))
                pessoa.inteligencia = rand_intel[0]
            elif educacao >= 31 and educacao <= 499:
                int = [0,1,2,3,4,5,6,7,8,9,10]
                peso =[7,10,9,8,5,2,2,2,1,1,1]
                rand_intel = (random.choices(int, weights=peso, k=1))
                pessoa.inteligencia = rand_intel[0]
            elif educacao >= 500 and educacao <= 1000:
                int = [0,1,2,3,4,5,6,7,8,9,10]
                peso =[6,9,8,7,6,5,2,2,1,1,1]
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
        if agricultura < 5:
            agricultura = math.ceil(math.sqrt(pesquisa))
        if agricultura > 5 and agricultura < 10:
            agricultura = 5 + math.ceil(math.sqrt(pesquisa)/5)
        if agricultura > 10 and agricultura < 20:
            agricultura = 10 + math.ceil(math.sqrt(pesquisa)/10)
        if agricultura > 20:
            agricultura = 20 + math.ceil(math.sqrt(pesquisa)/20)



        if agricultura <= 1: agricultura += 1 #impedir divisão por 0
        def agricultura_planeta(comida, agricultura, trabalhadores_campo): #agricultura
            trabalhadores_campo = 0
            idade_min = 0
            for pessoa in lista_pessoas:
                if pessoa.idade > idade_min: #idade para profissão//aposentar-se aos 80 anos
                    while trabalhadores_campo > (len(lista_pessoas)/10):
                        idade_min = 18
                        break
                    while trabalhadores_campo < (len(lista_pessoas)/10):
                        idade_min = 12
                        break
                    while trabalhadores_campo > 100:
                        idade_min = 19
                        break
                    while trabalhadores_campo > 200:
                        idade_min = 20
                        break
                    while trabalhadores_campo > 300:
                        idade_min = 21
                        break
                    if pessoa.emprego == 1 and pessoa.idade <= 60:
                        trabalhadores_campo += 1
                    elif pessoa.emprego == 1 and pessoa.idade >= 60:
                        trabalhadores_campo -= 1
            comida += trabalhadores_campo*agricultura 
            print("idade minima para trabalhar no campo:",idade_min)

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
        if pessoa.emprego == 4 and pessoa.idade >= 80:
            cientistas_aposentados += 1
            pessoa.emprego == 0
        
    return f"Agricultura: Tech(Comida/Trab) ---Educação: Prof:{professores}/Edu:{educacao}/Pes:{pesquisa}/Cientistas:{cientistas}/Tax_neg:{taxa_negativa}\n\t    {tech}\n|Trabalhadores rurais aposentados: {trabalhadores_campo_aposentados}|Professores aposentados: {professores_aposentados}| Cientistas Aposentados: {cientistas_aposentados}"

def sim():
    for x in range(pop_inicial):
        lista_pessoas.append(Pessoas(random.randint(18,50)))

def ano_corrente(idade_fertil_min, idade_fertil_max, professores, educacao, pesquisa, comida, agricultura, trabalhadores_campo, trabalhadores_campo_aposentados, professores_aposentados, taxa_negativa, cientistas, cientistas_aposentados, ciencia):
    reproducao(idade_fertil_min,idade_fertil_max)
    educacao_planeta(comida, agricultura, trabalhadores_campo,professores, educacao, pesquisa, trabalhadores_campo_aposentados, professores_aposentados, taxa_negativa, cientistas, cientistas_aposentados, ciencia)
    for pessoa in lista_pessoas:
        if pessoa.idade > 90 and pessoa.inteligencia != 0:
            lista_pessoas.remove(pessoa)
        elif pessoa.idade > 90 and pessoa.inteligencia == 0:
            taxa_negativa -= 1
            lista_pessoas.remove(pessoa)
        else:
            pessoa.idade += 1
    

sim()
f = open("resultado.txt", 'w')
f.write(" ")
f.close()
f = open("resultado.txt", 'a', encoding='utf-8') 

while len(lista_pessoas) < 20000 and len(lista_pessoas) > 1 and ano <= 10000:
    ano += 1
    ano_corrente(idade_fertil_min, idade_fertil_max, professores, educacao, pesquisa, comida, agricultura, trabalhadores_campo, trabalhadores_campo_aposentados, professores_aposentados, taxa_negativa, cientistas, cientistas_aposentados, ciencia)

    print(f"\nAno: {ano} Pop: {len(lista_pessoas)}")
    print("{}".format(educacao_planeta(comida, agricultura, trabalhadores_campo,professores,educacao,pesquisa, trabalhadores_campo_aposentados, professores_aposentados, taxa_negativa, cientistas, cientistas_aposentados, ciencia)))
    f.write(f"\nAno: {ano} Pop: {len(lista_pessoas)}\n" "{}\n".format(educacao_planeta(comida, agricultura, trabalhadores_campo,professores,educacao,pesquisa, trabalhadores_campo_aposentados, professores_aposentados, taxa_negativa, cientistas, cientistas_aposentados, ciencia)))
    
#dados gerais pós simulação
    #média de idade/inteligencia
if len(lista_pessoas) > 0:
    for pessoa in lista_pessoas:
        lista_idades.append(pessoa.idade)
        lista_inteligencia.append(pessoa.inteligencia)
        idade_media = math.ceil(sum(lista_idades)/len(lista_pessoas))
        inteligencia_media = str(sum(lista_inteligencia)/len(lista_pessoas))

    print(f"Média de idade: {idade_media}|Média de inteligência: {inteligencia_media[:4]}")

f.write(f"\n(Média de idade: {idade_media}|Média de inteligência: {inteligencia_media[:4]}")
f.close()
