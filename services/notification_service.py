from repositories.usuario_repository import UsuarioRepository

class NotificationService:
    def __init__(self):
        self.usuario_repository = UsuarioRepository()
        
    def notificar_disponibilidade(self, livro_titulo):
        usuarios = self.usuario_repository.buscar_usuarios()
        mensagem = f"O livro {livro_titulo} está disponível para empréstimo!"
        for usuario in usuarios:
            self.enviar_notificacao(usuario, mensagem)
    
    def enviar_notificacao(self, usuario, mensagem):
        print(f"Enviando notificação para {usuario}: {mensagem}")