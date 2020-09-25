# -*- coding: utf-8 -*-
"""
Por Alex Cordeiro
Script rápido para analisar dados publicados no diario oficial de Santos
com o resultado da pesquisa entre pais, alunos e professores.
COVID

Licença Apache 2.0

"""

import csv
escolas_aptas = []
path = 'C:\\git\\escolas_santos\\'
with open(path + "escolas_aptas.txt", 'r', 
          encoding='utf-8') as f:
    for line in f:
        line = line.rstrip()
        pointer = line.find(" ")
        seq = line[0:pointer]
        line = line[pointer+1:]
        escolas_aptas.append(line)

categoria = ""
escolas = []
with open(path + "pesquisa_setembro.txt", 'r', 
          encoding='utf-8') as f:

    for line in f:
        line = line.rstrip()
        if not line[0].isdecimal():
            categoria  = line
        else:
            apta = "Não"
            pointer = line.find(" ")
            seq = line[0:pointer]
            line = line[pointer+1:]
            pointer = line.rfind(" ")
            nao_fav = line[pointer+1:-1]
            line = line[:pointer]
            pointer = line.rfind(" ")
            fav = line[pointer+1:-1]
            line = line[:pointer]
            for e_apta in escolas_aptas:
                if e_apta == line:
                    apta = "Sim"
                    break
            escolas.append({"categoria": categoria, 
                            "seq": seq,
                            "escola": line,
                            "fav_ret":fav,
                            "nao_fav_ret": nao_fav,
                            "apta": apta})


with open(path + "resultado.csv", mode='w', newline='') as escolas_arquivo:
    fieldnames = ["categoria",  "seq", "escola",
                  "fav_ret", "nao_fav_ret", "apta"]
    escolas_writer = csv.DictWriter(escolas_arquivo, delimiter=',', quotechar='"', 
                                    quoting=csv.QUOTE_ALL, fieldnames=fieldnames)
    escolas_writer.writeheader()
    escolas_writer.writerows(escolas)

print(escolas)    
    