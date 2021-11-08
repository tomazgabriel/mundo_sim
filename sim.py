import random
import math

cronometro = 0

pop_inicial = random.randint(20,50)

ano = 0

idade_fertil_min = random.randint(14,18)
idade_fertil_max = random.randint(35,40)

dinheiro = 0
valor_aposentadoria = 0
lista_dinheiro = []

expectativa_vida = 100
lista_mortos = []
mortes = 0

lista_pessoas = []
lista_idades = []
lista_inteligencia = []
idade_media = 0
inteligencia_media = 0


taxa_negativa = 1

comida = 100
agricultura = 0

educacao = 0
pesquisa = 0
ciencia = 1
medicina = 1

#trabalhos
trabalhadores_campo, trabalhadores_campo_aposentados = 0, 0
professores, professores_aposentados = 0, 0
cientistas, cientistas_aposentados = 0, 0
medicos, medicos_aposentados = 0, 0

aposentadoria = 0

class Pessoas:
    def __init__(self, idade):
        self.sexo = random.randint(0,1)
        self.idade = idade
        self.educacao = educacao
        self.emprego = 0
        self.inteligencia = random.randint(0,10)
        self.sorte = random.randint(0,10)
        self.dinheiro = random.randint(0,100)




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
                    

def educacao_planeta(comida, agricultura, trabalhadores_campo, professores, educacao, pesquisa, trabalhadores_campo_aposentados, professores_aposentados,taxa_negativa, cientistas, cientistas_aposentados, ciencia, medicina, medicos, medicos_aposentados, expectativa_vida):
    global aposentadoria
    global valor_aposentadoria
    for pessoa in lista_pessoas:
        #professores/cientistas/médicos
        if pessoa.idade > 25: #idade para profissão//aposentar-se aos 80 anos
            if pessoa.emprego == 2 and pessoa.idade <= 80: #professores
                professores += 1
            elif pessoa.emprego == 2 and pessoa.idade >= 80:
                professores -= 1

            if pessoa.emprego == 4 and pessoa.idade <= 80: #cientistas
                cientistas += 1
            elif pessoa.emprego == 4 and pessoa.idade >= 80:
                cientistas -= 1
                
        if pessoa.idade > 30:
            if pessoa.emprego == 5 and pessoa.idade <= 80: #medicos
                medicos += 1
            elif pessoa.emprego == 5 and pessoa.idade >= 80:
                medicos -= 1

        if pessoa.inteligencia == 0:
            taxa_negativa += 1
        
        #aposentadoria
        aposentadoria = (expectativa_vida/2 + 10)
        valor_aposentadoria = aposentadoria/10
        if pessoa.idade >= aposentadoria:
            if pessoa.emprego == 1: #campo
                trabalhadores_campo_aposentados += 1
                pessoa.emprego == 0
            elif pessoa.emprego == 2: #professor
                professores_aposentados += 1
                pessoa.emprego == 0

            elif pessoa.emprego == 4: #cientista
                cientistas_aposentados += 1
                pessoa.emprego == 0

            elif pessoa.emprego == 5: #medico
                medicos_aposentados += 1
                pessoa.emprego == 0
            
    taxa_negativa = math.ceil(taxa_negativa/10)
    ciencia += cientistas/taxa_negativa
    educacao += math.ceil(professores + ciencia)
    pesquisa += math.ceil((educacao + ciencia)) 
    medicina += math.ceil((medicos + ciencia)/1.5)

    #immpedir divisão por 0 //otimizar dps
    if pesquisa <= 0:
        pesquisa += 1
    if educacao <= 0:
        educacao += 1
    
    #expectativa de vida
    def func_exp():
        global expectativa_vida
        if medicina < 10:
            expectativa_vida = random.randint(30,50)
        elif medicina > 10 and medicina < 20:
            expectativa_vida = random.randint(50,80)
        elif medicina > 20 and medicina < 50:
            expectativa_vida = random.randint(50,100)
        elif medicina > 50 and medicina < 100:
            expectativa_vida = random.randint(80,100)
        elif medicina > 100 and medicina < 200:
            expectativa_vida = random.randint(110,120)
        elif medicina > 200 and medicina < 500:
            expectativa_vida = random.randint(120,130)
        elif medicina > 500:
            expectativa_vida = random.randint(130,150)

    func_exp()

    def empregos():
        #empregos 0 = aposentado, 1=campo, 2=educacao 3=desemprego 4=cientista 5=medico
        for pessoa in lista_pessoas:
            if pessoa.inteligencia >= 0 and pessoa.inteligencia <= 5: #campo
                pessoa.emprego = 1
                pessoa.dinheiro += 2
            elif pessoa.inteligencia >= 6 and pessoa.sorte < 5: #professor
                pessoa.emprego = 2
                pessoa.dinheiro += 4
            elif pessoa.inteligencia >= 6 and pessoa.sorte > 5 and pessoa.sorte < 7: #cienctista
                pessoa.emprego = 4
                pessoa.dinheiro += 6
            elif pessoa.inteligencia == 0: #desempregado
                pessoa.emprego = 3
                pessoa.dinheiro += 0
            elif pessoa.emprego == 3: #aposentado
                if pessoa.inteligencia >= 0 and pessoa.inteligencia <= 5: #campo
                    pessoa.dinheiro += valor_aposentadoria+1
                elif pessoa.inteligencia >= 6 and pessoa.sorte < 5: #professor
                    pessoa.dinheiro += valor_aposentadoria+2
                elif pessoa.inteligencia >= 6 and pessoa.sorte > 5 and pessoa.sorte < 7: #cienctista
                    pessoa.dinheiro += valor_aposentadoria+3
                elif pessoa.inteligencia >= 7 and pessoa.sorte > 7: #medico
                    pessoa.dinheiro += valor_aposentadoria+5
                elif pessoa.inteligencia == 0: #desempregado
                    pessoa.dinheiro += valor_aposentadoria
                    
            elif pessoa.inteligencia >= 7 and pessoa.sorte > 7: #medico
                pessoa.emprego = 5
                pessoa.dinheiro += 10
                
                
    
    empregos()

    def economia():
        inflacao = math.ceil(sum(lista_dinheiro)-len(lista_pessoas))
        #impedir divisão por zero
        if inflacao <= 0:
            inflacao += 0.1
        if len(lista_pessoas) > 0:
            preco_comida = ((comida+inflacao)/len(lista_pessoas)/10000)#preço alimento
            if preco_comida <0:
                preco_comida += 0.1
            for pessoa in lista_pessoas:
                lista_dinheiro.append(pessoa.dinheiro)
                if pessoa.dinheiro < preco_comida: #morrer de fome
                    lista_pessoas.remove(pessoa)
                    #print(f"Morreu de fome aos {pessoa.idade} com R${pessoa.dinheiro}")
                elif pessoa.dinheiro > preco_comida:
                    pessoa.dinheiro -= preco_comida
        #print(preco_comida)
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
                        idade_min = 16
                        break
                    while trabalhadores_campo < (len(lista_pessoas)/10):
                        idade_min = 10
                        break
                    while trabalhadores_campo > 100:
                        idade_min = 18
                        break
                    while trabalhadores_campo > 200:
                        idade_min = 20
                        break
                    while trabalhadores_campo > 300:
                        idade_min = 21
                        break
                    if pessoa.emprego == 1 and pessoa.idade <= 80:
                        trabalhadores_campo += 1
                    elif pessoa.emprego == 1 and pessoa.idade >= 80:
                        trabalhadores_campo -= 1
            comida += trabalhadores_campo*agricultura 
            if comida < len(lista_pessoas):
                del lista_pessoas[0:int(len(lista_pessoas)-comida)]
                economia()
                comida = 0
            else:
                economia()
                comida -= len(lista_pessoas)
            return comida, trabalhadores_campo
        agri= agricultura_planeta(comida, agricultura, trabalhadores_campo)
        return agricultura, agri
    tech = techs(pesquisa, agricultura)
    intel(educacao)
        
    return f"Agricultura: Tech(Comida/Trab) ---Educação: Prof:{professores}/Edu:{educacao}/Pes:{pesquisa}/Cientistas:{cientistas}/Medicina:{medicina}/Médicos:{medicos}/Tax_neg:{taxa_negativa}\n\t    {tech}\n|Trabalhadores rurais aposentados: {trabalhadores_campo_aposentados}|Professores aposentados: {professores_aposentados}|Cientistas Aposentados: {cientistas_aposentados}|Médicos Aposentados:{medicos_aposentados}"

def sim():
    for x in range(pop_inicial):
        lista_pessoas.append(Pessoas(random.randint(18,50)))

def ano_corrente(idade_fertil_min, idade_fertil_max, professores, educacao, pesquisa, comida, agricultura, trabalhadores_campo, trabalhadores_campo_aposentados, professores_aposentados, taxa_negativa, cientistas, cientistas_aposentados, ciencia, medicina, medicos, medicos_aposentados, expectativa_vida):
    reproducao(idade_fertil_min,idade_fertil_max)
    educacao_planeta(comida, agricultura, trabalhadores_campo,professores, educacao, pesquisa, trabalhadores_campo_aposentados, professores_aposentados, taxa_negativa, cientistas, cientistas_aposentados, ciencia, medicina, medicos, medicos_aposentados, expectativa_vida)
    global mortes
    for pessoa in lista_pessoas:
        if pessoa.idade >= expectativa_vida and pessoa.inteligencia != 0:
            lista_pessoas.remove(pessoa)
            #print(f"Morreu aos {pessoa.idade} anos. Expectativa de vida:{expectativa_vida}. Emprego:{pessoa.emprego}. Dinheiro:{pessoa.dinheiro}")
            lista_mortos.append(1)
        elif pessoa.idade >= expectativa_vida and pessoa.inteligencia == 0:
            taxa_negativa -= 1
            lista_pessoas.remove(pessoa)
            #print(f"Morreu aos {pessoa.idade} anos. Expectativa de vida:{expectativa_vida}. Emprego:{pessoa.emprego}. Dinheiro:{pessoa.dinheiro}")
            lista_mortos.append(1)
        else:
            pessoa.idade += 1
    mortes = sum(lista_mortos)


sim()
f = open("resultado.txt", 'w')
f.write(" ")
f.close()
f = open("resultado.txt", 'a', encoding='utf-8') 

segundos, minutos, horas = 0, 0 ,0
print("aguarde")
while len(lista_pessoas) < 10000 and len(lista_pessoas) > 1 and ano < 10000:
    ano += 1
    segundos += 1
    if segundos > 60:
        segundos = 0
        minutos += 1
        if minutos > 60:
            segundos = 0
            minutos = 0
            horas =+ 1

    ano_corrente(idade_fertil_min, idade_fertil_max, professores, educacao, pesquisa, comida, agricultura, trabalhadores_campo, trabalhadores_campo_aposentados, professores_aposentados, taxa_negativa, cientistas, cientistas_aposentados, ciencia, medicina, medicos, medicos_aposentados, expectativa_vida)
    #print(f"\nAno: {ano} Pop: {len(lista_pessoas)} Mortes: {mortes}")
    #print("{}".format(educacao_planeta(comida, agricultura, trabalhadores_campo,professores,educacao,pesquisa, trabalhadores_campo_aposentados, professores_aposentados, taxa_negativa, cientistas, cientistas_aposentados, ciencia, medicina, medicos, medicos_aposentados, expectativa_vida)))
    f.write(f"\nAno: {ano} Pop: {len(lista_pessoas)}\nMortes:{sum(lista_mortos)}\n" "{}\n".format(educacao_planeta(comida, agricultura, trabalhadores_campo,professores,educacao,pesquisa, trabalhadores_campo_aposentados, professores_aposentados, taxa_negativa, cientistas, cientistas_aposentados, ciencia, medicina, medicos, medicos_aposentados, expectativa_vida)))
    

cronometro = str(f"{horas}:{minutos}:{segundos}")
print("aguarde...")
print("tempo: ", cronometro)
#dados gerais pós simulação
lista_riquezas = []
print(f"\nAno: {ano} Pop: {len(lista_pessoas)} Mortes: {mortes}")
print("{}".format(educacao_planeta(comida, agricultura, trabalhadores_campo,professores,educacao,pesquisa, trabalhadores_campo_aposentados, professores_aposentados, taxa_negativa, cientistas, cientistas_aposentados, ciencia, medicina, medicos, medicos_aposentados, expectativa_vida)))
if len(lista_pessoas) > 0:
    for pessoa in lista_pessoas:
        lista_idades.append(pessoa.idade)
        lista_inteligencia.append(pessoa.inteligencia)
        lista_riquezas.append(pessoa.dinheiro)
        idade_media = math.ceil(sum(lista_idades)/len(lista_pessoas))
        inteligencia_media = str(sum(lista_inteligencia)/len(lista_pessoas))
        riqueza_media = str(sum(lista_riquezas)/len(lista_pessoas))
         

    print(f"Média de idade: {idade_media}|Média de inteligência: {inteligencia_media[:5]}|Idade final para aposentadoria:{aposentadoria}|Valor aposentadoria final:{valor_aposentadoria}|Média de riquezas:{riqueza_media[:5]}")

    f.write(f"\n(Média de idade: {idade_media}|Média de inteligência: {inteligencia_media[:4]}|Idade final aposentadoria:{aposentadoria}")
    f.close()