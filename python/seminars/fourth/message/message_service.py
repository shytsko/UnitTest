class MessageService:

    @staticmethod
    def send_message(message: str, recipient: str):
        print(f"Отправка сообщения '{message}' получателю {recipient}")
