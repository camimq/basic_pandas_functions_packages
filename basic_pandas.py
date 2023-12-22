# %% [markdown]
# # <font color=green> PYTHON PARA DATA SCIENCE - PANDAS
# ---

# %% [markdown]
# # <font color=green> 1. INTRODUÇÃO AO PYTHON
# ---

# %% [markdown]
# # 1.1 Introdução

# %% [markdown]
# > Python é uma linguagem de programação de alto nível com suporte a múltiplos paradigmas de programação. É um projeto *open source* e desde seu surgimento, em 1991, vem se tornando uma das linguagens de programação interpretadas mais populares.
# >
# > Nos últimos anos Python desenvolveu uma comunidade ativa de processamento científico e análise de dados e vem se destacando como uma das linguagens mais relevantes quando o assundo é ciência de dados e machine learning, tanto no ambiente acadêmico como também no mercado.

# %% [markdown]
# # 1.2 Instalação e ambiente de desenvolvimento

# %% [markdown]
# ### Instalação Local
# 
# ### https://www.python.org/downloads/
# ### ou
# ### https://www.anaconda.com/distribution/

# %% [markdown]
# ### Google Colaboratory
# 
# ### https://colab.research.google.com

# %% [markdown]
# ### Verificando versão

# %%
!python -V

# %% [markdown]
# # 1.3 Trabalhando com dados

# %%
import pandas as pd
##pd.set_option('display.max_rows', 1000) ## para ver o dataframe inteiro

# %%
dataset = pd.read_csv(r'C:\Users\Elitebook\OneDrive\Desktop\web dev\repositorios\fiap\alura\warm up\1_pandas\data\db.csv', sep = ';')

# %%
dataset

# %%
dataset.dtypes


# %%
dataset[['Quilometragem', 'Valor']].describe()

# %%
dataset.info()

# %% [markdown]
# # <font color=green> 2. TRABALHANDO COM TUPLAS
# ---

# %% [markdown]
# # 2.1 Criando tuplas
# 
# Tuplas são sequências imutáveis que são utilizadas para armazenar coleções de itens, geralmente heterogêneos. Podem ser construídas de várias formas:
# ```
# - Utilizando um par de parênteses: ( )
# - Utilizando uma vírgula à direita: x,
# - Utilizando um par de parênteses com itens separados por vírgulas: ( x, y, z )
# - Utilizando: tuple() ou tuple(iterador)
# ```

# %%
()

# %%
1,2,3

# %%
nome = 'Passat'
valor = 153000
(nome, valor)

# %%
nomes_carros = tuple(['Jetta Variant', 'Passat', 'Crossfox', 'DS5'])
nomes_carros

# %%
type(nomes_carros)

# %% [markdown]
# # 2.2 Seleções em tuplas

# %%
nomes_carros = tuple(['Jetta Variant', 'Passat', 'Crossfox', 'DS5'])
nomes_carros

# %%
nomes_carros[0]

# %%
nomes_carros[1]

# %%
nomes_carros[-1]

# %%
nomes_carros[1:3]

# %%
nomes_carros = ('Jetta Variant', 'Passat', 'Crossfox', 'DS5', ('Fusca', 'Gol', 'C4'))
nomes_carros

# %%
nomes_carros[-1]

# %%
nomes_carros[-1][1]

# %%
carros = (
    (
        'Jetta Variant',
        'Motor 4.0 Turbo',
        2003,
        False,
        ('Rodas de liga', 'Travas elétricas', 'Piloto automático')
    ),
    (
        'Passat',
        'Motor Diesel',
        1991,
        True,
        ('Central multimídia', 'Teto panorâmico', 'Freios ABS')
    )
)

# %%
carros[0][3]

# %%
carros[-1][-1][-1]

# %%
carros[0][-1][:2]

# %% [markdown]
# # 2.3 Iterando em tuplas

# %%
nomes_carros = ('Jetta Variant', 'Passat', 'Crossfox', 'DS5')
nomes_carros

# %%
for item in nomes_carros:
  print(item)

# %% [markdown]
# ### Desempacotamento de tuplas

# %%
nomes_carros = ('Jetta Variant', 'Passat', 'Crossfox', 'DS5')
nomes_carros

# %%
carro_1, carro_2, carro_3, carro_4 = nomes_carros
carro_1

# %%
carro_2

# %%
carro_3

# %%
carro_4

# %%
_, A, _, B = nomes_carros

# %%
A

# %%
B

# %%
_, C, *_ = nomes_carros

# *_ é uma forma de selecionar SOMENTE o segundo ítem da lista, sem ter q mencionar todos os outros que vem depois.

# %%
C

# %% [markdown]
# ## *zip()*
# 
# https://docs.python.org/3.6/library/functions.html#zip

# %%
carros = ['Jetta Variant', 'Passat', 'Crossfox', 'DS5']
carros

# %%
valores = [88078.64, 106161.94, 72832.16, 124549.07]
valores

# %%
list(zip(carros, valores))

# %%
for item in zip(carros, valores):
  print(item)

# %%
for carro, valor in zip(carros, valores):
  print(carro, valor)

# %%
for carro, valor in zip(carros, valores):
  if(valor > 100000):
    print(carro, valor)

# %%
carros = (
    (
        'Jetta Variant',
        'Motor 4.0 Turbo',
        2003,
        False,
        ('Rodas de liga', 'Travas elétricas', 'Piloto automático')
    ),
    (
        'Passat',
        'Motor Diesel',
        1991,
        True,
        ('Central multimídia', 'Teto panorâmico', 'Freios ABS')
    )
)

# %%
for tupla in carros:
  for item in tupla[-1]:
    print(item)

# %%
nomes = ['Passat', 'Crossfox', 'DS5', 'C4', 'Jetta']
kms = [15000, 12000, 32000, 8000, 50000]

# %%
list(zip(nomes, kms))

# %%
for nome, km in zip(nomes, kms):
  if km < 20000:
    print(nome, km)

# %% [markdown]
# # <font color=green> 3. TRABALHANDO COM DICIONÁRIOS
# ---

# %% [markdown]
# # 3.1 Criando dicionários
# 
# Listas são coleções sequenciais, isto é, os itens destas sequências estão ordenados e utilizam índices (números inteiros) para acessar os valores.
# 
# Os dicionários são coleções um pouco diferentes. São estruturas de dados que representam um tipo de mapeamento. Mapeamentos são coleções de associações entre pares de valores onde o primeiro elemento do par é conhecido como chave (*key*) e o segundo como valor (*value*).
# 
# ```
# dicionario = {key_1: value_1, key_2: value_2, ..., key_n: value_n}
# ```
# 
# https://docs.python.org/3.6/library/stdtypes.html#typesmapping

# %%
carros = ['Jetta Variant', 'Passat', 'Crossfox']
carros

# %%
valores = [88078.64, 106161.94, 72832.16]
valores

# %%
carros.index('Passat')

# %%
valores[carros.index('Passat')]

# %%
#             chave          valor    chave       valor      chave       valor
dados = {'Jetta Variant' : 88078.64, 'Passat' : 106161.94, 'Crossfox' : 72832.16}
dados

# %%
type(dados)

# %% [markdown]
# ### Criando dicionários com *zip()*

# %%
list(zip(carros, valores))

# %%
dados = dict((zip(carros, valores)))
dados

# %% [markdown]
# # 3.2 Operações com dicionários

# %%
dados = {'Jetta Variant' : 88078.64, 'Passat' : 106161.94, 'Crossfox' : 72832.16}
dados

# %% [markdown]
# ## *dict[ key ]*
# 
# Retorna o valor correspondente à chave (*key*) no dicionário.

# %%
dados['Passat']

# %% [markdown]
# ## *key in dict*
# 
# Retorna **True** se a chave (*key*) for encontrada no dicionário.

# %%
'Ferrari' in dados

# %%
'Passat' in dados

# %%
'Fusca' not in dados

# %% [markdown]
# ## *len(dict)*
# 
# Retorna o número de itens do dicionário.

# %%
len(dados) #conta pares (chave:valor)

# %% [markdown]
# ## *dict[ key ] = value*
# 
# Inclui um item ao dicionário.

# %%
dados['DS5'] = 124549.07

# %%
dados

# %% [markdown]
# ## *del dict[ key ]*
# 
# Remove o item de chave (*key*) do dicionário.

# %%
del dados ['Jetta Variant']
dados

# %%
dados = {
    'Passat': {
        'ano': 2012,
        'km': 50000,
        'valor': 75000,
        'acessorios': ['Airbag', 'ABS']
    },
    'Crossfox': {
        'ano': 2015,
        'km': 35000,
        'valor': 25000
    }
}

print(dados)

# %%
# Testar se a chave acessorios existe no dicionário de informações do carro Crossfox (Resposta: False)
'acessorios' in dados['Crossfox']

# %%
# Testar se a chave acessorios existe no dicionário de informações do carro Passat (Resposta: True)
'acessorios' in dados['Passat']

# %%
# Obter o valor do carro Crossfox (Resposta: 25000)
dados['Crossfox']['valor']

# %%
# Acessar o último acessório do carro Passat (Resposta: 'ABS')
dados['Passat']['acessorios'][1]

# %% [markdown]
# # 3.3 Métodos de dicionários

# %% [markdown]
# ## *dict.update()*
# 
# Atualiza o dicionário.

# %%
dados

# %%
dados.update({'Passat' : 106161.94})
dados

# %%
dados.update({'Passat' : 106161.95, 'Fusca' : 150000})
dados

# %% [markdown]
# ## *dict.copy()*
# 
# Cria uma cópia do dicionário.

# %%
dadosCopy = dados.copy()

# %%
dadosCopy

# %%
del dadosCopy['Fusca']
dadosCopy

# %%
dados

# %% [markdown]
# ## *dict.pop(key[, default ])*
# 
# Se a chave for encontrada no dicionário, o item é removido e seu valor é retornado. Caso contrário, o valor especificado como *default* é retornado. Se o valor *default* não for fornecido e a chave não for encontrada no dicionário um erro será gerado.

# %%
dadosCopy

# %%
dadosCopy.pop('Passat')

# %%
dadosCopy

# %%
dadosCopy.pop('Passat', 'Chave não encontrada')

# %%
dadosCopy.pop('DS5')

# %%
dadosCopy

# %% [markdown]
# ## *dict.clear()*
# 
# Remove todos os itens do dicionário.

# %%
dadosCopy.clear()

# %%
dadosCopy

# %%
dados2 = {'Jetta': 88000, 'Crossfox': 72000, 'DS5': 124000}

# %%
dados2.update({'Passat' : 8500})
dados2

# %%
dados2.update(Fusca = 160000)
dados2

# %% [markdown]
# # 3.4 Iterando em dicionários

# %%
dados = {'Crossfox' : 72832.16, 'DS5' : 124549.07, 'Fusca' : 150000, 'Jettar Variant' : 88078.64, 'Passat' : 106161.95}
dados

# %% [markdown]
# ## *dict.keys()*
# 
# Retorna uma lista contendo as chaves (*keys*) do dicionário.

# %%
dados.keys()

# %%
for key in dados.keys():
  print(dados[key])

# %% [markdown]
# ## *dict.values()*
# 
# Retorna uma lista com todos os valores (*values*) do dicionário.

# %%
dados.values()

# %% [markdown]
# ## *dict.items()*
# 
# Retorna uma lista contendo uma tupla para cada par chave-valor (*key-value*) do dicionário.

# %%
dados.items()

# %%
for item in dados.items():
  print(item)

# %%
for key, value in dados.items():
  print(key, value)

# %%
for key, value in dados.items():
  if (value > 100000):
    print(key)

# %%
dados = {
    'Crossfox': {'valor': 72000, 'ano': 2005},
    'DS5': {'valor': 125000, 'ano': 2015},
    'Fusca': {'valor': 150000, 'ano': 1976},
    'Jetta': {'valor': 88000, 'ano': 2010},
    'Passat': {'valor': 106000, 'ano': 1998}
}
dados

# %%
for item in dados.items():
  if(item[1]['ano'] >= 2000):
    print(key, item[1]['ano'])


# %% [markdown]
# # <font color=green> 4. FUNÇÕES E PACOTES
# ---
#     
# Funções são unidades de código reutilizáveis que realizam uma tarefa específica, podem receber alguma entrada e também podem retornar alguma resultado.

# %% [markdown]
# # 4.1 Built-in function
# 
# A linguagem Python possui várias funções integradas que estão sempre acessíveis. Algumas já utilizamos em nosso treinamento: type(), print(), zip(), len(), set() etc.
# 
# https://docs.python.org/3.6/library/functions.html

# %%
dados = {'Jetta Variant': 88078.64, 'Passat': 106161.94, 'Crossfox': 72832.16}
dados

# %%
valores = []
for valor in dados.values():
  valores.append(valor)
valores

# %%
soma = 0
for valor in dados.values():
  soma += valor
soma

# %%
list(dados.values())

# %%
sum(dados.values())

# %%
help(sum)

# %% [markdown]
# # 4.2 Definindo funções sem e com parâmetros

# %% [markdown]
# ### Funções sem parâmetros
# 
# #### Formato padrão
# 
# ```
# def <nome>():
#     <instruções>
# ```

# %%
def media ():
  valor = (1 + 2 + 3) / 3
  print(valor)

media()

# %%
media()

# %% [markdown]
# ### Funções com parâmetros
# 
# #### Formato padrão
# 
# ```
# def <nome>(<param_1>, <param_2>, ..., <param_n>):
#     <instruções>
# ```

# %%
def media(number_1, number_2, number_3):
  valor = (number_1 + number_2 + number_3) / 3
  print(valor)

# %%
media(1, 2, 3)

# %%
media(23, 45, 67)

# %%
def media (lista):
  valor = sum(lista) / len(lista)
  print(valor)

# %%
media([1, 2, 3, 4, 5, 6, 37, 38, 45, 88, 90, 10])

# %%
resultado = media([1, 2, 3, 4, 5, 6, 37, 38, 45, 88, 90, 10])

# %%
resultado

# %%
type(resultado)

# %% [markdown]
# # Quilometragem média de um veículo
# 
# Uma tarefa importante em um trabalho de cientista de dados é o tratamento do dataset que vamos utilizar. Essa tarefa é dividida em várias etapas e uma delas é a sumarização dos dados, onde obtemos estatísticas descritivas para ajudar nas tomadas de decisão.
# 
# Algumas sumarizações precisam de um conjunto de elaborações, que devem ser desenvolvidas pelo próprio pesquisador. Neste ponto, as funções são bastante úteis no trabalho do cientista de dados. Com elas, podemos definir um conjunto de tarefas específicas, que recebem entradas e retornam resultados, e reutilizar esta codificação em outras partes de nosso projeto.
# 
# Um exemplo disso em nosso projeto é o cálculo da quilometragem média que um veículo rodou por ano. Não existe uma função pronta para o cálculo desta estatística em Python, e por isso precisamos escrever uma função que obtenha este valor.
# 
# Considere o conjunto de informações abaixo para responder o problema:
# 
# https://i.imgur.com/axPH6y3.png
# 
# ```
# dados = {
#     'Crossfox': {'km': 35000, 'ano': 2005},
#     'DS5': {'km': 17000, 'ano': 2015},
#     'Fusca': {'km': 130000, 'ano': 1979},
#     'Jetta': {'km': 56000, 'ano': 2011},
#     'Passat': {'km': 62000, 'ano': 1999}
# }
# ```
# 
# A estrutura a seguir é a definição de uma função que obtém e imprime a quilometragem média anual de cada veículo em um dicionário com a estrutura do dicionário `dados` acima:
# 
# <b>In[1]</b>
# 
# ```
# def km_media(dataset, ano_atual):
#     for item in _______________:
#         result = _____________ / (ano_atual - ____________)
#         print(result)
# ```
# 
# <b>In[2]</b>
# 
# ```
# def km_media(dataset, ano_atual):
#     for item in _______________:
#         result = _____________ / (ano_atual - ____________)
#         print(result)
# ```
# 
# <b>Out [2]:</b>
# ```
# 2500.0
# 4250.0
# 3250.0
# 7000.0
# 3100.0
# ```

# %% [markdown]
# ## RESOLUÇÃO

# %%
dados = {
    'Crossfox': {'km': 35000, 'ano': 2005},
    'DS5': {'km': 17000, 'ano': 2015},
    'Fusca': {'km': 130000, 'ano': 1979},
    'Jetta': {'km': 56000, 'ano': 2011},
    'Passat': {'km': 62000, 'ano': 1999}
}

# %%
def km_media(dataset, ano_atual):
    for item in dataset.items():
      result = item[1]['km'] / (ano_atual - item[1]['ano'])
      print(result)

# %%
km_media(dados, 2019)

# %% [markdown]
# # 4.3 Definindo funções que retornam valores

# %% [markdown]
# ### Funções que retornam um valor
# 
# #### Formato padrão
# 
# ```
# def <nome>(<param_1>, <param_2>, ..., <param_n>):
#     <instruções>
#     return <resultado>
# ```

# %%
def media(lista):
  valor = sum(lista) / len(lista)
  return valor

# %%
media([1, 2, 3, 4, 5, 6, 7, 8])

# %%
resultado = media([1, 2, 3, 4, 5, 6, 7, 8])

# %%
resultado

# %% [markdown]
# ### Funções que retornam mais de um valor
# 
# #### Formato padrão
# 
# ```
# def <nome>(<param_1>, <param_2>, ..., <param_n>):
#     <instruções>
#     return (<resultado_1>, <resultado_2>, ..., <resultado_n>)
# ```

# %%
def media(lista):
  valor = sum(lista) / len(lista)
  return (valor, len(lista))

# %%
media([1, 2, 3, 4, 5, 6, 7, 8, 9])

# %%
resultado, n = media([1, 2, 3, 4, 5, 6, 7, 8, 9])

# %%
resultado

# %%
n

# %% [markdown]
# ## Melhorando a nossa função
# 
# No problema anterior, definimos uma função para obter a quilometragem média anual de cada veículo em um dataset. Precisamos melhorar um pouco a nossa função e obter valores que possam ser reutilizados em outras partes do nosso projeto.
# 
# Aprendemos em nosso último vídeo como criar funções que retornam valores, e é isso que precisamos para resolver este problema. A estrutura a seguir é a definição de uma função que calcula as quilometragens médias anuais de cada veículo e retorna um dicionário com os nomes dos veículos como chaves e as quilometragens médias como valores:
# 
# **In[1]**
# 
# ```
# dados = {
#     'Crossfox': {'km': 35000, 'ano': 2005},
#     'DS5': {'km': 17000, 'ano': 2015},
#     'Fusca': {'km': 130000, 'ano': 1979},
#     'Jetta': {'km': 56000, 'ano': 2011},
#     'Passat': {'km': 62000, 'ano': 1999}
# }
# ```
# 
# **In[2]**
# 
# ```
# def km_media(dataset, ano_atual):
#     result = {}
#     for item in dataset.items():
#         media = item[1]['km'] / (ano_atual - item[1]['ano'])
#         _________________________________        
#     ________________
# ```
# 
# **In[2]**
# 
# ```
# km_media(dados, 2019)
# ```
# 
# **Out[3]**
# 
# ```
# {'Crossfox': 2500.0,
#  'DS5': 4250.0,
#  'Fusca': 3250.0,
#  'Jetta': 7000.0,
#  'Passat': 3100.0}
# ```
# 

# %% [markdown]
# ## Resolução

# %%
dados = {
    'Crossfox': {'km': 35000, 'ano': 2005},
    'DS5': {'km': 17000, 'ano': 2015},
    'Fusca': {'km': 130000, 'ano': 1979},
    'Jetta': {'km': 56000, 'ano': 2011},
    'Passat': {'km': 62000, 'ano': 1999}
}

# %%
def km_media(dataset, ano_atual): # definição do nome da função + parametros a serem utilizados
  result = {} # declarando a variável de resultado
  for item in dataset.items():
    media = item[1]['km'] / (ano_atual - item[1]['ano'])
    result.update({item[0]: media})
  return result


# %%
km_media(dados, 2019)

# %% [markdown]
# ## Elaborando um pouco mais a nossa função
# 
# A nossa função `km_media()` já retorna valores que podem ser trabalhados em outras partes do nosso projeto. Uma elaboração extra, que também pode ser interessante, principalmente para a criação de DataFrames (próximas aulas), é a atualização do próprio input da função. Podemos fazer com que a nossa função retorne as informações do dicionário dados, incluindo as informações de quilometragem média anual.
# 
# A estrutura a seguir é a definição de uma função que calcula as quilometragens médias anuais de cada veículo, atualiza o dicionário de entrada e retorna este dicionário:
# 
# **In[1]**
# 
# ```
# dados = {
#     'Crossfox': {'km': 35000, 'ano': 2005},
#     'DS5': {'km': 17000, 'ano': 2015},
#     'Fusca': {'km': 130000, 'ano': 1979},
#     'Jetta': {'km': 56000, 'ano': 2011},
#     'Passat': {'km': 62000, 'ano': 1999}
# }
# ```
# 
# **In[2]**
# 
# ```
# def km_media(dataset, ano_atual):
#     result = {}
#     for item in dataset.items():
#         media = item[1]['km'] / (ano_atual - item[1]['ano'])
#         ____________________________________
#         ___________________________________
# 
#     return result
# ```
# 
# **In[3]**
# 
# ```
# km_media(dados, 2019)
# ```
# 
# **Out[3]**
# 
# ```
# {'Crossfox': {'km': 35000, 'ano': 2005, 'km_media': 2500.0},
#  'DS5': {'km': 17000, 'ano': 2015, 'km_media': 4250.0},
#  'Fusca': {'km': 130000, 'ano': 1979, 'km_media': 3250.0},
#  'Jetta': {'km': 56000, 'ano': 2011, 'km_media': 7000.0},
#  'Passat': {'km': 62000, 'ano': 1999, 'km_media': 3100.0}}
# ```

# %% [markdown]
# ## Resolução

# %%
dados = {
    'Crossfox': {'km': 35000, 'ano': 2005},
    'DS5': {'km': 17000, 'ano': 2015},
    'Fusca': {'km': 130000, 'ano': 1979},
    'Jetta': {'km': 56000, 'ano': 2011},
    'Passat': {'km': 62000, 'ano': 1999}
}

# %%
def km_media(dataset, ano_atual):
    result = {}
    for item in dataset.items():
        media = item[1]['km'] / (ano_atual - item[1]['ano'])
        item[1].update({ 'km_media': media })
        result.update({ item[0]: item[1] })
    return result

# %%
km_media(dados, 2023)

# %% [markdown]
# # <font color=green> 5. PANDAS BÁSICO
# ---
# 
# **versão: 0.25.2**
#   
# Pandas é uma ferramenta de manipulação de dados de alto nível, construída com base no pacote Numpy. O pacote pandas possui estruturas de dados bastante interessantes para manipulação de dados e por isso é muito utilizado por cientistas de dados.
# 
# 
# ## Estruturas de Dados
# 
# ### Series
# 
# Series são arrays unidimensionais rotulados capazes de armazenar qualquer tipo de dado. Os rótulos das linhas são chamados de **index**. A forma básica de criação de uma Series é a seguinte:
# 
# 
# ```
#     s = pd.Series(dados, index = index)
# ```
# 
# O argumento *dados* pode ser um dicionário, uma lista, um array Numpy ou uma constante.
# 
# ### DataFrames
# 
# DataFrame é uma estrutura de dados tabular bidimensional com rótulos nas linha e colunas. Como a Series, os DataFrames são capazes de armazenar qualquer tipo de dados.
# 
# 
# ```
#     df = pd.DataFrame(dados, index = index, columns = columns)
# ```
# 
# O argumento *dados* pode ser um dicionário, uma lista, um array Numpy, uma Series e outro DataFrame.
# 
# **Documentação:** https://pandas.pydata.org/pandas-docs/version/0.25/

# %% [markdown]
# # 5.1 Estruturas de dados

# %%
import pandas as pd

# %% [markdown]
# ### Criando uma Series a partir de uma lista

# %%
carros = ['Jetta Variant', 'Passat', 'Crossfox']
carros

# %%
pd.Series(carros)

# %% [markdown]
# ### Criando um DataFrame a partir de uma lista de dicionários

# %%
dados = [
    {'Nome': 'Jetta Variant', 'Motor': 'Motor 4.0 Turbo', 'Ano': 2003, 'Quilometragem': 44410.0, 'Zero_km': False, 'Valor': 88078.64},
    {'Nome': 'Passat', 'Motor': 'Motor Diesel', 'Ano': 1991, 'Quilometragem': 5712.0, 'Zero_km': False, 'Valor': 106161.94},
    {'Nome': 'Crossfox', 'Motor': 'Motor Diesel V8', 'Ano': 1990, 'Quilometragem': 37123.0, 'Zero_km': False, 'Valor': 72832.16}
]

# %%
dataset = pd.DataFrame(dados)

# %%
dataset

# %%
dataset[['Nome', 'Motor', 'Ano', 'Quilometragem', 'Valor','Zero_km']] ## para alterar a ordem das colunas, basta uttilizar esta entrada, colocando as colunas na ordem desejada.

# %% [markdown]
# ### Criando um DataFrame a partir de um dicionário

# %%
dados = {
    'Nome': ['Jetta Variant', 'Passat', 'Crossfox'],
    'Motor': ['Motor 4.0 Turbo', 'Motor Diesel', 'Motor Diesel V8'],
    'Ano': [2003, 1991, 1990],
    'Quilometragem': [44410.0, 5712.0, 37123.0],
    'Zero_km': [False, False, False],
    'Valor': [88078.64, 106161.94, 72832.16]
}

# %%
dataset = pd.DataFrame(dados)

# %%
dataset

# %% [markdown]
# ### Criando um DataFrame a partir de uma arquivo externo

# %%
dataset = pd.read_csv('/db.csv', sep = ';', index_col = 0)

# %%
dataset

# %% [markdown]
# # Criando Dataframes
# 
# Vimos no último vídeo que é possível criar DataFrames e Series a partir de várias fontes (arquivos externos, listas, dicionários, etc).
# 
# Na aula que falamos sobre funções, desenvolvemos em nossos exercícios uma função que recebia um dicionário com um conjunto de informações sobre veículos, e calculava a quilometragem média anual de cada veículo. Esta função retornava o conteúdo do dicionário de input da função, incluindo as informações sobre a quilometragem média:
# 
# **In[1]**
# 
# ```
# dados = {
#     'Crossfox': {'km': 35000, 'ano': 2005},
#     'DS5': {'km': 17000, 'ano': 2015},
#     'Fusca': {'km': 130000, 'ano': 1979},
#     'Jetta': {'km': 56000, 'ano': 2011},
#     'Passat': {'km': 62000, 'ano': 1999}
# }
# ```
# 
# **In[2]**
# 
# ```
# def km_media(dataset, ano_atual):
#     result = {}
#     for item in dataset.items():
#         media = item[1]['km'] / (ano_atual - item[1]['ano'])
#         item[1].update({ 'km_media': media })
#         result.update({ item[0]: item[1] })
# 
#     return result
# ```
# 
# **In[3]**
# 
# ```
# km_media(dados, 2019)
# ```
# 
# **Out[3]**
# 
# ```
# {'Crossfox': {'km': 35000, 'ano': 2005, 'km_media': 2500.0},
#  'DS5': {'km': 17000, 'ano': 2015, 'km_media': 4250.0},
#  'Fusca': {'km': 130000, 'ano': 1979, 'km_media': 3250.0},
#  'Jetta': {'km': 56000, 'ano': 2011, 'km_media': 7000.0},
#  'Passat': {'km': 62000, 'ano': 1999, 'km_media': 3100.0}}
# ```
# 
# Assinale a alternativa que mostra a forma correta de se criar uma `DataFrame` com o resultado obtido pela função acima. O `DataFrame` resultante deve ter a seguinte forma:
# 
# **Out[1]**
# ```
# 	          km	    ano	k   m_media
# Crossfox	35000.0	  2005.0	2500.0
# DS5	      17000.0	  2015.0	4250.0
# Fusca	    130000.0	1979.0	3250.0
# Jetta	    56000.0	  2011.0	7000.0
# Passat	  62000.0	  1999.0	3100.0
# ```
# 
# Dica: Para resolver esta questão, será necessário relembrar um recurso que aprendemos no curso anterior, quando falamos de _arrays_ Numpy. Este recurso também pode ser aplicado a `DataFrames` do `pandas`:
# 
# **ndarray.T**: _Retornar o array transposto, isto é, converte linhas em colunas e vice versa._
# 
# 

# %% [markdown]
# ## Resolução

# %%
dados = {
    'Crossfox': {'km': 35000, 'ano': 2005},
    'DS5': {'km': 17000, 'ano': 2015},
    'Fusca': {'km': 130000, 'ano': 1979},
    'Jetta': {'km': 56000, 'ano': 2011},
    'Passat': {'km': 62000, 'ano': 1999}
}

# %%
def km_media(dataset, ano_atual):
    result = {}
    for item in dataset.items():
        media = item[1]['km'] / (ano_atual - item[1]['ano'])
        item[1].update({ 'km_media': media })
        result.update({ item[0]: item[1] })

    return result

# %%
km_media(dados, 2019)

# %%
dataframe = pd.DataFrame(dados)

# %%
dataframe

# %%
import pandas as pd
carros = pd.DataFrame(km_media(dados, 2019)).T
carros

## A propriedade T, é uma forma de acessar o método transpose() do DataFrame.

# %% [markdown]
# # 5.2 Seleções com DataFrames

# %% [markdown]
# ### Selecionando colunas

# %%


# %%
dataset['Valor']

# %%
type(dataset['Valor'])

# %%
dataset[['Valor']]

# %%
type(dataset[['Valor']])

# %% [markdown]
# ### Selecionando linhas - [ i : j ]
# 
# <font color=red>**Observação:**</font> A indexação tem origem no zero e nos fatiamentos (*slices*) a linha com índice i é **incluída** e a linha com índice j **não é incluída** no resultado.

# %%
dataset[0:3]

# %% [markdown]
# ### Utilizando .loc para seleções
# 
# <font color=red>**Observação:**</font> Seleciona um grupo de linhas e colunas segundo os rótulos ou uma matriz booleana.

# %%
dataset.loc['Passat']

# %%
dataset.loc[['Passat', 'DS5']]

# %%
dataset.loc[['Passat', 'DS5'], ['Motor', 'Valor']]

# %%
dataset.loc[:, ['Motor', 'Valor']]

# %% [markdown]
# ### Utilizando .iloc para seleções
# 
# <font color=red>**Observação:**</font> Seleciona com base nos índices, ou seja, se baseia na posição das informações.

# %%
dataset.head()

# %%
dataset.iloc[[1]]

# %%
dataset.iloc[1:4]

# %%
dataset.iloc[1:4, [0, 5, 2]]

# %%
dataset.iloc[[1, 42, 22], [0,5, 2]]

# %%
dataset.iloc[:, [0,5, 2]]

# %% [markdown]
# ## Exercício

# %% [markdown]
# ### Utilizando .loc e .iloc para seleções

# %%
import pandas as pd

dados = {
    'Motor': ['Motor 4.0 Turbo', 'Motor Diesel', 'Motor Diesel V8', 'Motor 2.0', 'Motor 1.6'],
    'Ano': [2019, 2003, 1991, 2019, 1990],
    'Quilometragem': [0.0, 5712.0, 37123.0, 0.0, 120000.0],
    'Zero_km': [True, False, False, True, False],
    'Valor': [88000.0, 106000.0, 72000.0, 89000.0, 32000.0]
}

dataset = pd.DataFrame(dados, index = ['Jetta', 'Passat', 'Crossfox', 'DS5', 'Fusca'])

dataset

# %%
dataset.iloc[[1,3], [0,-1]]

# %%
dataset.loc[['Passat', 'DS5'], ['Motor', 'Valor']]

# %% [markdown]
# # 5.3 Queries com DataFrames

# %%
dataset = pd.read_csv('/db.csv', sep = ';', index_col = 0)

# %%
dataset.head()

# %%
dataset.Motor

# %%
select = dataset.Motor == 'Motor Diesel'

# %%
select

# %%
type(select)

# %%
dataset[select]

# %%
dataset[(dataset.Motor == 'Motor Diesel') & (dataset.Zero_km == True)]

# %%
(dataset.Motor == 'Motor Diesel') & (dataset.Zero_km == True)

# %% [markdown]
# ### Utilizando o método query

# %%
dataset.query('Motor == "Motor Diesel" and Zero_km == True')

# %% [markdown]
# ## Exercício

# %% [markdown]
# ### Realizando consultas em um DataFrame

# %%
import pandas as pd

dados = {
    'Motor': ['Motor 4.0 Turbo', 'Motor Diesel', 'Motor Diesel V8', 'Motor Diesel', 'Motor 1.6'],
    'Ano': [2019, 2003, 1991, 2019, 1990],
    'Quilometragem': [0.0, 5712.0, 37123.0, 0.0, 120000.0],
    'Zero_km': [True, False, False, True, False],
    'Valor': [88000.0, 106000.0, 72000.0, 89000.0, 32000.0]
}

dataset = pd.DataFrame(dados, index = ['Jetta', 'Passat', 'Crossfox', 'DS5', 'Fusca'])

# %% [markdown]
# # 5.4 Iterando com DataFrames

# %%
dataset = pd.read_csv('/db.csv', sep = ';', index_col = 0)

# %%
dataset.head()

# %%
for item in dataset:
  print(item)

# %%
for index, row in dataset.iterrows():
  if (2019 - row['Ano'] != 0):
    dataset.loc[index, 'Km_media'] = row['Quilometragem'] / (2019 - row['Ano'])
  else:
    dataset.loc[index, 'Km_media'] = 0

dataset

# %% [markdown]
# # 5.5 Tratamento de dados

# %%
dataset.head()

# %%
dataset.info()

# %%
dataset.Quilometragem.isna()

# %%
dataset[dataset.Quilometragem.isna()]

# %%
dataset.fillna(0, inplace = True)

# %%
dataset

# %%
dataset.query("Zero_km == True")

# %%
dataset = pd.read_csv('/db.csv', sep = ';')

# %%
dataset

# %%
dataset.dropna(subset = ['Quilometragem'], inplace = True)

# %%
dataset


