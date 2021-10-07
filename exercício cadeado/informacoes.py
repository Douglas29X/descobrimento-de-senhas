from os import system

def boas_vindas():

    system('cls')
    print('  Seja bem vindo ao programa de descobrimento de senhas!\n'
    '  O objetivo desse experimento será observar o quão segura é a sua senha,\n'
    'e o quão difícil será para o programa desvendá-la.')

def pede_informacoes_usuario():

    senha = input('''\n  Para começarmos, digite sua senha a seguir, sendo que ela:
    * Deve conter apenas números e letras;
    * Deve ter de 1 a 9 caracteres;
    * Além de que serão considerados importantes caracteres minúsculos e maiúsculos. 
  Insira sua senha: ''')
    

    if len(senha) > 9:
        print('Desculpe, a senha possui tamanho inválido. Tente novamente.')
        pede_informacoes_usuario()
    
    return senha

def finaliza_programa(senha, tentativas):
    system('cls')
    print(f'''  Programa finalizado com sucesso! Segundo o programa, a sua senha era: {senha}
e o número de tentativas utilizadas para descobri-lá foi de {tentativas} tentativas''')