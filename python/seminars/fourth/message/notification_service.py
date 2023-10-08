from seminars.fourth.message.message_service import MessageService


class NotificationService:
    def __init__(self, message_service: MessageService):
        self._message_service = message_service

    def send_notification(self, message: str, recipient: str):
        self._message_service.send_message(message, recipient)
