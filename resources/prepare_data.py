def prepare_data(arg):
    # Метод подготовки тестовых данных
    data = {}
    if arg == 'booking':
        data = {
            'firstname': 'Test',
            'lastname': 'Testenko',
            'totalprice': 450,
            'depositpaid': True,
            "bookingdates": {
                'checkin': "2023-05-10",
                'checkout': "2023-05-20"
            },
            'additionalneeds': 'breakfast included'
        }
    elif arg == 'full_change_booking':
        data = {
            'firstname': 'Test',
            'lastname': 'Testov',
            'totalprice': 250,
            'depositpaid': True,
            "bookingdates": {
                'checkin': "2023-05-10",
                'checkout': "2023-03-15"
            },
        }
    elif arg == 'part_change_booking':
        data = {
            'totalprice': 250,
            "bookingdates": {
                'checkout': "2023-05-10"
            },
        }
    elif arg == 'token':
        data = {
            "username": "admin",
            "password": "password123"
        }
    elif arg == 'filter':
        data = {
            "firstname": "Test"
        }
    return data
