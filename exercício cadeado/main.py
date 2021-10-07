from cadeado import Cadeado, descobre_senha
from informacoes import boas_vindas, finaliza_programa, pede_informacoes_usuario


def roda():
    boas_vindas()

    senha = pede_informacoes_usuario()

    cadeado_usuario = Cadeado(senha)

    senha_descoberta, tentativas = descobre_senha(cadeado_usuario)

    finaliza_programa(senha_descoberta, tentativas)

if __name__ == '__main__':
    roda()