# -*- coding: utf-8 -*-
'''
# SÉRIES DISPONÍVEIS A PARTIR DESSE CÓDIGO
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41,
42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 240, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 268, 269, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 426, 427, 879, 882, 909, 910, 911, 912, 913, 914, 915,916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931**
'''

import ssl
import requests
import urllib3
import openpyxl
import ast
import pandas as pd

series_validas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 240, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 268, 269, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 426, 427, 879, 882, 909, 910, 911, 912, 913, 914, 915,916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931]

print(f'Estas são as séries válidas para consulta: {series_validas}')
SERIES = input("Insira as séries desejadas (separadas por vírgula, caso seja mais de uma): ")
SERIES = [int(x) for x in SERIES.split(",")]
SERIES_N = []
for serie in SERIES:
    if serie in series_validas:
        SERIES_N.append(serie)
    else:
        print(f'Essa série não é válida: {serie}')
        print("Tente novamente com séries válidas")
        print("Séries válidas: ", series_validas)
        SERIES_N = input("Insira APENAS as séries válidas desejadas (separadas por vírgula, caso seja mais de uma): ")
        SERIES_N = [int(x) for x in SERIES_N.split(",")]

ANO_INICIAL = int(input('Insira o ano inicial desejado: '))
ANO_FINAL = int(input('Insira o ano final desejado: ')) + 1
ANOS=range(ANO_INICIAL,ANO_FINAL)
ANO=[]
for i in ANOS:
    ANO.append(f"{i}")

class CustomHttpAdapter (requests.adapters.HTTPAdapter):
    # "Transport adapter" that allows us to use custom ssl_context.

    def __init__(self, ssl_context=None, **kwargs):
        self.ssl_context = ssl_context
        super().__init__(**kwargs)

    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = urllib3.poolmanager.PoolManager(
            num_pools=connections, maxsize=maxsize,
            block=block, ssl_context=self.ssl_context)

def get_legacy_session():
    ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    ctx.options |= 0x4  # OP_LEGACY_SERVER_CONNECT
    session = requests.session()
    session.mount('https://', CustomHttpAdapter(ctx))
    return session

class dataImesc:
    def __init__(self,ano):
        self.dicio={1:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2688]",
                    2:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2689]",
                    3:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2691]",
                    4:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2692]",
                    5:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2694]",
                    6:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2696]",
                    7:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2701]",
                    8:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2702]",
                    9:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2708]",
                    10:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2709]",
                    11:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2710]",
                    12:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2711]",
                    13:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2713]",
                    14:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2714]",
                    15:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2715]",
                    16:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[0]",
                    17:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2688]",
                    18:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2689]",
                    19:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2691]",
                    20:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2692]",
                    21:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2694]",
                    22:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2696]",
                    23:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2701]",
                    24:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2702]",
                    25:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2708]",
                    26:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2709]",
                    27:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2710]",
                    28:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2711]",
                    29:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2713]",
                    30:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2714]",
                    31:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2715]",
                    32:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2688]",
                    33:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2689]",
                    34:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2691]",
                    35:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2692]",
                    36:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2694]",
                    37:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2696]",
                    38:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2701]",
                    39:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2702]",
                    40:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2708]",
                    41:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2709]",
                    42:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2710]",
                    43:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2711]",
                    44:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2713]",
                    45:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2714]",
                    46:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2715]",
                    47:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[0]",
                    48:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2688]",
                    49:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2689]",
                    50:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2691]",
                    51:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2692]",
                    52:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2694]",
                    53:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2696]",
                    54:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2701]",
                    55:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2702]",
                    56:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2708]",
                    57:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2709]",
                    58:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2710]",
                    59:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2711]",
                    60:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2713]",
                    61:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2714]",
                    62:f"https://servicodados.ibge.gov.br/api/v3/agregados/1612/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=81[2715]",
                    63:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2720]",
                    64:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2721]",
                    65:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2725]",
                    66:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2727]",
                    67:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2733]",
                    68:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2734]",
                    69:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2736]",
                    70:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2737]",
                    71:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2738]",
                    72:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2743]",
                    73:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2745]",
                    74:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/214?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2747]",
                    75:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[0]",
                    76:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2720]",
                    77:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2721]",
                    78:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2725]",
                    79:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2727]",
                    80:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2733]",
                    81:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2734]",
                    82:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2736]",
                    83:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2737]",
                    84:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2738]",
                    85:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2743]",
                    86:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2745]",
                    87:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/216?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2747]",
                    88:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2720]",
                    89:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2721]",
                    90:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2725]",
                    91:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2727]",
                    92:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2733]",
                    93:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2734]",
                    94:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2736]",
                    95:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2737]",
                    96:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2738]",
                    97:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2743]",
                    98:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2745]",
                    99:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/112?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2747]",
                    100:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[0]",
                    101:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2720]",
                    102:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2721]",
                    103:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2725]",
                    104:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2727]",
                    105:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2733]",
                    106:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2734]",
                    107:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2736]",
                    108:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2737]",
                    109:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2738]",
                    110:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2743]",
                    111:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2745]",
                    112:f"https://servicodados.ibge.gov.br/api/v3/agregados/1613/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=82[2747]",
                    113:f"https://servicodados.ibge.gov.br/api/v3/agregados/291/periodos/{ano}/variaveis/142?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=194[33247]",
                    114:f"https://servicodados.ibge.gov.br/api/v3/agregados/291/periodos/{ano}/variaveis/142?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=194[33248]",
                    115:f"https://servicodados.ibge.gov.br/api/v3/agregados/291/periodos/{ano}/variaveis/142?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=194[33249]",
                    116:f"https://servicodados.ibge.gov.br/api/v3/agregados/291/periodos/{ano}/variaveis/142?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=194[33250]",
                    117:f"https://servicodados.ibge.gov.br/api/v3/agregados/291/periodos/{ano}/variaveis/142?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=194[33251]",
                    118:f"https://servicodados.ibge.gov.br/api/v3/agregados/291/periodos/{ano}/variaveis/142?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=194[33252]",
                    119:f"https://servicodados.ibge.gov.br/api/v3/agregados/291/periodos/{ano}/variaveis/142?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=194[3458]",
                    120:f"https://servicodados.ibge.gov.br/api/v3/agregados/291/periodos/{ano}/variaveis/142?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=194[3459]",
                    121:f"https://servicodados.ibge.gov.br/api/v3/agregados/291/periodos/{ano}/variaveis/143?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=194[33247]",
                    122:f"https://servicodados.ibge.gov.br/api/v3/agregados/291/periodos/{ano}/variaveis/143?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=194[33248]",
                    123:f"https://servicodados.ibge.gov.br/api/v3/agregados/291/periodos/{ano}/variaveis/143?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=194[33249]",
                    124:f"https://servicodados.ibge.gov.br/api/v3/agregados/291/periodos/{ano}/variaveis/143?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=194[33250]",
                    125:f"https://servicodados.ibge.gov.br/api/v3/agregados/291/periodos/{ano}/variaveis/143?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=194[33251]",
                    126:f"https://servicodados.ibge.gov.br/api/v3/agregados/291/periodos/{ano}/variaveis/143?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=194[33252]",
                    127:f"https://servicodados.ibge.gov.br/api/v3/agregados/291/periodos/{ano}/variaveis/143?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=194[3458]",
                    128:f"https://servicodados.ibge.gov.br/api/v3/agregados/291/periodos/{ano}/variaveis/143?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=194[3459]",
                    129:f"https://servicodados.ibge.gov.br/api/v3/agregados/291/periodos/{ano}/variaveis/143?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=194[0]",
                    130:f"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/{ano}/variaveis/144?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3403]",
                    131:f"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/{ano}/variaveis/144?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3404]",
                    132:f"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/{ano}/variaveis/144?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3407]",
                    133:f"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/{ano}/variaveis/144?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[39409]",
                    134:f"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/{ano}/variaveis/144?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[11296]",
                    135:f"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/{ano}/variaveis/145?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3403]",
                    136:f"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/{ano}/variaveis/145?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3404]",
                    137:f"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/{ano}/variaveis/145?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3407]",
                    138:f"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/{ano}/variaveis/145?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[39409]",
                    139:f"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/{ano}/variaveis/145?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[11296]",
                    140:f"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/{ano}/variaveis/145?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[0]",
                    141:f"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/{ano}/variaveis/144?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3413]",
                    142:f"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/{ano}/variaveis/144?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3415]",
                    143:f"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/{ano}/variaveis/144?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3421]",
                    144:f"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/{ano}/variaveis/144?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3422]",
                    145:f"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/{ano}/variaveis/144?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3424]",
                    146:f"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/{ano}/variaveis/144?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3425]",
                    147:f"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/{ano}/variaveis/144?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3426]",
                    148:f"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/{ano}/variaveis/144?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3427]",
                    149:f"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/{ano}/variaveis/144?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3433]",
                    150:f"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/{ano}/variaveis/144?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]]&classificacao=193[3434]",
                    151:f"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/{ano}/variaveis/144?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]]&classificacao=193[3435]",
                    152:f"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/{ano}/variaveis/144?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]]&classificacao=193[3439]",
                    #153:f"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/{ano}/variaveis/144?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]}]&classificacao=193[3444]",
                    154:f"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/{ano}/variaveis/144?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]]&classificacao=193[3445]",
                    155:f"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/{ano}/variaveis/144?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3446]",
                    156:f"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/{ano}/variaveis/145?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3413]|193[3413]",
                    157:f"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/{ano}/variaveis/145?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3415]|193[3415]",
                    158:f"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/{ano}/variaveis/145?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3421]|193[3421]",
                    159:f"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/{ano}/variaveis/145?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3422]|193[3422]",
                    160:f"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/{ano}/variaveis/145?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3424]|193[3424]",
                    161:f"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/{ano}/variaveis/145?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3425]|193[3425]",
                    162:f"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/{ano}/variaveis/145?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3426]|193[3426]",
                    163:f"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/{ano}/variaveis/145?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3427]|193[3427]",
                    164:f"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/{ano}/variaveis/145?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3433]|193[3433]",
                    165:f"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/{ano}/variaveis/145?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3434]|193[3434]",
                    166:f"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/{ano}/variaveis/145?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3435]|193[3435]",
                    167:f"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/{ano}/variaveis/145?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3439]|193[3439]",
                    168:f"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/{ano}/variaveis/145?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3444]|193[3444]",
                    169:f"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/{ano}/variaveis/145?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3445]|193[3445]",
                    170:f"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/{ano}/variaveis/145?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3446]|193[3446]",
                    171:f"https://servicodados.ibge.gov.br/api/v3/agregados/74/periodos/{ano}/variaveis/106?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=80[2682]",
                    172:f"https://servicodados.ibge.gov.br/api/v3/agregados/74/periodos/{ano}/variaveis/106?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=80[2685]",
                    173:f"https://servicodados.ibge.gov.br/api/v3/agregados/74/periodos/{ano}/variaveis/106?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=80[2686]",
                    174:f"https://servicodados.ibge.gov.br/api/v3/agregados/74/periodos/{ano}/variaveis/106?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=80[2687]",
                    175:f"https://servicodados.ibge.gov.br/api/v3/agregados/74/periodos/{ano}/variaveis/106?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=80[2683]",
                    176:f"https://servicodados.ibge.gov.br/api/v3/agregados/74/periodos/{ano}/variaveis/106?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=80[2684]",
                    177:f"https://servicodados.ibge.gov.br/api/v3/agregados/74/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=80[2682]",
                    178:f"https://servicodados.ibge.gov.br/api/v3/agregados/74/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=80[2685]",
                    179:f"https://servicodados.ibge.gov.br/api/v3/agregados/74/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=80[2686]",
                    180:f"https://servicodados.ibge.gov.br/api/v3/agregados/74/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=80[2687]",
                    181:f"https://servicodados.ibge.gov.br/api/v3/agregados/74/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=80[2683]",
                    182:f"https://servicodados.ibge.gov.br/api/v3/agregados/74/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=80[2684]",
                    183:f"https://servicodados.ibge.gov.br/api/v3/agregados/74/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=80[0]",
                    184:f"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/{ano}/variaveis/4146?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32861]",
                    185:f"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/{ano}/variaveis/4146?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32865]",
                    186:f"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/{ano}/variaveis/4146?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32867]",
                    187:f"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/{ano}/variaveis/4146?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32869]",
                    188:f"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/{ano}/variaveis/4146?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32870]",
                    189:f"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/{ano}/variaveis/4146?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32871]",
                    190:f"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/{ano}/variaveis/4146?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32872]",
                    191:f"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/{ano}/variaveis/4146?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32873]",
                    192:f"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/{ano}/variaveis/4146?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32874]",
                    193:f"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/{ano}/variaveis/4146?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32875]",
                    194:f"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/{ano}/variaveis/4146?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32876]",
                    195:f"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/{ano}/variaveis/4146?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32877]",
                    196:f"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/{ano}/variaveis/4146?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32878]",
                    197:f"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/{ano}/variaveis/4146?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32880]",
                    198:f"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/{ano}/variaveis/4146?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32881]",
                    199:f"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/{ano}/variaveis/4146?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32886]",
                    200:f"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/{ano}/variaveis/4146?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32887]",
                    201:f"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/{ano}/variaveis/4146?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32889]",
                    202:f"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32861]",
                    203:f"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32865]",
                    204:f"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32867]",
                    205:f"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32869]",
                    206:f"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32870]",
                    207:f"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32871]",
                    208:f"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32872]",
                    209:f"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32873]",
                    210:f"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32874]",
                    211:f"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32875]",
                    212:f"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32876]",
                    213:f"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32877]",
                    214:f"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32878]",
                    215:f"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32880]",
                    216:f"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32881]",
                    217:f"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32886]",
                    218:f"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32887]",
                    219:f"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[32889]",
                    220:f"https://servicodados.ibge.gov.br/api/v3/agregados/3940/periodos/{ano}/variaveis/215?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=654[0]",
                    221:f"https://servicodados.ibge.gov.br/api/v3/agregados/3939/periodos/{ano}/variaveis/105?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=79[2670]",
                    222:f"https://servicodados.ibge.gov.br/api/v3/agregados/3939/periodos/{ano}/variaveis/105?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=79[2675]",
                    223:f"https://servicodados.ibge.gov.br/api/v3/agregados/3939/periodos/{ano}/variaveis/105?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=79[2672]",
                    224:f"https://servicodados.ibge.gov.br/api/v3/agregados/3939/periodos/{ano}/variaveis/105?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=79[32794]",
                    225:f"https://servicodados.ibge.gov.br/api/v3/agregados/3939/periodos/{ano}/variaveis/105?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=79[32795]",
                    226:f"https://servicodados.ibge.gov.br/api/v3/agregados/3939/periodos/{ano}/variaveis/105?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=79[2681]",
                    227:f"https://servicodados.ibge.gov.br/api/v3/agregados/3939/periodos/{ano}/variaveis/105?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=79[2677]",
                    228:f"https://servicodados.ibge.gov.br/api/v3/agregados/3939/periodos/{ano}/variaveis/105?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=79[32796]",
                    229:f"https://servicodados.ibge.gov.br/api/v3/agregados/3939/periodos/{ano}/variaveis/105?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=79[32793]",
                    230:f"https://servicodados.ibge.gov.br/api/v3/agregados/3939/periodos/{ano}/variaveis/105?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=79[2680]",
                    231:f"https://servicodados.ibge.gov.br/api/v3/agregados/5938/periodos/{ano}/variaveis/37?localidades=N1[all]|N3[all]",
                    232:f"",
                    233:f"https://servicodados.ibge.gov.br/api/v3/agregados/5938/periodos/{ano}/variaveis/498?localidades=N1[all]|N3[all]",
                    234:f"https://servicodados.ibge.gov.br/api/v3/agregados/5938/periodos/{ano}/variaveis/513?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]",
                    235:f"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/{ano}/variaveis/144?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3440]",
                    240:f"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/{ano}/variaveis/145?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3440]",
                    251:f"https://servicodados.ibge.gov.br/api/v3/agregados/5938/periodos/{ano}/variaveis/37?localidades=N6[N3[21]]",
                    252:f"https://servicodados.ibge.gov.br/api/v3/agregados/5938/periodos/{ano}/variaveis/543?localidades=N6[N3[21]]",
                    253:f"https://servicodados.ibge.gov.br/api/v3/agregados/5938/periodos/{ano}/variaveis/498?localidades=N6[N3[21]]",
                    254:f"https://servicodados.ibge.gov.br/api/v3/agregados/5938/periodos/{ano}/variaveis/513?localidades=N6[N3[21]]",
                    255:f"https://servicodados.ibge.gov.br/api/v3/agregados/291/periodos/{ano}/variaveis/142?localidades=N6[N3[21]]&classificacao=194[3455]",
                    256:f"https://servicodados.ibge.gov.br/api/v3/agregados/5938/periodos/{ano}/variaveis/517?localidades=N6[N3[21]]",
                    257:f"https://servicodados.ibge.gov.br/api/v3/agregados/291/periodos/{ano}/variaveis/142?localidades=N6[N3[21]]&classificacao=194[3456]",
                    258:f"https://servicodados.ibge.gov.br/api/v3/agregados/5938/periodos/{ano}/variaveis/6575?localidades=N6[N3[21]]",
                    259:f"https://servicodados.ibge.gov.br/api/v3/agregados/291/periodos/{ano}/variaveis/142?localidades=N6[N3[21]]",
                    260:f"https://servicodados.ibge.gov.br/api/v3/agregados/5938/periodos/{ano}/variaveis/525?localidades=N6[N3[21]]",
                    261:f"https://servicodados.ibge.gov.br/api/v3/agregados/291/periodos/{ano}/variaveis/143?localidades=N6[N3[21]]&classificacao=194[3455]",
                    268:f"https://servicodados.ibge.gov.br/api/v3/agregados/7431/periodos/{ano}/variaveis/10765?localidades=N1[all]|N2[all]|N3[all]&classificacao=86[2776]",
                    269:f"https://servicodados.ibge.gov.br/api/v3/agregados/7431/periodos/{ano}/variaveis/10765?localidades=N1[all]|N2[all]|N3[all]&classificacao=86[2779]",
                    278:f"https://servicodados.ibge.gov.br/api/v3/agregados/7431/periodos/{ano}/variaveis/10765?localidades=N1[all]|N2[all]|N3[all]&classificacao=86[95251]",
                    279:f"https://servicodados.ibge.gov.br/api/v3/agregados/7434/periodos/{ano}/variaveis/10765?localidades=N1[all]|N2[all]|N3[all]&classificacao=2[4]",
                    280:f"https://servicodados.ibge.gov.br/api/v3/agregados/7434/periodos/{ano}/variaveis/10765?localidades=N1[all]|N2[all]|N3[all]&classificacao=2[5]",
                    281:f"https://servicodados.ibge.gov.br/api/v3/agregados/7433/periodos/{ano}/variaveis/10765?localidades=N1[all]|N2[all]|N3[all]&classificacao=1568[18837]",
                    282:f"https://servicodados.ibge.gov.br/api/v3/agregados/7433/periodos/{ano}/variaveis/10765?localidades=N1[all]|N2[all]|N3[all]&classificacao=1568[11779]",
                    283:f"https://servicodados.ibge.gov.br/api/v3/agregados/7433/periodos/{ano}/variaveis/10765?localidades=N1[all]|N2[all]|N3[all]&classificacao=1568[11628]",
                    284:f"https://servicodados.ibge.gov.br/api/v3/agregados/7433/periodos/{ano}/variaveis/10765?localidades=N1[all]|N2[all]|N3[all]&classificacao=1568[11629]",
                    285:f"https://servicodados.ibge.gov.br/api/v3/agregados/7433/periodos/{ano}/variaveis/10765?localidades=N1[all]|N2[all]|N3[all]&classificacao=1568[11630]",
                    286:f"https://servicodados.ibge.gov.br/api/v3/agregados/7433/periodos/{ano}/variaveis/10765?localidades=N1[all]|N2[all]|N3[all]&classificacao=1568[11631]",
                    287:f"https://servicodados.ibge.gov.br/api/v3/agregados/7433/periodos/{ano}/variaveis/10765?localidades=N1[all]|N2[all]|N3[all]&classificacao=1568[99713]",
                    288:f"https://servicodados.ibge.gov.br/api/v3/agregados/7444/periodos/{ano}/variaveis/10774?localidades=N1[all]|N2[all]|N3[all]&classificacao=2[6794]",
                    289:f"https://servicodados.ibge.gov.br/api/v3/agregados/7444/periodos/{ano}/variaveis/10774?localidades=N1[all]|N2[all]|N3[all]&classificacao=2[4]",
                    290:f"https://servicodados.ibge.gov.br/api/v3/agregados/7444/periodos/{ano}/variaveis/10774?localidades=N1[all]|N2[all]|N3[all]&classificacao=2[5]",
                    291:f"https://servicodados.ibge.gov.br/api/v3/agregados/7441/periodos/{ano}/variaveis/10774?localidades=N1[all]|N2[all]|N3[all]&classificacao=86[2776]",
                    292:f"https://servicodados.ibge.gov.br/api/v3/agregados/7441/periodos/{ano}/variaveis/10774?localidades=N1[all]|N2[all]|N3[all]&classificacao=86[2779]",
                    293:f"https://servicodados.ibge.gov.br/api/v3/agregados/7441/periodos/{ano}/variaveis/10774?localidades=N1[all]|N2[all]|N3[all]&classificacao=86[2777]",
                    294:f"https://servicodados.ibge.gov.br/api/v3/agregados/7443/periodos/{ano}/variaveis/10774?localidades=N1[all]|N2[all]|N3[all]&classificacao=1568[18837]",
                    295:f"https://servicodados.ibge.gov.br/api/v3/agregados/7443/periodos/{ano}/variaveis/10774?localidades=N1[all]|N2[all]|N3[all]&classificacao=1568[11779]",
                    296:f"https://servicodados.ibge.gov.br/api/v3/agregados/7443/periodos/{ano}/variaveis/10774?localidades=N1[all]|N2[all]|N3[all]&classificacao=1568[11628]",
                    297:f"https://servicodados.ibge.gov.br/api/v3/agregados/7443/periodos/{ano}/variaveis/10774?localidades=N1[all]|N2[all]|N3[all]&classificacao=1568[11629]",
                    298:f"https://servicodados.ibge.gov.br/api/v3/agregados/7443/periodos/{ano}/variaveis/10774?localidades=N1[all]|N2[all]|N3[all]&classificacao=1568[11630]",
                    299:f"https://servicodados.ibge.gov.br/api/v3/agregados/7443/periodos/{ano}/variaveis/10774?localidades=N1[all]|N2[all]|N3[all]&classificacao=1568[11631]",
                    300:f"https://servicodados.ibge.gov.br/api/v3/agregados/7443/periodos/{ano}/variaveis/10774?localidades=N1[all]|N2[all]|N3[all]&classificacao=1568[99713]",
                    #393:"https://servicodados.ibge.gov.br/api/v3/agregados/1301/periodos/{ano}/variaveis/616?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]",
                    394:f"https://servicodados.ibge.gov.br/api/v3/agregados/200/periodos/{ano}/variaveis/93?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=1[1]",
                    395:f"https://servicodados.ibge.gov.br/api/v3/agregados/200/periodos/{ano}/variaveis/93?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=1[2]",
                    396:f"https://servicodados.ibge.gov.br/api/v3/agregados/200/periodos/{ano}/variaveis/93?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=2[4]",
                    397:f"https://servicodados.ibge.gov.br/api/v3/agregados/200/periodos/{ano}/variaveis/93?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=2[5]",
                    398:f"https://servicodados.ibge.gov.br/api/v3/agregados/136/periodos/{ano}/variaveis/93?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=86[2776]",
                    399:f"https://servicodados.ibge.gov.br/api/v3/agregados/136/periodos/{ano}/variaveis/93?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=86[2777]",
                    400:f"https://servicodados.ibge.gov.br/api/v3/agregados/136/periodos/{ano}/variaveis/93?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=86[2778]",
                    401:f"https://servicodados.ibge.gov.br/api/v3/agregados/136/periodos/{ano}/variaveis/93?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=86[2779]",
                    402:f"https://servicodados.ibge.gov.br/api/v3/agregados/136/periodos/{ano}/variaveis/93?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=86[2780]",
                    403:f"https://servicodados.ibge.gov.br/api/v3/agregados/136/periodos/{ano}/variaveis/93?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=86[2781]",
                    426:f"https://servicodados.ibge.gov.br/api/v3/agregados/793/periodos/{ano}/variaveis/93?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]",
                    427:f"https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/{ano}/variaveis/9324?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]",
                    879:f"https://servicodados.ibge.gov.br/api/v3/agregados/289/periodos/{ano}/variaveis/145?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=193[3434]",
                    882:f"https://servicodados.ibge.gov.br/api/v3/agregados/7431/periodos/{ano}/variaveis/10765?localidades=N1[all]|N2[all]|N3[all]&classificacao=86[2777]",
                    909:f"https://servicodados.ibge.gov.br/api/v3/agregados/827/periodos/{ano}/variaveis/1982?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=12528[111701]|12517[0]",
                    910:f"https://servicodados.ibge.gov.br/api/v3/agregados/6959/periodos/{ano}/variaveis/10085?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=829[46302]|226[4851]",
                    911:f"https://servicodados.ibge.gov.br/api/v3/agregados/827/periodos/{ano}/variaveis/1982?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=12528[111724]|12517[0]",
                    912:f"https://servicodados.ibge.gov.br/api/v3/agregados/827/periodos/{ano}/variaveis/1982?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=12528[111726]|12517[0]",
                    913:f"https://servicodados.ibge.gov.br/api/v3/agregados/827/periodos/{ano}/variaveis/1982?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=12528[111725]|12517[0]",
                    914:f"https://servicodados.ibge.gov.br/api/v3/agregados/827/periodos/{ano}/variaveis/1982?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=12528[111727]|12517[0]",
                    915:f"https://servicodados.ibge.gov.br/api/v3/agregados/827/periodos/{ano}/variaveis/1982?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=12528[111730]|12517[0]",
                    916:f"https://servicodados.ibge.gov.br/api/v3/agregados/827/periodos/{ano}/variaveis/1982?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=12528[111729]|12517[0]",
                    917:f"https://servicodados.ibge.gov.br/api/v3/agregados/827/periodos/{ano}/variaveis/1982?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=12528[111709]|12517[0]",
                    918:f"https://servicodados.ibge.gov.br/api/v3/agregados/827/periodos/{ano}/variaveis/1982?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=12528[111728]|12517[0]",
                    919:f"https://servicodados.ibge.gov.br/api/v3/agregados/827/periodos/{ano}/variaveis/1982?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=12528[111710]|12517[0]",
                    920:f"https://servicodados.ibge.gov.br/api/v3/agregados/827/periodos/{ano}/variaveis/1982?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=12528[111711]|12517[0]",
                    921:f"https://servicodados.ibge.gov.br/api/v3/agregados/827/periodos/{ano}/variaveis/1982?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=12528[111733]|12517[0]",
                    922:f"https://servicodados.ibge.gov.br/api/v3/agregados/827/periodos/{ano}/variaveis/1982?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=12528[111713]|12517[0]",
                    923:f"https://servicodados.ibge.gov.br/api/v3/agregados/827/periodos/{ano}/variaveis/1982?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=12528[111714]|12517[0]",
                    924:f"https://servicodados.ibge.gov.br/api/v3/agregados/827/periodos/{ano}/variaveis/1982?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=12528[111715]|12517[0]",
                    925:f"https://servicodados.ibge.gov.br/api/v3/agregados/827/periodos/{ano}/variaveis/1982?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=12528[111716]|12517[0]",
                    926:f"https://servicodados.ibge.gov.br/api/v3/agregados/827/periodos/{ano}/variaveis/1982?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=12528[111719]|12517[0]",
                    927:f"https://servicodados.ibge.gov.br/api/v3/agregados/827/periodos/{ano}/variaveis/1982?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=12528[111731]|12517[0]",
                    928:f"https://servicodados.ibge.gov.br/api/v3/agregados/827/periodos/{ano}/variaveis/1982?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=12528[111718]|12517[0]",
                    929:f"https://servicodados.ibge.gov.br/api/v3/agregados/827/periodos/{ano}/variaveis/1982?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=12528[111720]|12517[0]",
                    930:f"https://servicodados.ibge.gov.br/api/v3/agregados/827/periodos/{ano}/variaveis/1982?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=12528[111722]|12517[0]",
                    931:f"https://servicodados.ibge.gov.br/api/v3/agregados/827/periodos/{ano}/variaveis/1982?localidades=N1[all]|N2[all]|N3[all]|N6[N3[21]]&classificacao=12528[111717]|12517[0]"
                    }

        self.lista=[]
        self.serie=[]

    def procurar_tabela(self, numero_Tabela):
        #Get the request
        self.tabela=numero_Tabela
        self.Resposta= get_legacy_session().get(self.dicio[numero_Tabela])
        self.Resposta=self.Resposta.json()
        self.organiza_json()
        self.transforma_em_pandas()
        resultado=self.formato_dataimesc()
        return resultado

    def organiza_json(self):
        #Unpacking the JSON
        self.results=self.Resposta
        self.first=self.results[0]
        self.second=self.first["resultados"]
        self.third=self.second[0]
        self.fouth=self.third["series"]
        for i in self.fouth:
            self.local=i['localidade']
            self.result2=f'"localidade":{self.local["id"]}, "nome":"{self.local["nome"]}"'
            self.serie.append(ast.literal_eval(f"{i['serie']}"))
            self.result3="{"+self.result2+"}"
            self.lista.append(ast.literal_eval(self.result3))

    def transforma_em_pandas(self):
        data_Cidades=pd.DataFrame(self.lista)
        self.data_Serie=pd.DataFrame(self.serie)
        self.anos=list(self.data_Serie.columns)
        data_frame=pd.concat([data_Cidades,self.data_Serie], axis=1)
        data_frame.loc[(data_frame['localidade']==1 )& (data_frame['nome']=='Brasil'), ['localidade']] = 'BR'
        data_frame.loc[(data_frame['localidade']==1 )& (data_frame["nome"]=="Norte"), ['localidade']] = "N"
        data_frame.loc[(data_frame['localidade']==2 ), ['localidade']] = "NE"
        data_frame.loc[(data_frame['localidade']==3 ), ['localidade']] = "SE"
        data_frame.loc[(data_frame['localidade']==4 ), ['localidade']] = "S"
        data_frame.loc[(data_frame['localidade']==5 ), ['localidade']] = "CO"
        data_frame.loc[(data_frame['localidade']==11 ), ['localidade']] = "RO"
        data_frame.loc[(data_frame['localidade']==12 ), ['localidade']] = "AC"
        data_frame.loc[(data_frame['localidade']==13 ), ['localidade']] = "AM"
        data_frame.loc[(data_frame['localidade']==14 ), ['localidade']] = "RR"
        data_frame.loc[(data_frame['localidade']==15 ), ['localidade']] = "PA"
        data_frame.loc[(data_frame['localidade']==16 ), ['localidade']] = "AP"
        data_frame.loc[(data_frame['localidade']==17 ), ['localidade']] = "TO"
        data_frame.loc[(data_frame['localidade']==21 ), ['localidade']] = "MA"
        data_frame.loc[(data_frame['localidade']==22 ), ['localidade']] = "PI"
        data_frame.loc[(data_frame['localidade']==23 ), ['localidade']] = "CE"
        data_frame.loc[(data_frame['localidade']==24 ), ['localidade']] = "RN"
        data_frame.loc[(data_frame['localidade']==25 ), ['localidade']] = "PB"
        data_frame.loc[(data_frame['localidade']==26 ), ['localidade']] = "PE"
        data_frame.loc[(data_frame['localidade']==27 ), ['localidade']] = "AL"
        data_frame.loc[(data_frame['localidade']==28 ), ['localidade']] = "SE"
        data_frame.loc[(data_frame['localidade']==29 ), ['localidade']] = "BA"
        data_frame.loc[(data_frame['localidade']==31 ), ['localidade']] = "MG"
        data_frame.loc[(data_frame['localidade']==32 ), ['localidade']] = "ES"
        data_frame.loc[(data_frame['localidade']==33 ), ['localidade']] = "RJ"
        data_frame.loc[(data_frame['localidade']==35 ), ['localidade']] = "SP"
        data_frame.loc[(data_frame['localidade']==41 ), ['localidade']] = "PR"
        data_frame.loc[(data_frame['localidade']==42 ), ['localidade']] = "SC"
        data_frame.loc[(data_frame['localidade']==43 ), ['localidade']] = "RS"
        data_frame.loc[(data_frame['localidade']==50 ), ['localidade']] = "MS"
        data_frame.loc[(data_frame['localidade']==51 ), ['localidade']] = "MT"
        data_frame.loc[(data_frame['localidade']==52 ), ['localidade']] = "GO"
        data_frame.loc[(data_frame['localidade']==53 ), ['localidade']] = "DF"
        data_frame.insert(loc=0, column="serie", value=self.tabela)
        data_frame.insert(loc=1, column="abrangencia", value="4")
        data_frame.loc[(data_frame['nome']=="Brasil" ), ['abrangencia']] = "1"
        data_frame.loc[(data_frame['nome']=="Norte" ), ['abrangencia']] = "2"
        data_frame.loc[(data_frame['nome']=="Nordeste" ), ['abrangencia']] = "2"
        data_frame.loc[(data_frame['nome']=="Centro-Oeste" ), ['abrangencia']] = "2"
        data_frame.loc[(data_frame['nome']=="Sul" ), ['abrangencia']] = "2"
        data_frame.loc[(data_frame['nome']=="Sudeste" ), ['abrangencia']] = "2"
        data_frame.loc[(data_frame['nome']=="Rondônia" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Acre" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Amazonas" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Roraima" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Pará" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Amapá" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Tocantins" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Maranhão" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Piauí" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Ceará" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Rio Grande do Norte"), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Paraíba" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Pernambuco" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Alagoas" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Sergipe" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Bahia" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Minas Gerais" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Espírito Santo" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Rio de Janeiro" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="São Paulo" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Paraná" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Santa Catarina" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Rio Grande do Sul" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Mato Grosso do Sul" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Mato Grosso" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Goiás" ), ['abrangencia']] = "3"
        data_frame.loc[(data_frame['nome']=="Distrito Federal" ), ['abrangencia']] = "3"
        self.data_frame2=data_frame
        #print(data_frame)
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', 1)
        resultado6=self.data_frame2[self.data_frame2["abrangencia"]=="4"]


    def formato_dataimesc(self):
        dataframe_organizado=pd.melt(self.data_frame2,id_vars=["serie","abrangencia","localidade","nome"],value_vars=self.anos)
        dataframe_final=dataframe_organizado[["serie","abrangencia","localidade","nome","value","variable"]]
        #dataframe_final=dataframe_organizado2.set_index("serie")
        return dataframe_final


# Iniciando a Classe
print(ANO)

for i in SERIES_N:
    teste = dataImesc(("|").join(ANO))
    print(teste)
    # Insira o número da tabela desejada abaixo
    tabela_search = int(i)
    # Pesquisa iniciada
    dataframe_Formatado = teste.procurar_tabela(tabela_search)
    dataframe_Formatado['nome']=dataframe_Formatado['nome'].str.replace(' - MA', '', regex=False)
    print(dataframe_Formatado)
    # exportando para Excel
    dataframe_Formatado.to_excel(f"resultado_serie{i}.xlsx", index=False)