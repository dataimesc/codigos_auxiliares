import requests as rq
import pandas as pd

series=[i for i in range(1,10)]

for serie in series:
    try:
        requi=rq.get(f'http://dataimesc.imesc.ma.gov.br/getData?id={serie}&scope=4&from=2010&to=2021')
        requi=requi.json()
        requi_series=requi["values"]
        mat=pd.DataFrame(requi_series).transpose()
        mat=mat.reset_index()
        mat.insert(1, "nivel", 0)
        mat.loc[(mat['index']=='2100055'), ['nivel']] = 24
        mat.loc[(mat['index']=='2100105'), ['nivel']] = 7
        mat.loc[(mat['index']=='2100154'), ['nivel']] = 13
        mat.loc[(mat['index']=='2100204'), ['nivel']] = 20
        mat.loc[(mat['index']=='2100303'), ['nivel']] = 32
        mat.loc[(mat['index']=='2100402'), ['nivel']] = 17
        mat.loc[(mat['index']=='2100436'), ['nivel']] = 25
        mat.loc[(mat['index']=='2100477'), ['nivel']] = 21
        mat.loc[(mat['index']=='2100501'), ['nivel']] = 27
        mat.loc[(mat['index']=='2100550'), ['nivel']] = 15
        mat.loc[(mat['index']=='2100600'), ['nivel']] = 23
        mat.loc[(mat['index']=='2100709'), ['nivel']] = 10
        mat.loc[(mat['index']=='2100808'), ['nivel']] = 7
        mat.loc[(mat['index']=='2100832'), ['nivel']] = 16
        mat.loc[(mat['index']=='2100873'), ['nivel']] = 8
        mat.loc[(mat['index']=='2100907'), ['nivel']] = 13
        mat.loc[(mat['index']=='2100956'), ['nivel']] = 5
        mat.loc[(mat['index']=='2101004'), ['nivel']] = 26
        mat.loc[(mat['index']=='2101103'), ['nivel']] = 11
        mat.loc[(mat['index']=='2101202'), ['nivel']] = 17
        mat.loc[(mat['index']=='2101251'), ['nivel']] = 11
        mat.loc[(mat['index']=='2101301'), ['nivel']] = 16
        mat.loc[(mat['index']=='2101350'), ['nivel']] = 1
        mat.loc[(mat['index']=='2101400'), ['nivel']] = 27
        mat.loc[(mat['index']=='2101509'), ['nivel']] = 22
        mat.loc[(mat['index']=='2101608'), ['nivel']] = 28
        mat.loc[(mat['index']=='2101707'), ['nivel']] = 31
        mat.loc[(mat['index']=='2101731'), ['nivel']] = 7
        mat.loc[(mat['index']=='2101772'), ['nivel']] = 21
        mat.loc[(mat['index']=='2101806'), ['nivel']] = 9
        mat.loc[(mat['index']=='2101905'), ['nivel']] = 20
        mat.loc[(mat['index']=='2101939'), ['nivel']] = 18
        mat.loc[(mat['index']=='2101970'), ['nivel']] = 12
        mat.loc[(mat['index']=='2102002'), ['nivel']] = 21
        mat.loc[(mat['index']=='2102036'), ['nivel']] = 24
        mat.loc[(mat['index']=='2102077'), ['nivel']] = 17
        mat.loc[(mat['index']=='2102101'), ['nivel']] = 13
        mat.loc[(mat['index']=='2102150'), ['nivel']] = 17
        mat.loc[(mat['index']=='2102200'), ['nivel']] = 7
        mat.loc[(mat['index']=='2102309'), ['nivel']] = 6
        mat.loc[(mat['index']=='2102325'), ['nivel']] = 24
        mat.loc[(mat['index']=='2102358'), ['nivel']] = 23
        mat.loc[(mat['index']=='2102374'), ['nivel']] = 11
        mat.loc[(mat['index']=='2102408'), ['nivel']] = 1
        mat.loc[(mat['index']=='2102507'), ['nivel']] = 30
        mat.loc[(mat['index']=='2102556'), ['nivel']] = 2
        mat.loc[(mat['index']=='2102606'), ['nivel']] = 15
        mat.loc[(mat['index']=='2102705'), ['nivel']] = 26
        mat.loc[(mat['index']=='2102754'), ['nivel']] = 14
        mat.loc[(mat['index']=='2102804'), ['nivel']] = 2
        mat.loc[(mat['index']=='2102903'), ['nivel']] = 15
        mat.loc[(mat['index']=='2103000'), ['nivel']] = 32
        mat.loc[(mat['index']=='2103109'), ['nivel']] = 16
        mat.loc[(mat['index']=='2103125'), ['nivel']] = 16
        mat.loc[(mat['index']=='2103158'), ['nivel']] = 12
        mat.loc[(mat['index']=='2103174'), ['nivel']] = 12
        mat.loc[(mat['index']=='2103208'), ['nivel']] = 7
        mat.loc[(mat['index']=='2103257'), ['nivel']] = 24
        mat.loc[(mat['index']=='2103307'), ['nivel']] = 25
        mat.loc[(mat['index']=='2103406'), ['nivel']] = 32
        mat.loc[(mat['index']=='2103505'), ['nivel']] = 6
        mat.loc[(mat['index']=='2103554'), ['nivel']] = 17
        mat.loc[(mat['index']=='2103604'), ['nivel']] = 25
        mat.loc[(mat['index']=='2103703'), ['nivel']] = 16
        mat.loc[(mat['index']=='2103752'), ['nivel']] = 23
        mat.loc[(mat['index']=='2103802'), ['nivel']] = 14
        mat.loc[(mat['index']=='2103901'), ['nivel']] = 32
        mat.loc[(mat['index']=='2104008'), ['nivel']] = 18
        mat.loc[(mat['index']=='2104057'), ['nivel']] = 2
        mat.loc[(mat['index']=='2104073'), ['nivel']] = 2
        mat.loc[(mat['index']=='2104081'), ['nivel']] = 28
        mat.loc[(mat['index']=='2104099'), ['nivel']] = 5
        mat.loc[(mat['index']=='2104107'), ['nivel']] = 27
        mat.loc[(mat['index']=='2104206'), ['nivel']] = 6
        mat.loc[(mat['index']=='2104305'), ['nivel']] = 15
        mat.loc[(mat['index']=='2104404'), ['nivel']] = 14
        mat.loc[(mat['index']=='2104503'), ['nivel']] = 14
        mat.loc[(mat['index']=='2104552'), ['nivel']] = 23
        mat.loc[(mat['index']=='2104602'), ['nivel']] = 4
        mat.loc[(mat['index']=='2104628'), ['nivel']] = 4
        mat.loc[(mat['index']=='2104651'), ['nivel']] = 8
        mat.loc[(mat['index']=='2104677'), ['nivel']] = 12
        mat.loc[(mat['index']=='2104701'), ['nivel']] = 4
        mat.loc[(mat['index']=='2104800'), ['nivel']] = 5
        mat.loc[(mat['index']=='2104909'), ['nivel']] = 16
        mat.loc[(mat['index']=='2105005'), ['nivel']] = 31
        mat.loc[(mat['index']=='2105104'), ['nivel']] = 11
        mat.loc[(mat['index']=='2105153'), ['nivel']] = 21
        mat.loc[(mat['index']=='2105203'), ['nivel']] = 18
        mat.loc[(mat['index']=='2105302'), ['nivel']] = 23
        mat.loc[(mat['index']=='2105351'), ['nivel']] = 5
        mat.loc[(mat['index']=='2105401'), ['nivel']] = 10
        mat.loc[(mat['index']=='2105427'), ['nivel']] = 24
        mat.loc[(mat['index']=='2105450'), ['nivel']] = 6
        mat.loc[(mat['index']=='2105476'), ['nivel']] = 28
        mat.loc[(mat['index']=='2105500'), ['nivel']] = 23
        mat.loc[(mat['index']=='2105609'), ['nivel']] = 14
        mat.loc[(mat['index']=='2105658'), ['nivel']] = 12
        mat.loc[(mat['index']=='2105708'), ['nivel']] = 29
        mat.loc[(mat['index']=='2105807'), ['nivel']] = 29
        mat.loc[(mat['index']=='2105906'), ['nivel']] = 17
        mat.loc[(mat['index']=='2105922'), ['nivel']] = 22
        mat.loc[(mat['index']=='2105948'), ['nivel']] = 29
        mat.loc[(mat['index']=='2105963'), ['nivel']] = 29
        mat.loc[(mat['index']=='2105989'), ['nivel']] = 2
        mat.loc[(mat['index']=='2106003'), ['nivel']] = 18
        mat.loc[(mat['index']=='2106102'), ['nivel']] = 9
        mat.loc[(mat['index']=='2106201'), ['nivel']] = 15
        mat.loc[(mat['index']=='2106300'), ['nivel']] = 13
        mat.loc[(mat['index']=='2106326'), ['nivel']] = 12
        mat.loc[(mat['index']=='2106359'), ['nivel']] = 29
        mat.loc[(mat['index']=='2106375'), ['nivel']] = 12
        mat.loc[(mat['index']=='2106409'), ['nivel']] = 7
        mat.loc[(mat['index']=='2106508'), ['nivel']] = 30
        mat.loc[(mat['index']=='2106607'), ['nivel']] = 19
        mat.loc[(mat['index']=='2106631'), ['nivel']] = 26
        mat.loc[(mat['index']=='2106672'), ['nivel']] = 13
        mat.loc[(mat['index']=='2106706'), ['nivel']] = 6
        mat.loc[(mat['index']=='2106755'), ['nivel']] = 26
        mat.loc[(mat['index']=='2106805'), ['nivel']] = 16
        mat.loc[(mat['index']=='2106904'), ['nivel']] = 21
        mat.loc[(mat['index']=='2107001'), ['nivel']] = 23
        mat.loc[(mat['index']=='2107100'), ['nivel']] = 11
        mat.loc[(mat['index']=='2107209'), ['nivel']] = 10
        mat.loc[(mat['index']=='2107258'), ['nivel']] = 27
        mat.loc[(mat['index']=='2107308'), ['nivel']] = 22
        mat.loc[(mat['index']=='2107357'), ['nivel']] = 8
        mat.loc[(mat['index']=='2107407'), ['nivel']] = 17
        mat.loc[(mat['index']=='2107456'), ['nivel']] = 30
        mat.loc[(mat['index']=='2107506'), ['nivel']] = 3
        mat.loc[(mat['index']=='2107605'), ['nivel']] = 1
        mat.loc[(mat['index']=='2107704'), ['nivel']] = 22
        mat.loc[(mat['index']=='2107803'), ['nivel']] = 19
        mat.loc[(mat['index']=='2107902'), ['nivel']] = 22
        mat.loc[(mat['index']=='2108009'), ['nivel']] = 22
        mat.loc[(mat['index']=='2108058'), ['nivel']] = 31
        mat.loc[(mat['index']=='2108108'), ['nivel']] = 29
        mat.loc[(mat['index']=='2108207'), ['nivel']] = 18
        mat.loc[(mat['index']=='2108256'), ['nivel']] = 20
        mat.loc[(mat['index']=='2108306'), ['nivel']] = 30
        mat.loc[(mat['index']=='2108405'), ['nivel']] = 20
        mat.loc[(mat['index']=='2108454'), ['nivel']] = 25
        mat.loc[(mat['index']=='2108504'), ['nivel']] = 21
        mat.loc[(mat['index']=='2108603'), ['nivel']] = 20
        mat.loc[(mat['index']=='2108702'), ['nivel']] = 21
        mat.loc[(mat['index']=='2108801'), ['nivel']] = 26
        mat.loc[(mat['index']=='2108900'), ['nivel']] = 18
        mat.loc[(mat['index']=='2109007'), ['nivel']] = 2
        mat.loc[(mat['index']=='2109056'), ['nivel']] = 16
        mat.loc[(mat['index']=='2109106'), ['nivel']] = 4
        mat.loc[(mat['index']=='2109205'), ['nivel']] = 11
        mat.loc[(mat['index']=='2109239'), ['nivel']] = 8
        mat.loc[(mat['index']=='2109270'), ['nivel']] = 20
        mat.loc[(mat['index']=='2109304'), ['nivel']] = 10
        mat.loc[(mat['index']=='2109403'), ['nivel']] = 31
        mat.loc[(mat['index']=='2109452'), ['nivel']] = 3
        mat.loc[(mat['index']=='2109502'), ['nivel']] = 27
        mat.loc[(mat['index']=='2109551'), ['nivel']] = 23
        mat.loc[(mat['index']=='2109601'), ['nivel']] = 11
        mat.loc[(mat['index']=='2109700'), ['nivel']] = 9
        mat.loc[(mat['index']=='2109759'), ['nivel']] = 4
        mat.loc[(mat['index']=='2109809'), ['nivel']] = 20
        mat.loc[(mat['index']=='2109908'), ['nivel']] = 21
        mat.loc[(mat['index']=='2110005'), ['nivel']] = 21
        mat.loc[(mat['index']=='2110039'), ['nivel']] = 8
        mat.loc[(mat['index']=='2110104'), ['nivel']] = 13
        mat.loc[(mat['index']=='2110203'), ['nivel']] = 10
        mat.loc[(mat['index']=='2110237'), ['nivel']] = 13
        mat.loc[(mat['index']=='2110278'), ['nivel']] = 31
        mat.loc[(mat['index']=='2110302'), ['nivel']] = 14
        mat.loc[(mat['index']=='2110401'), ['nivel']] = 7
        mat.loc[(mat['index']=='2110500'), ['nivel']] = 1
        mat.loc[(mat['index']=='2110609'), ['nivel']] = 13
        mat.loc[(mat['index']=='2110658'), ['nivel']] = 9
        mat.loc[(mat['index']=='2110708'), ['nivel']] = 4
        mat.loc[(mat['index']=='2110807'), ['nivel']] = 9
        mat.loc[(mat['index']=='2110856'), ['nivel']] = 24
        mat.loc[(mat['index']=='2110906'), ['nivel']] = 22
        mat.loc[(mat['index']=='2111003'), ['nivel']] = 1
        mat.loc[(mat['index']=='2111029'), ['nivel']] = 21
        mat.loc[(mat['index']=='2111052'), ['nivel']] = 2
        mat.loc[(mat['index']=='2111078'), ['nivel']] = 32
        mat.loc[(mat['index']=='2111102'), ['nivel']] = 22
        mat.loc[(mat['index']=='2111201'), ['nivel']] = 3
        mat.loc[(mat['index']=='2111250'), ['nivel']] = 14
        mat.loc[(mat['index']=='2111300'), ['nivel']] = 3
        mat.loc[(mat['index']=='2111409'), ['nivel']] = 17
        mat.loc[(mat['index']=='2111508'), ['nivel']] = 26
        mat.loc[(mat['index']=='2111532'), ['nivel']] = 24
        mat.loc[(mat['index']=='2111573'), ['nivel']] = 2
        mat.loc[(mat['index']=='2111607'), ['nivel']] = 9
        mat.loc[(mat['index']=='2111631'), ['nivel']] = 18
        mat.loc[(mat['index']=='2111672'), ['nivel']] = 18
        mat.loc[(mat['index']=='2111706'), ['nivel']] = 1
        mat.loc[(mat['index']=='2111722'), ['nivel']] = 21
        mat.loc[(mat['index']=='2111748'), ['nivel']] = 4
        mat.loc[(mat['index']=='2111763'), ['nivel']] = 23
        mat.loc[(mat['index']=='2111789'), ['nivel']] = 16
        mat.loc[(mat['index']=='2111805'), ['nivel']] = 5
        mat.loc[(mat['index']=='2111904'), ['nivel']] = 6
        mat.loc[(mat['index']=='2111953'), ['nivel']] = 22
        mat.loc[(mat['index']=='2112001'), ['nivel']] = 27
        mat.loc[(mat['index']=='2112100'), ['nivel']] = 25
        mat.loc[(mat['index']=='2112209'), ['nivel']] = 19
        mat.loc[(mat['index']=='2112233'), ['nivel']] = 18
        mat.loc[(mat['index']=='2112274'), ['nivel']] = 21
        mat.loc[(mat['index']=='2112308'), ['nivel']] = 4
        mat.loc[(mat['index']=='2112407'), ['nivel']] = 20
        mat.loc[(mat['index']=='2112456'), ['nivel']] = 20
        mat.loc[(mat['index']=='2112506'), ['nivel']] = 31
        mat.loc[(mat['index']=='2112605'), ['nivel']] = 7
        mat.loc[(mat['index']=='2112704'), ['nivel']] = 10
        mat.loc[(mat['index']=='2112803'), ['nivel']] = 30
        mat.loc[(mat['index']=='2112852'), ['nivel']] = 24
        mat.loc[(mat['index']=='2112902'), ['nivel']] = 26
        mat.loc[(mat['index']=='2113009'), ['nivel']] = 17
        mat.loc[(mat['index']=='2114007'), ['nivel']] = 8
        mat=mat.groupby("nivel").sum()
        mat=mat.reset_index()
        mat.insert(0, "nome", 0)
        mat.loc[(mat['nivel']==1), ['nome']] ='Baixada Maranhense'
        mat.loc[(mat['nivel']==2), ['nome']] ='Chapada Das Mesas'
        mat.loc[(mat['nivel']==3), ['nome']] ='Ilha Do Maranhão'
        mat.loc[(mat['nivel']==4), ['nome']] ='Pré-Amazônia'
        mat.loc[(mat['nivel']==5), ['nome']] ='Serras'
        mat.loc[(mat['nivel']==6), ['nome']] ='Alpercatas'
        mat.loc[(mat['nivel']==7), ['nome']] ='Alto Munim'
        mat.loc[(mat['nivel']==8), ['nome']] ='Alto Turi'
        mat.loc[(mat['nivel']==9), ['nome']] ='Baixo Balsas'
        mat.loc[(mat['nivel']==10), ['nome']] ='Baixo Itapecuru'
        mat.loc[(mat['nivel']==11), ['nome']] ='Baixo Munim'
        mat.loc[(mat['nivel']==12), ['nome']] ='Baixo Turi'
        mat.loc[(mat['nivel']==13), ['nome']] ='Delta Do Parnaíba'
        mat.loc[(mat['nivel']==14), ['nome']] ='Flores'
        mat.loc[(mat['nivel']==15), ['nome']] ='Gurupi'
        mat.loc[(mat['nivel']==16), ['nome']] ='Litoral Ocidental'
        mat.loc[(mat['nivel']==17), ['nome']] ='Mearim'
        mat.loc[(mat['nivel']==18), ['nome']] ='Médio Mearim'
        mat.loc[(mat['nivel']==19), ['nome']] ='Médio Parnaíba'
        mat.loc[(mat['nivel']==20), ['nome']] ='Pericumã'
        mat.loc[(mat['nivel']==21), ['nome']] ='Pindaré'
        mat.loc[(mat['nivel']==22), ['nome']] ='Sertão Maranhense'
        mat.loc[(mat['nivel']==23), ['nome']] ='Tocantins'
        mat.loc[(mat['nivel']==24), ['nome']] ='Carajás'
        mat.loc[(mat['nivel']==25), ['nome']] ='Cocais'
        mat.loc[(mat['nivel']==26), ['nome']] ='Eixos Rodoferroviários'
        mat.loc[(mat['nivel']==27), ['nome']] ='Gerais De Balsas'
        mat.loc[(mat['nivel']==28), ['nome']] ='Guajajaras'
        mat.loc[(mat['nivel']==29), ['nome']] ='Imigrantes'
        mat.loc[(mat['nivel']==30), ['nome']] ='Lagos'
        mat.loc[(mat['nivel']==31), ['nome']] ='Lençóis Maranhenses'
        mat.loc[(mat['nivel']==32), ['nome']] ='Timbiras'
        print(mat)
        #mat.to_excel("serie_agregada_regioes_planejamento.xlsx", index=False)
    except:
        print(f"Tabela {serie} nem rodou")
print("programa encerrado")