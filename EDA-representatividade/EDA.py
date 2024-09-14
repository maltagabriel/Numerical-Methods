# Desafio Técnico F1rst
# ----------------------
# ---- Parte 03 --------
# ----------------------
# Gabriel Nogueira Malta
# ----------------------

import math
import pandas as pd
import numpy as np
import spacy
from nltk.tokenize import sent_tokenize
import matplotlib.pyplot as plt

nlp = spacy.load("en_core_web_sm")

def CountNaN(df):
    # Essa função conta quantos valores NaN existem em uma coluna e encontra qual é a coluna com mais dados faltantes
    NaN_in_Column = []
    for c in range(df.shape[1]):
        NaN_in_Column.append(df.iloc[:,c].isnull().sum())
    max_NaN = super.columns[NaN_in_Column.index(max(NaN_in_Column))]

    return [NaN_in_Column, max_NaN]

def CountBool(lst):
    # Essa função soma valores booleanos em uma lista
    return sum(bool(x) for x in lst)

def CountValues(column):
    # Essa função toma uma coluna (de um DataFrame) e retorna uma lista contendo os valores presentes na coluna e quantas vezes tais valores se repetem
    values = []
    values_list = []
    for obj in column:
        if obj not in values_list and str(obj) != 'nan':
            values_list.append((obj))

    values_counted = []
    for obj in values_list:
        values_counted.append(column.value_counts()[obj])

    for i in range(len(values_list)):
        values.append([values_list[i], values_counted[i]])

    return(values)

def CountInList(lista, valor):
    count = 0
    for elemento in lista:
        if (elemento == valor):
            count = count + 1
    return count

super = pd.read_csv('archive/superheroes_nlp_dataset.csv')
total_heroes = super.shape[0]

creators_counted_and_listed = CountValues(super['creator'])

# ----- COR DE PELE ------
skin_color_counted_and_listed = CountValues(super['skin_color']) #contamos aqui qunatos heróis de cada cor de pele aparecem no nosso banco de dados
informacao_mais_defasada = CountNaN(super) #aqui constatamos que os dados de cor de pele são os mais faltantes no nosso banco

#daqui em diante calculamos os scores médios de heróis de pele preta e heróis de pele branca para compará-los em um gráfico
black_heroes = []
white_heroes = []
for i in range(total_heroes):
    if super['skin_color'].values[i] == 'Black':
        black_heroes.append(i)
    elif super['skin_color'].values[i] == 'White':
        white_heroes.append(i)

black_intelligence_list = []
black_strength_list = []
black_speed_list = []
black_durability_list = []
black_power_list = []
black_combat_list = []

for index in black_heroes:
    black_intelligence_list.append(super['intelligence_score'].values[index])
    black_strength_list.append((super['strength_score'].values[index]))
    black_speed_list.append((super['speed_score'].values[index]))
    black_durability_list.append((super['durability_score'].values[index]))
    black_power_list.append((super['power_score'].values[index]))
    black_combat_list.append((super['combat_score'].values[index]))

white_intelligence_list = []
white_strength_list = []
white_speed_list = []
white_durability_list = []
white_power_list = []
white_combat_list = []

for index in white_heroes:
    white_intelligence_list.append(super['intelligence_score'].values[index])
    white_strength_list.append((super['strength_score'].values[index]))
    white_speed_list.append((super['speed_score'].values[index]))
    white_durability_list.append((super['durability_score'].values[index]))
    white_power_list.append((super['power_score'].values[index]))
    white_combat_list.append((super['combat_score'].values[index]))

black_intelligence_mean = np.mean(black_intelligence_list),
black_strength_mean = np.mean(black_strength_list),
black_speed_mean = np.mean(black_speed_list),
black_durability_mean = np.mean(black_durability_list),
black_power_mean = np.mean(black_power_list),
black_combat_mean = np.mean(black_combat_list)
black_means = [black_intelligence_mean, black_strength_mean,black_speed_mean,black_durability_mean,black_power_mean,black_combat_mean]

white_intelligence_mean = np.mean(white_intelligence_list)
white_strength_mean = np.mean(white_strength_list)
white_speed_mean = np.mean(white_speed_list)
white_durability_mean = np.mean(white_durability_list)
white_power_mean = np.mean(white_power_list)
white_combat_mean = np.mean(white_combat_list)
white_means = [white_intelligence_mean, white_strength_mean, white_speed_mean, white_durability_mean, white_power_mean,white_combat_mean]

#imprimimos gráficos comparativos entre heróis de pele preta e branca
barwidth = 0.2
plt.figure(figsize=(10,5))
r1=np.arange(len(black_means))
r2=[x+barwidth for x in r1]
plt.bar(r1,black_means, color='#A52A2A', width = barwidth, label='Heróis de pele preta')
plt.bar(r2, white_means, color='#FAEBD7', width=barwidth, label='Heróis de pele branca')
plt.xlabel('Médias dos scores')
plt.xticks([r+barwidth for r in range(len(black_means))],['Inteligência', 'Força', 'Velocidade', 'Durabilidade', 'Poder', 'Combate'])
plt.ylabel('Score médio')
plt.title('Médias de cada score de heróis de pele preta e branca')
plt.legend()
plt.show()

# imprimimos um arquivo txt com a quantidade total de heróis de cada cor de pele e também a qunatidade total de dados faltantes em cada uma das colunas do nosso DataFrame, constatando que a cor de pele é o dado mais faltoso
with open('Subrepresentação de heróis de pele preta.txt', 'w') as f:
    dado1 = str(skin_color_counted_and_listed)+"\n"
    dado2 = str(informacao_mais_defasada)
    f.write(dado1+dado2)
    f.close()

#--------- GÊNERO ------------
gender_counted_and_listed = CountValues(super['gender']) #aqui contamos quantos heróis e heroínas existem no nosso banco de dados

#aqui calculamos scores médios entre heróis e heroínas para compará-los em gráfico
women_heroes = []
men_heroes = []
for i in range(total_heroes):
    if super['gender'].values[i] == 'Female':
        women_heroes.append(i)
    elif super['gender'].values[i] == 'Male':
        men_heroes.append(i)

women_intelligence_list = []
women_strength_list = []
women_speed_list = []
women_durability_list = []
women_power_list = []
women_combat_list = []

for index in women_heroes:
    women_intelligence_list.append(super['intelligence_score'].values[index])
    women_strength_list.append((super['strength_score'].values[index]))
    women_speed_list.append((super['speed_score'].values[index]))
    women_durability_list.append((super['durability_score'].values[index]))
    women_power_list.append((super['power_score'].values[index]))
    women_combat_list.append((super['combat_score'].values[index]))

men_intelligence_list = []
men_strength_list = []
men_speed_list = []
men_durability_list = []
men_power_list = []
men_combat_list = []

for index in white_heroes:
    men_intelligence_list.append(super['intelligence_score'].values[index])
    men_strength_list.append((super['strength_score'].values[index]))
    men_speed_list.append((super['speed_score'].values[index]))
    men_durability_list.append((super['durability_score'].values[index]))
    men_power_list.append((super['power_score'].values[index]))
    men_combat_list.append((super['combat_score'].values[index]))

women_intelligence_mean = np.mean(women_intelligence_list)
women_strength_mean = np.mean(women_strength_list)
women_speed_mean = np.mean(women_speed_list)
women_durability_mean = np.mean(women_durability_list)
women_power_mean = np.mean(women_power_list)
women_combat_mean = np.mean(women_combat_list)
women_means = [women_intelligence_mean, women_strength_mean,women_speed_mean,women_durability_mean,women_power_mean,women_combat_mean]

men_intelligence_mean = np.mean(men_intelligence_list)
men_strength_mean = np.mean(men_strength_list)
men_speed_mean = np.mean(men_speed_list)
men_durability_mean = np.mean(men_durability_list)
men_power_mean = np.mean(men_power_list)
men_combat_mean = np.mean(men_combat_list)
men_means = [men_intelligence_mean, men_strength_mean,men_speed_mean,men_durability_mean,men_power_mean,men_combat_mean]

#Gráfico de barras comparativo entre scores de heróis e heroínas
barwidth = 0.2
plt.figure(figsize=(10,5))
r1=np.arange(len(women_means))
r2=[x+barwidth for x in r1]
plt.bar(r1,women_means, color='#8601AF', width = barwidth, label='Heroínas')
plt.bar(r2, men_means, color='#40E0D0', width=barwidth, label='Heróis')
plt.xlabel('Médias dos scores')
plt.xticks([r+barwidth for r in range(len(women_means))],['Inteligência', 'Força', 'Velocidade', 'Durabilidade', 'Poder', 'Combate'])
plt.ylabel('Score médio')
plt.title('Médias de cada score de heróis e heroínas')
plt.legend()
plt.show()

#Aqui analisamos a evolução histórica do surgimento de novas heroínas
women_f1rst_appearance_year = {}
for i in range(len(women_heroes)):
    women_heroes_f1rst_doc = nlp(str(super['first_appearance'][women_heroes[i]]))
    women_heroes_f1rst_num = [token.lemma_ for token in women_heroes_f1rst_doc if token.is_digit]
    women_heroes_f1rst_int = [int(num) for num in women_heroes_f1rst_num]
    for number in women_heroes_f1rst_int:
        if number < 2022 and number >1900:
            women_f1rst_appearance_year[i] = number

years_sorted = sorted(list(women_f1rst_appearance_year.values()))

inicio = math.floor(years_sorted[0]/10)*10
fim = math.floor(years_sorted[len(years_sorted)-1]/10)*10
decades = []
for i in range(int((fim-inicio)/10)+1):
    decades.append(inicio+i*10)

women_f1st_appearance_decade = np.zeros(len(decades))
for year in years_sorted:
    for i in range(len(decades)):
        if math.floor(year/10)*10 == decades[i]:
            women_f1st_appearance_decade[i] = women_f1st_appearance_decade[i]+1

#Aqui imprimimos um gráfico da evolução histórica do surgimento de novas heroínas
plt.plot(decades,women_f1st_appearance_decade)
plt.xlabel('Década')
plt.ylabel('Quantidade de heroínas')
plt.title('Quantidade de super-heroínas aparecendo pela primeira vez a cada década')
plt.show()

#aqui imprimimos um arquivo de texto com a contagem de heróis e heroínas
with open('Subrepresentação feminina.txt', 'w') as f:
    dado1 = str(gender_counted_and_listed)+"\n"
    f.write(dado1)
    f.close()

# ----- SEXUALIDADE ----------
# Procurando referências a heróis e heroínas LGBT
sexualidade = ['lesbian', 'gay', 'bissexual', 'transexual', 'LGBT', 'homossexual', 'queer']
LGBT_heroes = {}
encontrar = []
LGBT_history_tokenized = []
for sex in sexualidade:
    LGBT_heroes[sex] = []
    mention_sex = super.apply(lambda row: row.astype(str).str.contains(sex).any(), axis=1)
    encontrar.append(CountBool(mention_sex))
    for i in range(len(mention_sex)):
        if mention_sex[i] == True:
            LGBT_heroes[sex].append([i, super.iloc[i,0]])
            doc = nlp(super.iloc[i,4])
            LGBT_history_tokenized.append([i, sent_tokenize(super.iloc[i,4])])

# Agora que encontramos menções às palavras gay e lesbian (já que foram as únicas encontradas, vamos encontrar os contextos referentes às menções e confirmarmos ou não a informação
# de que tais heróis/heroínas são LGBT

mentions = []
title = "Menções à palavra 'gay' e 'lesbian' em seus devidos contextos: \n"
mentions.append(title)
for LGBT_hero_history in LGBT_history_tokenized:
    for sentence in LGBT_hero_history[1]:
        doc_sentence = nlp(sentence)
        sentence_tokens = [token.orth_ for token in doc_sentence if token.is_alpha]
        if 'gay' in sentence_tokens:
            mentions.append(super.iloc[LGBT_hero_history[0],0] + ": " + sentence + "\n")
        if 'lesbian' in sentence_tokens:
            mentions.append(super.iloc[LGBT_hero_history[0],0] + ": " + sentence + "\n")

#imprimimos um arquivo de texto com as sentenças onde aparecem as palavras "gay" e "lesbian" para que possam ser analisadas
with open('Contextos_gay_lesbian.txt', 'w') as f:
    for mention in mentions:
        f.write(mention)
    f.close()

# Com os devidos contextos podemos ver que a menção à palavra 'lesbian' na história de Morph não se trata do herói, mas de Sunfire. O mesmo caso acontece na história de Two-Face onde a menção à palavra 'lesbian'
# se refere à outra personagem. Mas Batwoman V e Silk Spectre são de fato lésbicas, como fica evidente, respectivamente, nos trechos: "When the relationship was discovered, however, Kate chose to come out as a lesbian";
# "she was expelled from the group simply because she was a lesbian".

# Da mesma forma conferimos a informação da sexualidade dos heróis cuja história contém a palavra 'gay'. Captain Stingaree e The Ray (CW) são de fato gays como fica claro nos trechos presentes em suas histórias:
# "Captain Stingaree was later revealed to be gay, and in a relationship with The Cavalier."; e "Ray decided to come out as gay to his parents before departing to Earth-X to face Overgirl.". Por outro lado, a história
# de Silk Spectre contém a palvra gay mas em referência a outro personagem. A menção à palavra 'gay' na história de Kick-Ass é para contar quando o herói se passou por gay para se aproximar da garota que era interessado
# e na história de Northstar para descrever seus inimigos que eram anti-mutante e anti-gay.