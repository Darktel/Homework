from person import Person           # импортирует наши классы
from person import Manager
bob = Person('Bob Smith')           # создание  обьектов для сохранения
sue = Person ('Sue jonse', job = 'dev', pay = 10000)
tom = Manager ('Tom Jonse', 50000)

import shelve
db = shelve.open('persondb')    # Имя файла хранилища
for object in (bob, sue, tom):  # Вкачестве ключа используеться атрибут name
    db[object.name] = object    # Сохранить объект
db.close()                      # Закрыть после внесения изменений
