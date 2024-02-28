# conferir indicadores disponíveis no dataimesc a partir do front-end

import requests as rq
from bs4 import BeautifulSoup
import pandas as pd

# gerando dict vazio para inserir as informações do site
df = {'indice':[],'titulo':[]}

# dentro do "range" definir intervalo de séries que se deseja encontrar
# obs: segundo número do parâmetro deve ser adicionado +1 para gerar corretamente
for i in range(1,11):
    url = 'http://dataimesc.imesc.ma.gov.br/series/'+str(i)+'/show'
    reqs = rq.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    for title in soup.find_all('h2',{'class':'p-2 title'}):
        df['indice'].append(i)
        df['titulo'].append(title.get_text())

data = pd.DataFrame(df)
print(data)

# descomentar abaixo caso deseje exportar para excel
# import
# data.to_excel('indicadores_dataimesc.xlsx',index=False)