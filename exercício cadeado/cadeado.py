
class Cadeado:
    def __init__(self, senha):
        self.__senha = senha
        
    @property
    def senha(self):
        return self.__senha


def descobre_senha(cadeado):
    tentativas = 1
    termina = False
    senha_descoberta = ''
    seta = 0
    linha_leitura = 0

    while not termina:
        with open('variaveis.csv', 'r') as arquivo:
            letras = arquivo.read().replace('\n', '')
            letra = letras[linha_leitura]
            print(letra)
            print(cadeado.senha[seta])
            if letra != cadeado.senha[seta]:
                tentativas+= 1
                linha_leitura+= 1
            else:
                senha_descoberta+= senha_descoberta.join(letra)
                seta+= 1
                linha_leitura = 0
            if cadeado.senha == senha_descoberta:
                termina = True
    return senha_descoberta, tentativas - tentativas//2