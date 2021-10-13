#!/usr/bin/env python
# coding: utf-8

# In[31]:


'''Desafio:
    
Você trabalha em uma empresa de telecom e tem clientes de vários serviços diferentes, 
entre os principais: internet e telefone.
    
O problema é que, analisando o histórico dos clientes dos últimos anos, você percebeu que a 
empresa está com Churn de mais de 26% dos clientes.
  
Isso representa uma perda de milhões para a empresa.

O que a empresa precisa fazer para resolver isso?
    
Base de Dados: 
https://drive.google.com/drive/folders/1T7D0BlWkNuy_MDpUHuBG44kT80EmRYIs?usp=sharing <br>

Link Original do Kaggle: 
https://www.kaggle.com/radmirzosimov/telecom-users-dataset'''


# In[32]:


# Passo 1: Entender qual é o problema
import pandas as pd

tabela = pd.read_csv('telecom_users.csv')

# Passo 2: Importar a base de dados
# - Visualizar a base de dados
# - Descobrir os erros da base de dados

tabela = tabela.drop("Unnamed: 0",axis=1)
display(tabela)


# In[33]:


# Passo 3: Tratamento de dados
# - Valores que estão reconhecidos de forma errada
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")

# - Valores vazios
# deletando as colunas vazias
tabela = tabela.dropna(how='all',axis=1)

# deletando linhas vazias
tabela = tabela.dropna(how='any',axis=0)

print(tabela.info())


# In[34]:


# Passo 4: Análise inicial
# Como estão os nossos cancelamentos?
print(tabela["Churn"].value_counts())
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))


# In[35]:


# Passo 5: Análise mais completa
# comparar cada coluna da minha tabela com a coluna de cancelamento
import plotly.express as px

# etapa 1: criar o gráfico
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x = coluna, color="Churn")
    # etapa2: exibir o gráfico
    grafico.show()


# In[36]:


'''Conclusões:
    
- Clientes com contrato mensal tem muito mais chance de cancelar
    - Podemos fazer promoções para o cliente ir para o contrato anual
    
- Familias maiores tendem a cancelar menos do que familias menores
    - Podemos fazer promoçoes pra pessoa pegar uma linha adicional de telefone
    
- MesesComoCliente baixos tem MUITO cancelamento.Clientes com pouco tempo como cliente tendem 
a cancelar muito.
    - A primeira experiência do cliente na operadora pode ser ruim
    - Talvez a captação de clientes ta trazendo clientes desqualificados
    - Ideia: a gente pode criar incentivo pro cliente ficar mais tempo 
- Quanto mais serviços o cliente tem , menos chance dele cancelar
    - Podemos fazer promoções com mais serviços pro cliente
    
- Tem alguma coisa no nosso serviço de Fibra que ta fazendo os clientes cancelarem
    - Agir sobre a fibra
    
- Clientes no Boleto tem muito mais chance de cancelar, temos que fazer uma ação para eles mudarem pra outra fomra de pagamento.
'''


# In[ ]:




