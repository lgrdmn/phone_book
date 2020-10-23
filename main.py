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


def add_subscriber(pnum, fname, lname, streetname, hnum):
    """Добавление абонента в телефонный справочник"""
    subscriber = ['', '', '', '', '']
    check = one_subscriber_finder(pnum)
    print(check)
    if check:
        message = 'Абонент c таким номером телефона уже есть в телефонном справочнике'
        pnum = check[0][0]
        fname = check[0][1]
        lname = check[0][2]
        streetname = check[0][3]
        hnum = check[0][4]
    else:
        subscriber[0] = pnum
        subscriber[1] = fname
        subscriber[2] = lname
        subscriber[3] = streetname
        subscriber[4] = hnum
        subscriber = tuple(subscriber)
        add_values_to_db(subscriber)
        message = 'Абонент добавлен в телефонный справочник.'
    return message, pnum, fname, lname, streetname, hnum


def find_subscriber(find_number):
    """Поиск абонента в телефонном справочнике по номеру телефона"""
    check = one_subscriber_finder(find_number)
    if check:
        message = 'Абонент есть в телефонном справочнике:'
        pnum = check[0][0]
        fname = check[0][1]
        lname = check[0][2]
        streetname = check[0][3]
        hnum = check[0][4]
    else:
        message = 'Абонент отсутствует в телефонном справочнике.'
        pnum = ''
        fname = ''
        lname = ''
        streetname = ''
        hnum = ''
    return message, pnum, fname, lname, streetname, hnum


def del_subscriber(del_number):
    """Удаление абонента из телефонного справочника по номеру телефона"""
    check = one_subscriber_finder(del_number)
    if check:
        conn = sqlite3.connect('phone_book.db')
        cur = conn.cursor()
        cur.execute("DELETE FROM subscribers WHERE phone_number=?;", (del_number,))
        message = 'Абонент удалён из телефонного справочника'
        pnum = check[0][0]
        fname = check[0][1]
        lname = check[0][2]
        streetname = check[0][3]
        hnum = check[0][4]
        conn.commit()
        conn.close()
    else:
        message = 'Абонент отсутствует в телефонном справочнике.'
        pnum = ''
        fname = ''
        lname = ''
        streetname = ''
        hnum = ''
    return message, pnum, fname, lname, streetname, hnum


def update_subscriber(pnum, fname, lname, streetname, hnum):
    """Изменение данных абонента в телефонном справочнике"""
    check = one_subscriber_finder(pnum)
    if check:
        conn = sqlite3.connect('phone_book.db')
        cur = conn.cursor()
        cur.execute("UPDATE subscribers SET 'phone_number'=?, 'first_name'=?, 'last_name'=?, "
                    "'street_name'=?, 'house_number'=? WHERE phone_number=?;",
                    (pnum, fname, lname, streetname, hnum, pnum))
        conn.commit()
        message = 'Данные абонента изменены в телефонном справочнике'
        conn.commit()
        conn.close()
    else:
        message = 'Абонент с таким номером телефона отсутствует в телефонном справочнике.'
        pnum = ''
        fname = ''
        lname = ''
        streetname = ''
        hnum = ''
    return message, pnum, fname, lname, streetname, hnum


if __name__ == '__main__':
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
