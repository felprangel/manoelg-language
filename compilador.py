import sys

#Lê o argumento passado no cmd
nome_arquivo = sys.argv[1]

#Printa uma ajuda no cmd caso o usuário use -h ou --help como argumento
if nome_arquivo == "-h" or nome_arquivo == '--help':
	print("Sintaxe 'python interpreter.py [arquivo]’")
	sys.exit()
else:
	#Abre o arquivo caso o usuário tenha passado o nome de uma arquivo como argumento
	arquivo = open(nome_arquivo)

#Lê as linhas do arquivo
linhas = arquivo.readlines()

for i in linhas:
	if len(i) > 2:
		for j in range(len(i)-1):
			if i[j] == 'b':
				print("É Bom Demaize Meuzamigo!")
			else:
				print("Error")	
				break
	elif i[0] == 'b':
		print("Bom Demaize!")
	else:
		print("Error")


