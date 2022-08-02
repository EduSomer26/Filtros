import csv

title_len_limit = 20

obj = {
    "titulo": str(),
    "conteudo":list()
    }
    
general = list()

conteudo_lista = []

with open("ECG\EEG_orig.dat") as eeg:
    lines = eeg.readlines()
    lines = [line.rstrip() for line in lines]

for i in range(0, 20):

    if len(lines[i].replace(";", "\n")) < title_len_limit:
            obj["titulo"] = lines[i].replace(";", "\n")
            titulo2 = obj["titulo"]
    else:
        conteudo_lista.append(lines[i].replace(";", "\n"))
        obj["conteudo"] = conteudo_lista

    if len(lines[i].replace(";", "\n")) < title_len_limit:

        general.append(obj)
        obj = {
                "titulo": str(),
                "conteudo":list()
                }

with open('teste_leitura1.csv','w') as arquivo:
    writer = csv.writer(arquivo)
    for elm in conteudo_lista[:3]:
        writer.writerow([elm])

