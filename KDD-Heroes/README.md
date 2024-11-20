<h1>Análise dos Dados</h1>

Compartilho um exercício de EDA onde avaliei a representação das comunidades feminina, negra e LGBT no banco de dados do Kaggle contedo 1450 heróis e heroínas. O conjunto dos dados está disponível no endereço:
\href{https://www.kaggle.com/datasets/jonathanbesomi/superheroes-nlp-dataset}{https://www.kaggle.com/datasets/jonathanbesomi/superheroes-nlp-dataset}

Observamos a questão da representatividade com foco em gênero, cor de pele e sexualidade, para cada um dos três aspectos foram utilizadas abordagens diferentes de análise.

<h2>Cor de Pele</h2>
Quanto à cor de pele, percebi que é o dado mais defasado do banco de dados, sendo essa informação ausente na descrição de 1277 heróis (o segundo dado mais faltoso tem pouco mais da metade de desinformações: 662), lembrando que o total são 1450 heróis. 

Também percebi que existem, no nosso banco de dados, mais heróis de pele azul (23), vermelha (15), verde (30) e branca (30) do que heróis de pele preta (13). O que considero ser um retrato da subrrepresentação da população negra nas mídias convencionais.

A partir dos dados dos scores, elaborei um gráfico comparativo entre scores médios de heróis de pele preta e heróis de pele branca. Me chamou a atenção o fato de que em média os heróis negros são mais fortes porém menos inteligentes do que os heróis brancos, acredito que tal dado corrobora com o estereótipo do negro como ser animalesco e bruto. As médias foram calculadas usando a biblioteca Numpy e os gráficos elaborado com a biblioteca Matplotlib.

<h2>Gênero</h2>
 Quanto ao gênero, também existe uma subrrepresentação feminina com apenas 335 heroínas no total de 1450.
 
 Além disso os scores médios são bem discrepantes, como podemos ver no gráfico a seguir:

 Também elaborei um gráfico para visualizar a evolução histórica da participação feminina no conjunto de heróis e notei que a partir de 1970 começam a surgir mais novas heroínas:
 
 Os dados do surgimento de novas heroínas ao longo do tempo foi captado através da busca por numerais maiores que 1900 e menores que 2022 presentes na coluna "first\_appearance" do banco de dados. Tal busca se deu através da biblioteca Spacy. Entre as 335 heroínas, 88 tinham o ano da primeira aparição.

<h2>Sexualidade</h3>
 Para analisar a sexualidade dos heróis e heroínas, procurei por algumas palavras-chave nas histórias pessoais dos heróis, encontrando menções às palavras "gay" e "lesbian", a partir das menções e de seus respectivos contextos, encontrei 2 heróis gays: Captain Stingaree e The Ray (CW) e duas heroínas lésbicas: Batwoman V e Silk Spectre. A busca textual foi realizada inicialmente usando o método .apply do Pandas com as palavras-chave: lesbian, gay, bissexual, transexual, LGBT, homossexual, queer. Foram encontradas apenas menções aos termos lesbian e gay. 
 
 Usando o sent\_tokenize da biblioteca NLTK de Programação de Lingaugem Natural, encontrei os contextos onde apareceram os termos citados e imprimi um arquivo de texto com tais sentenças, para analisá-las e entender como era feita a referência.
 
 Com os devidos contextos pude ver que a menção à palavra 'lesbian' na história de Morph não se trata do herói, mas de Sunfire. O mesmo caso acontece na história de Two-Face onde a menção à palavra 'lesbian' se refere à outra personagem. Mas Batwoman V e Silk Spectre são de fato lésbicas, como fica evidente, respectivamente, nos trechos: "When the relationship was discovered, however, Kate chose to come out as a lesbian";
 "she was expelled from the group simply because she was a lesbian".

Da mesma forma conferimos a informação da sexualidade dos heróis cuja história contém a palavra 'gay'. Captain Stingaree e The Ray (CW) são de fato gays como fica claro nos trechos presentes em suas histórias:
"Captain Stingaree was later revealed to be gay, and in a relationship with The Cavalier."; e "Ray decided to come out as gay to his parents before departing to Earth-X to face Overgirl.". Por outro lado, a história
de Silk Spectre contém a palvra gay mas em referência a outro personagem. A menção à palavra 'gay' na história de Kick-Ass é para contar quando o herói se passou por gay para se aproximar da garota que era interessado
# e na história de Northstar para descrever seus inimigos que eram anti-mutante e anti-gay.
 
Apenas 4 heróis LGBT num banco de 1450 confirma que há uma subrrepresentação da comunidade no campo das mídias de heróis.