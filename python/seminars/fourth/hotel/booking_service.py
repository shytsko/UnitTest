from seminars.fourth.hotel.hotel_service import HotelService


class BookingService:
    def __init__(self, hotel_service: HotelService):
        self._hotel_service = hotel_service

    def book_room(self, room_id: int):
        if self._hotel_service.is_room_available(room_id):
            # Код, который бронирует номер.
            # Логика бронирования комнаты
            # В реальном приложении здесь бы было больше кода
            return True
        else:
            return False
