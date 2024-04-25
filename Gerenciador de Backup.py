import os  	# fazer uma lista com os arquivos da pasta
from tkinter.filedialog import askdirectory	 # abrir janelas para selecionar uma pasta do computador
import shutil        #Copiar arquivos, copiar pastas e verificar se a pasta já existe ou não
import datetime      #Conseguir pegar uma data

#Selecionando a pasta
nome_pasta_selecionada = askdirectory()
 
#Fazendo uma lista de arquivos dentro dessa pasta
lista_arquivos = os.listdir(nome_pasta_selecionada)

#Lugar onde a pasta backup vai ser criada
nome_pasta_backup = "backup"
nome_completo_pasta_backup = f"{nome_pasta_selecionada}/{nome_pasta_backup}"
#Verificando se a pasta existe ou nao
if not os.path.exists(nome_completo_pasta_backup):
	os.mkdir(nome_completo_pasta_backup)

#Pegando a data atual
data_atual = datetime.datetime.today().strftime("%Y-%m-%d %H%M%S")

#Copiando os arquivos e colando na pasta de destino final
for arquivo in lista_arquivos:
	nome_completo_arquivo = f"{nome_pasta_selecionada}/{arquivo}"
	nome_final_arquivo = f"{nome_completo_pasta_backup}/{data_atual}/{arquivo}"

	if not os.path.exists(f"{nome_completo_pasta_backup}/{data_atual}"):
		os.mkdir(f"{nome_completo_pasta_backup}/{data_atual}")

	if "." in arquivo:
		shutil.copy2(nome_completo_arquivo, nome_final_arquivo)
	elif "backup" != arquivo:
		shutil.copytree(nome_completo_arquivo, nome_final_arquivo)

print("Backup realizado!")
	
	


