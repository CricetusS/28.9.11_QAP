from api.client import booker_client
from resources.prepare_data import prepare_data
from serializers.bookers import BookingModel, LiteBookingModel, Token, FilterModel

token = ''  # Получить токен после авторизации
booking_id = 0  # Тестовый id


# Проверка получения токена
def test_token():
    global token

    new_token = booker_client.create_token(prepare_data('token'))
    token = new_token.json()['token']

    assert new_token.status_code == 200, f'{new_token.json()}'
    # Проверка обязательного поля token в ответе
    assert Token(**new_token.json()).dict()
    assert token != ''


# Проверка получения списка броней
def test_list_booking():
    filters = prepare_data('filter')

    # Проверка соответствия полей запроса
    assert FilterModel(**filters).dict()

    list_of_bookings = booker_client.get_list_of_bookings(token, filters)

    assert list_of_bookings.status_code == 200, f'{list_of_bookings.json()}'


# Проверка создания брони
def test_create_booking():
    global booking_id

    booking = prepare_data('booking')
    create_booking = booker_client.create_booking(token, booking)
    booking_id = create_booking.json()['bookingid']

    get_booking = booker_client.get_booking(token, booking_id)

    assert get_booking.status_code == 200, f'{get_booking.json()}'
    # Проверка соответствия полей запроса и ответа с проверкой обязательных полей
    assert BookingModel(**booking).dict() == BookingModel(**get_booking.json()).dict()


# Проверка получения информации о брони
def test_get_booking():
    global booking_id

    if booking_id == 0:
        filters = []
        list_of_bookings = booker_client.get_list_of_bookings(token, filters)
        booking_id = list_of_bookings.json()[0]['bookingid']
    get_booking = booker_client.get_booking(token, booking_id)

    assert get_booking.status_code == 200, f'{get_booking.json()}'
    # Проверка соответствия полей запроса и ответа с проверкой обязательных полей
    assert BookingModel(**get_booking.json()).dict()


# Проверка изменения брони
def test_update_booking():
    global booking_id
    if booking_id == 0:
        filters = []
        list_of_bookings = booker_client.get_list_of_bookings(token, filters)
        booking_id = list_of_bookings.json()[0]['bookingid']

    booking = prepare_data('full_change_booking')
    update_booking = booker_client.update_booking(token, booking_id, booking)

    assert update_booking.status_code == 200, f'{update_booking.json()}'
    # Проверка соответствия полей запроса и ответа с проверкой обязательных полей
    assert BookingModel(**booking).dict() == BookingModel(**update_booking.json()).dict()


# Проверка частичного изменения брони
def test_partial_update_booking():
    global booking_id
    if booking_id == 0:
        filters = []
        list_of_bookings = booker_client.get_list_of_bookings(token, filters)
        booking_id = list_of_bookings.json()[0]['bookingid']

    booking = prepare_data('part_change_booking')
    update_booking = booker_client.update_booking(token, booking_id, booking)

    assert update_booking.status_code == 200, f'{update_booking.json()}'
    # Проверка соответствия полей запроса и ответа с проверкой обязательных полей
    assert LiteBookingModel(**booking).dict() == LiteBookingModel(**update_booking.json()).dict()


# Проверка удаления брони
def test_delete_booking():
    global booking_id
    if booking_id == 0:
        filters = []
        list_of_bookings = booker_client.get_list_of_bookings(token, filters)
        booking_id = list_of_bookings.json()[0]['bookingid']

    delete_booking = booker_client.update_booking(token, booking_id)

    assert delete_booking.status_code == 200, f'{delete_booking.url}'
