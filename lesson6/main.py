# Creates string of values separated by any symbols
def create_value(line, offset=0, sep=' '):
    value = ''
    for i in range(len(line) - offset):
        value += line[i]
        if i < len(line) - offset - 1:
            value += sep
    return value


# Creates an entry from the string
def create_record_from_line(line):
    line = line.split(', ')
    name = create_value(line, offset=1)
    phone = line[-1]
    return [name, phone]


# Creates virtual phonebook from database
def create_book_from_db(path):
    data = open(path, 'r')
    book = list(map(create_record_from_line, data))
    for i in range(len(book)):
        book[i].insert(0, f'{i}')
    data.close()
    return book


# Write line to database
def write_data(path, line):
    data = open(path, 'a')
    data.write(line)
    data.close()


# Rewrite database with new data
def rewrite_data(path, book):
    open(path, 'w')
    for record in book:
        line = f"{create_value(record[1].split(' '), sep=', ')}, {record[2]}"
        write_data(path, line)


# Create and write line to db
def input_record(path):
    reqs = ['Введите фамилию: ',
            'Введите имя: ',
            'Введите отчество: ',
            'Введите номер телефона: ']
    line = create_value(list(map(lambda r: input(r), reqs)), sep=', ') + '\n'
    write_data(path, line)


# Delete entry from DB
def del_record(path, rec_id):
    book = create_book_from_db(path)
    book.remove(book[rec_id])
    rewrite_data(path, book)


# Edit phone number
def edit_record(path, rec_id):
    book = create_book_from_db(path)
    record = book[rec_id]
    print(f'ФИО: {record[1]}')
    print(f'Старый телефон: {record[2]}')
    record[2] = input('Введите новый номер телефона: ') + '\n'
    show_record(record)
    rewrite_data(path, book)


# Find list of records in phonebook
def find_records(val, book):
    res = list(filter(lambda rec:
                      list(filter(lambda r:
                                  val.upper() in r.upper(), rec)), book))
    return res


def show_book(book):
    for record in book:
        show_record(record)


def show_record(record):
    print(f'ID: {record[0]} ')
    print(f'ФИО: {record[1]} ')
    print(f'Телефон: {record[2]} ')


def main():
    command = input('\
    __________________________________________\n\
    :1 - Показать все записи\n\
    :4 - Добавить новый контакт\n\
    :5 - Удалить контакт\n\
    :6 - Изменить номер телефона у контакта\n\
    :7 - Выход\n\
    Введите запрос (имя, телефон или ID) или номер команды через двоеточие - ')

    path = 'phone_book.txt'
    book = create_book_from_db(path)
    if command == ':1':
        show_book(book)
    elif command == ':4':
        input_record(path)
    elif command == ':5':
        del_record(path, int(input('Введите ID записи: ')))
    elif command == ':6':
        edit_record(path, int(input('Введите ID записи: ')))
    elif command == ':7':
        exit()
    else:
        show_book(find_records(command, book))


if __name__ == "__main__":
    main()
