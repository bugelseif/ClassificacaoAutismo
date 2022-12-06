import pandas as pd
import numpy as np
import seaborn as sns
import csv
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import sklearn.metrics




dados = pd.read_csv('Dados Autismo.csv')
dados.drop(['id'], axis = 1, inplace = True)
le = LabelEncoder()
# dados['GrauAustismo']=le.fit_transform(dados['GrauAustismo'])
print("Quantidade de colunas: ",dados.shape[1])
dados.head(10)





corr_matrix = dados.corr().abs() 
mask = np.triu(np.ones_like(corr_matrix, dtype = bool))
tri_df = corr_matrix.mask(mask)
to_drop = [x for x in tri_df.columns if any(tri_df[x] > 0.92)]
dados2 = dados.drop(to_drop, axis = 1)
print("Quantidade de colunas do dataframe original: ",dados.shape[1])
print("Quantidade de colunas do dataframe reduzido: ",dados2.shape[1])






print(dados2["GrauAutismo"])

X = dados2.drop(["GrauAutismo"] ,axis="columns")
y = dados2['GrauAutismo']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42, shuffle=True)
modelo = linear_model.LogisticRegression()
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)
a = modelo.coef_
b =  modelo.intercept_
print("Coeficientes da reta: \n")
print("a = ",a)
print("b = ",b)
acc = accuracy_score(y_test, y_pred)
print("Acurácia: ", acc)
matriz = confusion_matrix(y_test, y_pred)
print(matriz)
relatorio = classification_report(y_test, y_pred)
print(relatorio)






X = dados2.drop(["GrauAutismo"] ,axis="columns")
y = dados2['GrauAutismo']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42, shuffle=True)
modelo = DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=0)
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print("Acurácia: ", acc)
matriz = confusion_matrix(y_test, y_pred)
print(matriz)
relatorio = classification_report(y_test, y_pred)
print(relatorio)





# X = dados2.drop(["GrauAutismo"] ,axis="columns")
# y = dados2['GrauAutismo']
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42, shuffle=True)
# modelo = DecisionTreeClassifier(criterion='entropy', max_depth=5, random_state=0)
# modelo.fit(X_train, y_train)
# y_pred = modelo.predict(X_test)
# acc = accuracy_score(y_test, y_pred)
# print("Acurácia: ", acc)
# matriz = confusion_matrix(y_test, y_pred)
# print(matriz)
# relatorio = classification_report(y_test, y_pred)
# print(relatorio)





def teste(dados):
    
   
   
    with open('example.csv', 'w', newline='',encoding="utf8") as file: #escreve os dados em um arquivo csv
        writer = csv.writer(file)
        #foram retirados as tabelas para id e GrauAutismo
        termos ="genero@Dificuldades de comunicação?@Comportamentos repetitivos interação ?@A criança  interage socialmente  ?@Presença ou não de fala ?@Não olha nos olhos mesmo quando alguém fala com ela (e) ?@Risos e gargalhadas fora de hora, como por exemplo durante um velório ou um casamento   ?@Não gosta de carinho ou afeto e por isso não se deixa abraçar ou beijar   ?@Dificuldade em relacionar-se com outras crianças    ?@Repetir as mesmas coisas, sons e palavras; brincar 3 com os mesmos brinquedos   ?@ Sabe falar, mas prefere não se comunicar  ?@Quando fala, a comunicação é monótona ?@Repete uma pergunta várias vezes seguidas sem se importar se está chateando os outros  ?@Tem 3 a mesma expressão no rosto e não entende gestos e expressões faciais dos outros   ?@Não tem medo de situações perigosas, como por exemplo atravessar a rua sem olhar para os carros ? (Desconsiderando Bipolaridade)   @Olha 3 na mesma direção como se estivesse parado no tempo?@Fica se balançando para frente e para trás por vários minutos ou horas ou torcer as mãos ou os dedos constantemente  ?@Dificuldade a se adaptar a uma nova rotina ficando agitado ?@Fica extremamente agitado quando está em público ou em ambientes barulhentos  ?"
        cabecalho = termos.split("@")
        writer.writerow(cabecalho) # cabeçalho
        writer.writerow(dados.encode("utf8")) # dados
    arquivo = pd.read_csv('example.csv') # lê os dados do arquivo csv que foi escrito
   
    lista_numpy = modelo.predict(arquivo) # utiliza a árovere e retorna um resultado
    lista_resultado = lista_numpy.tolist() # convertendo o resultado que está como listanumpy em lista
    if lista_resultado[0]==0: #o resultado retornado é 0 para negativo e 1 para positivo nesse exemplo
      
            resposta = 'Não Autista'
    elif  lista_resultado[0]==1:
            resposta = 'Leve'
            
    elif  lista_resultado[0]==2:
            resposta = 'Moderado'
            
    elif  lista_resultado[0]==3:
            resposta = 'Severo'
    else:
            resposta = 'erro'
    
    return resposta

