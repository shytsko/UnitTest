# Вам необходимо написать тест с использованием моков для сервиса бронирования отелей.
# Условие: У вас есть класс HotelService с методом public boolean isRoomAvailable(int roomId),
# который обычно проверяет, доступен ли номер в отеле.
# Вам необходимо проверить правильность работы класса BookingService, который
# использует HotelService для бронирования номера, если он доступен
from mockito import mock, verify, when

from seminars.fourth.hotel.booking_service import BookingService
from seminars.fourth.hotel.hotel_service import HotelService


class TestBookingService:
    def test_room_available(self):
        mock_hotel_service = mock(HotelService)
        when(mock_hotel_service).is_room_available(...).thenReturn(True)
        booking_service = BookingService(mock_hotel_service)
        room_num = 10

        res = booking_service.book_room(room_num)

        verify(mock_hotel_service).is_room_available(room_num)
        assert res
