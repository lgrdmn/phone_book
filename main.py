import json


def get_phonebook():
    """Считывание телефонного справочника"""
    with open('phone_book.json', 'r') as file:
        return json.load(file)


def write_json(subs):
    """Запись абонента в телефонный справочник"""
    with open('phone_book.json', 'w') as file:
        json.dump(subs, file)


def add_subscriber():
    """Добавление абонента в телефонный справочник"""
    subscriber = dict()
    subscriber["first_name"] = input("Введите имя абонента: ")
    subscriber["last_name"] = input("Введите фамилию абонента: ")
    subscriber["phone_number"] = input("Введите телефонный номер абонента: ")
    subscriber["street_name"] = input("Введите улицу абонента: ")
    subscriber["house_number"] = input("Введите номер дома абонента: ")
    phonebook = get_phonebook()
    for sub in phonebook:
        if subscriber["phone_number"] == sub["phone_number"]:
            print('Абонент c таким номером телефона уже есть в телефонном справочнике:', sub["first_name"],
                  sub["last_name"], sub["phone_number"], sub["street_name"], sub["house_number"])
            return
    phonebook.append(subscriber)
    write_json(phonebook)
    print('Абонент:', subscriber["first_name"], subscriber["last_name"], subscriber["phone_number"],
          subscriber["street_name"], subscriber["house_number"], 'добавлен в телефонный справочник')


def find_subscriber():
    """Поиск абонента в телефонном справочнике по номеру телефона"""
    find_number = input("Введите телефонный номер абонента которого хотите НАЙТИ: ")
    phonebook = get_phonebook()
    for sub in phonebook:
        if find_number == sub["phone_number"]:
            print('Абонент есть в телефонном справочнике:', sub["first_name"], sub["last_name"],
                  sub["phone_number"], sub["street_name"], sub["house_number"])
            return
    print('Абонент отсутствует в телефонном справочнике.')


def del_subscriber():
    """Удаление абонента из телефонного справочника по номеру телефона"""
    del_number = input("Введите телефонный номер абонента которого хотите УДАЛИТЬ: ")
    phonebook = get_phonebook()
    for sub in phonebook:
        if del_number == sub["phone_number"]:
            print('Абонент:', sub["first_name"], sub["last_name"], sub["phone_number"],
                  sub["street_name"], sub["house_number"], 'удалён из телефонного справочника')
            phonebook.remove(sub)
            write_json(phonebook)
            return
    print('Абонент отсутствует в телефонном справочнике.')


while True:
    command = input('Введите A, если хотите добавить абонента \n'
                    'Введите D, если хотите удалить абонента \n'
                    'Введите F, если хотите найти абонента \n'
                    'Введите E, если хотите выйти \n')
    if command == 'A' or command == 'a':
        add_subscriber()
    elif command == 'D' or command == 'd':
        del_subscriber()
    elif command == 'F' or command == 'f':
        find_subscriber()
    elif command == 'E' or command == 'e':
        break
    else:
        print('Вы ввели неверную команду.')
