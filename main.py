nome_arquivo = "texto.txt"

while True:
    print("----------------------------------------------")
    print("MENU")
    print("1. Ler arquivo")
    print("2. Adicionar texto no arquivo")
    print("3. Saber quantidade de caracteres do arquivo")
    print("4. Sair do sistema")

    menu = input("Digite o número da opção desejada: ")
    
    # verifica a opção selecionada
    if menu == "1":
        # Abrindo e lendo o arquivo. Utilizando 'r' pois é só leitura 
        # Fonte: https://diegomariano.com/manipulando-arquivos/#:~:text=Para%20abrir%20um%20arquivo%20de,abertura%20do%20arquivo%20(opcional).
        with open(nome_arquivo, 'r') as arquivo:
            conteudo_arquivo = arquivo.read()
            print("----------------------------------------------")
            print(f"Conteúdo do arquivo:\n\n{conteudo_arquivo}")

    elif menu == "2":
        # Solicitando uma frase para adicionar ao arquivo
        # Fonte: https://pythonacademy.com.br/blog/input-e-print-entrada-e-saida-de-dados-no-python
        frase = input("Digite uma frase para ser adicionada ao arquivo: \n")
        # Abrindo o arquivo em modo escrita e adicionando a frase digitada anteriormente
        with open(nome_arquivo, 'a') as arquivo:
            arquivo.write("\n" + frase)
        print("Frase adicionada com sucesso!")
      
    elif menu == "3":
        # Fonte: https://www.pythonprogressivo.net/2018/10/Strings-O-que-sao-Como-usar-Acessar-Caracteres-Tamanho-len.html#:~:text=Uma%20fun%C3%A7%C3%A3o%20nativa%20do%20Python,tem%20vinte%20e%20quatro%20caracteres.
        with open(nome_arquivo, 'r') as arquivo:
            conteudo_arquivo = arquivo.read()
            num_caracteres = len(conteudo_arquivo)
            print(f"\n\nNúmero de caracteres no arquivo: {num_caracteres}")
          
    elif menu == "4":
        print("Saindo do sistema...")
        break # interrompe o loop e finaliza o programa
    else:
        print("Opção inválida!")
