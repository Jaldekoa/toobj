# toobj: Transform a dictionary into an object
Python package that transforms flat or nested dictionaries into objects.

## Installation
```commandline
pip install toobj
```

## ToObj
Transforms flat or nested dictionaries into objects.

### Args
| Parameter | Type   | Description                             |
|-----------|--------|-----------------------------------------|
| `d`       | `dict` | Dictionary to convert in Python object. |

```python
from toobj import ToObj

d = dict(...)
obj = ToObj(d)
```

## Usage

```python
from toobj import ToObj

# Sample data
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

# Dictionary to object
data_obj = ToObj(data)
```

```
>>> data_obj.name
'Alice'
>>> data_obj.address.zipcode
12345
>>> data_obj.address.coordinates.meta.continent
'Europe'
>>> data_obj.contacts.phones[0].number
'123-456'
>>> data_obj.hobbies[2].name
'coding'
```