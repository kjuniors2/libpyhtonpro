import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Junior', email='junior@python.pro.br'),
            Usuario(nome='LinuxPro', email='junior@python.pro.br'),
        ],
        [
            Usuario(nome='Junior', email='junior@python.pro.br'),
        ]

    ],
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'junior@foo.bar',
        'Curso de Python',
        'Confira os modulos saso fantasticos'
    )
    assert len(usuarios) == enviador.qt_email_enviados

class EnviadorMock(Enviador):
    def __init__(self):
        super().__init__()
        self.parametros_de_envio = None
        self.qt_email_enviados = 0

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.paramentros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qt_email_enviados += 1


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Junior', email='junior@foo.bar')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'junior@foo.bar',
        'Curso de Python',
        'Confira os modulos saso fantasticos'
    )
    assert enviador.paramentros_de_envio == (
        'junior@foo.bar',
        'junior@foo.bar',
        'Curso de Python',
        'Confira os modulos saso fantasticos',
    )
