def show_menu()-> int:
    print('\t    Главное меню')
    menu_list = ['Показать все контакты',
                 'Открыть файл',
                 'Сохранить файл',
                 'Создать контакт',
                 'Изменить контакт',
                 'Удалить контакт',
                 'Выход']
    for i in range(len(menu_list)):
        print(f'\t {i+1}. {menu_list[i]}')
    a = False
    while a==False:
        user_input=input('Введите команду: ')
        try:
            user_input=int(user_input)
            a=True
        except:
            print('Ошибка. Выберите пункт меню.')
        return user_input

# Функция вывода списка контактов
def show_all(db:list):
    if db_success(db):
        
        for i in range(len(db)):
            user_id = i+1
            print(f"\n{user_id}", end=". ")
            for v in db [i].values():
                print(f'{v}', end=' ')
        print('\n\n')


def db_success(db: list):
    if db:
        print('\nТелефонная книга открыта\n')
        print()
        return True
    else:
        print("\nТелефонная книга пуста или не открыта\n")
        return False

def exit_program():
    print("Завершение программы")
    exit()

def create_contact():
    print('Создание нового контакта.')
    new_contact = dict()
    
    new_contact['lastname']  = input('\t Введите фамилию: ')
    new_contact['firstname']  = input('\t Введите имя: ')
    new_contact['phone']  = input('\t Введите телефон: ')
    new_contact['comment']  = input('\t Введите комментарий: ')
    print(f"\n{new_contact}\n")
    print('\nКонтакт сохранен!\n')    
    return new_contact

def create_newcontact():
    new_contact = create_contact()
    return new_contact


def del_cont():
    print("\nДля возврата в меню введите 1901\n")
    num_contact=input('Пожалуйста, выберите id контакта для удаления!\n')
    if num_contact=='1901':
        show_menu()
    else:
        num_contact=int(num_contact)
        return num_contact


def change():
    x = False
    while x == False:
        num_contact = input("Введите порядковый номер контакта, который хотитt удалить")
        try:
            num_contact=int(num_contact)
            x= True
        except:
            print("Ошибка")
            x=True
        print(num_contact)
        return num_contact


















"""
def del_cont():
    num_contact=input('Пожалуйста, выберите id контакта для удаления!')
    num_contact=int(num_contact)
    return num_contact
"""