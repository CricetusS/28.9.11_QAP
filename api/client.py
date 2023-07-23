import requests
import json


class Booker:
    url = "https://restful-booker.herokuapp.com"

    def __header__(self, token):
        headers = {'Content-Type': 'application/json', 'Cookie': f'{token}'}
        return headers

    # Создание токена
    def create_token(self, token):
        headers = {'Content-Type': 'application/json'}
        data = json.dumps(token)
        return requests.post(self.url + '/auth', headers=headers, data=data)

    # Создание бронирования
    def create_booking(self, token, booking):
        data = json.dumps(booking)
        return requests.post(self.url + '/booking', headers=self.__header__(token), data=data)

    # Получение бронирования
    def get_booking(self, token, booking_id):
        return requests.get(self.url + f'/booking/{booking_id}', headers=self.__header__(token))

    # Получение списка бронирований
    def get_list_of_bookings(self, token, filters):
        return requests.get(self.url + '/booking', headers=self.__header__(token), params=filters)

    # Обновление бронирования по id
    def update_booking(self, token, booking_id, booking):
        data = json.dumps(booking)
        return requests.put(self.url + f'/booking/{booking_id}', headers=self.__header__(token), data=data)

    # Удаление бронирования по id
    def delete_booking(self, token, booking_id):
        return requests.delete(self.url + f'/booking/{booking_id}', headers=self.__header__(token))


booker_client = Booker()
