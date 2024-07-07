class NotificationService:
    def notificar(self, mensagem, usuarios):
        for usuario in usuarios:
            print(f"Notificando {usuario.nome}: {mensagem}")

class BookAvailabilityNotifier:
    def __init__(self, notification_service):
        self.notification_service = notification_service

    def notificar_disponibilidade(self, livro, usuarios):
        mensagem = f"O livro '{livro['titulo']}' está disponível."
        self.notification_service.notificar(mensagem, usuarios)