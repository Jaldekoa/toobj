from toobj import ToObj
import pytest


def test_toobj():
    data = {
        'name': 'Alice',
        'age': 30,
        'address': {
            'city': 'Wonderland',
            'zipcode': 12345,
            'coordinates': {
                'lat': 52.5200,
                'long': 13.4050,
                'meta': {
                    'continent': 'Europe',
                    'population': 3000000
                }
            }
        },
        'contacts': {
            'email': 'alice@example.com',
            'phones': [
                {'type': 'home', 'number': '123-456'},
                {'type': 'work', 'number': '789-101'}
            ]
        },
        'hobbies': ['reading', 'traveling', {'name': 'coding', 'level': 'advanced'}]
    }

    obj = ToObj(data)
    assert obj.name == 'Alice'
    assert obj.address.zipcode == 12345
    assert obj.address.coordinates.meta.continent == 'Europe'
    assert obj.contacts.phones[0].number == '123-456'
    assert obj.hobbies[2].name == 'coding'