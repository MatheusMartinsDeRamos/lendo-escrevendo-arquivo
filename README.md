LINK DO REPLIT: https://replit.com/@Matheusmartin63/Atividade-de-Producao-Lab-Prog#main.py

Fiz um código com 4 opções, sendo elas, Ler o conteúdo de um arquivo .TXT, contar quantos caracteres contém nesse arquivo, adicionar uma frase a ele ou sair do sistema.
Dentro do código eu adicionei comentários de alguns materiais que pesquisei para fazer o código funcionar, sendo que muitas das funções eu já tinha visto em C++ ou JavaScript que são as linguagens que tenho um pouco de conhecimento.

O trabalho se concentra no “main.py”, mas eu deixei o “mainV2.py” no diretório pois pretendo ir adicionando algumas melhorias com o tempo para estudar mais Python e lógica. Como primeira mudança já adicionei uma solicitação para o usuário digitar o nome do arquivo que quer ler, e a próxima mudança que eu gostaria de fazer é, caso o arquivo não exista, perguntar se o usuário deseja criar, e caso sim, criar o arquivo no diretório do usuário.
input_nome_arquivo = input("Digite o nome do arquivo sem a extensão: ")
nome_arquivo = input_nome_arquivo + ".txt"
