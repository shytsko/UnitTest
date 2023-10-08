# Вам нужно написать тест с использованием моков для сервиса отправки сообщений.
# Условие: У вас есть класс MessageService с методом public void sendMessage(String message, String
# recipient), который отправляет сообщение получателю.
# Вам необходимо проверить правильность работы класса NotificationService, который использует
# MessageService для отправки уведомлений.

from mockito import mock, verify, when

from seminars.fourth.message.message_service import MessageService
from seminars.fourth.message.notification_service import NotificationService


class TestNotificationService:
    def test_send_massage(self):
        mock_message_service = mock(MessageService)
        notification_service = NotificationService(mock_message_service)
        when(mock_message_service).send_message(...).thenReturn()

        notification_service.send_notification("message", "recipiet")

        verify(mock_message_service, times=1).send_message("message", "recipiet")