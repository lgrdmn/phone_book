import sqlite3


def creator_db():
    """Создание базы данных"""
    conn = sqlite3.connect('phone_book.db')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS subscribers(
    phone_number TEXT,
    first_name TEXT,
    last_name TEXT,
    street_name TEXT, 
    house_number TEXT);
    """)
    conn.commit()
    conn.close()


def all_subscribers():
    """Загрузка всех абонентов из базы данных"""
    conn = sqlite3.connect('phone_book.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM subscribers;")
    all_results = cur.fetchall()
    conn.close()
    return all_results


def one_subscriber_finder(phone_number):
    """Поиск абонента по номеру телефона"""
    conn = sqlite3.connect('phone_book.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM subscribers WHERE phone_number=?;", (phone_number,))
    all_results = cur.fetchall()
    conn.close()
    return all_results


def add_values_to_db(user):
    """Запись в телефонный справочник"""
    conn = sqlite3.connect('phone_book.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO subscribers VALUES(?, ?, ?, ?, ?);", user)
    conn.commit()
    conn.close()


def add_subscriber():
    """Добавление абонента в телефонный справочник"""
    subscriber = ['', '', '', '', '']
    subscriber[0] = input("Введите телефонный номер абонента: ")
    check = one_subscriber_finder(subscriber[0])
    if check:
        print('Абонент c таким номером телефона уже есть в телефонном справочнике:', check[0][0],
              check[0][1], check[0][2], check[0][3], check[0][4])
        return
    subscriber[1] = input("Введите имя абонента: ")
    subscriber[2] = input("Введите фамилию абонента: ")
    subscriber[3] = input("Введите улицу абонента: ")
    subscriber[4] = input("Введите номер дома абонента: ")
    subscriber = tuple(subscriber)
    add_values_to_db(subscriber)
    print('Абонент:', subscriber[0], subscriber[1], subscriber[2], subscriber[3], subscriber[4],
          'добавлен в телефонный справочник')


def find_subscriber():
    """Поиск абонента в телефонном справочнике по номеру телефона"""
    find_number = input("Введите телефонный номер абонента которого хотите НАЙТИ: ")
    check = one_subscriber_finder(find_number)
    if check:
        print('Абонент есть в телефонном справочнике:', check[0][0],
              check[0][1], check[0][2], check[0][3], check[0][4])
        return
    print('Абонент отсутствует в телефонном справочнике.')


def del_subscriber():
    """Удаление абонента из телефонного справочника по номеру телефона"""
    del_number = input("Введите телефонный номер абонента которого хотите УДАЛИТЬ: ")
    check = one_subscriber_finder(del_number)
    if check:
        conn = sqlite3.connect('phone_book.db')
        cur = conn.cursor()
        cur.execute("DELETE FROM subscribers WHERE phone_number=?;", (del_number,))
        print('Абонент:', check[0][0], check[0][1], check[0][2],
              check[0][3], check[0][4], 'удалён из телефонного справочника')
        conn.commit()
        conn.close()
        return
    print('Абонент отсутствует в телефонном справочнике.')


def update_subscriber():
    """Изменение данных абонента в телефонном справочнике"""
    update_number = input("Введите телефонный номер абонента данные которого хотите ИЗМЕНИТЬ: ")
    check = one_subscriber_finder(update_number)
    if check:
        print('Данные абонента которого вы хотите ИЗМЕНИТЬ:', check[0][0],
              check[0][1], check[0][2], check[0][3], check[0][4])
        action = input('Вы уверены, что хотите внести изменения? Y/N \n')
        if action == 'Y' or action == 'y':
            conn = sqlite3.connect('phone_book.db')
            cur = conn.cursor()
            cur.execute("DELETE FROM subscribers WHERE phone_number=?;", (update_number,))
            conn.commit()
            subscriber = ['', '', '', '', '']
            subscriber[0] = input("Введите НОВЫЙ телефонный номер абонента: ")
            subscriber[1] = input("Введите НОВОЕ имя абонента: ")
            subscriber[2] = input("Введите НОВУЮ фамилию абонента: ")
            subscriber[3] = input("Введите НОВУЮ улицу абонента: ")
            subscriber[4] = input("Введите НОВЫЙ номер дома абонента: ")
            subscriber = tuple(subscriber)
            add_values_to_db(subscriber)
            print('Данные абонента:', subscriber[0], subscriber[1], subscriber[2], subscriber[3],
                  subscriber[4], 'изменены в телефонный справочник')
            conn.commit()
            conn.close()
        elif action == 'N' or action == 'n':
            pass
        return
    print('Абонент отсутствует в телефонном справочнике.')


creator_db()
print(all_subscribers())

while True:
    command = input('Введите A, если хотите добавить абонента \n'
                    'Введите D, если хотите удалить абонента \n'
                    'Введите F, если хотите найти абонента \n'
                    'Введите U, если хотите изменить данные абонента \n'
                    'Введите E, если хотите выйти \n')
    if command == 'A' or command == 'a':
        add_subscriber()
    elif command == 'D' or command == 'd':
        del_subscriber()
    elif command == 'F' or command == 'f':
        find_subscriber()
    elif command == 'U' or command == 'u':
        update_subscriber()
    elif command == 'E' or command == 'e':
        break
    else:
        print('Вы ввели неверную команду.')

