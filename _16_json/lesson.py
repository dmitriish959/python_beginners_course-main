# Распоковка book в json_string

import json

book = {
    'title': '1984',
    'author': 'George Orwell',
    'isbn': '978-0451524935',
    'uuid': 'a3b3r3a-k1a2d3a4b6r4a'
}

json_string = json.dumps(book)

print(type(json_string))
print(json_string)

json_string = '{"title": "1984", "author": "George Orwell", "isbn": "978-0451524935", "uuid": "a3b3r3a-k1a2d3a4b6r4a"}'
