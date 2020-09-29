class Enviador:
    def __init__(self):
        self.qt_email_enviados = 0

    def enviar(self, remetente, destinatario, assunto, corpo):
        if '@' not in remetente:
            raise EmailInvalido(f'Email de remetente inválido: {remetente}')
        self.qt_email_enviados += 1
        return remetente


class EmailInvalido(Exception):
    pass
