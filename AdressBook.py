import pickle
import random

def add_in_zap(a,b):
    global adr_data
    zap = {}
    zap['id'] = random.randint(a,b)
    zap['name'] = input('Введите имя: ')
    zap['surname'] = input('Введите фамилию: ')
    zap['adress'] = input('Введите адрес: ')
    with open(adr_data, 'ab') as f:
        pickle.dump(zap, f)
    a_b.append(zap)
    print('В книгу добавлен', zap)
    del zap
    return a_b

def zap_in_file(a_b):
    global adr_data
    with open(adr_data, 'wb') as f:
        pickle.dump(a_b, f)
    print(f"Адресная книга содержащая {count} запись, сохранена!")

def del_zap():
    global a_b
    ab_do = a_b[:]
    del_id = input('Введите "ID" контакта, который надо удалить ')
    # print(del_id)
    for i,q in enumerate(a_b.copy()):
        if str(q['id']).split()[0] in del_id:
            del a_b[i]
    print('Контакт под ID', del_id, 'удалён!') if len(ab_do) > len(a_b) else print('Такого ID нет. Никого не удалили.')
    return a_b

def open_a_b():
    global adr_data
    global a_b
    with open(adr_data, 'rb') as f:
        a_b = pickle.load(f)
    print(f'Адресная книга успешно загружена!')
    return a_b

a_b = []
count = 0
id = 0
adr_data = 'AddrBook.data'

while True:
    print('\n1. Добавить контакт\n2. Удалить контакт\n3. Показать все контакты\n'
          '4. Сохранить данные в файл\n5. Загрузить адресную книгу. \n6. Выйти\n'
          'Если ранее был создана адрессная книга настоятельно рекомендую загрузить её!\n')
    choise = input('Выберите действие: ')
    if choise == '1':
        count = len(a_b)
        add_in_zap(1,999)
        count += 1
    elif choise == '2':
        del_zap()

    elif choise == '3':
        for q in a_b:
            print('\nID: ', q['id'])
            print('Имя: ', q['name'])
            print('Фамилия: ', q['surname'])
            print('Адресс: ', q['adress'], '\n')
        # print(a_b)
    elif choise == '4':
        zap_in_file(a_b)
    elif choise == '5':
        open_a_b()
    else:

        break













