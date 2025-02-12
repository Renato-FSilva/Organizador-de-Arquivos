import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Seleciona uma pasta")

lista_arquivos = os.listdir(caminho)

locais = {
    "imagens": [".png", ".jpg", ".jpeg"],
    "videos": [".mp4"],
    "panilhas": [".xlsx"],
    "pdfs": [".pdf"],
    "csv": [".csv"]
}

for arquivos in lista_arquivos:
    #01. Arquivo.pdf
    nome, extensao = os.path.splitext(f'{caminho}/{arquivos}')
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivos}", f"{caminho}/{pasta}/{arquivos}")