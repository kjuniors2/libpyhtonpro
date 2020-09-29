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
    enviador = Enviador()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'junior@foo.bar',
        'Curso de Python',
        'Confira os modulos saso fantasticos'
    )
    assert len(usuarios) == enviador.qt_email_enviados
