from users import User
from Item import Item
from category import Category

basket = []

if __name__ == '__main__':
    user = User(login='Kukushka', password='12345')
    password_valid = False
    while not password_valid:
        print('Введите логин: ')
        login = input()
        print('Введите пароль: ')
        password = input()
        if user.login == login and user.password == password:
            print('Регистрация прошла успешно!')
            password_valid = True
        else:
            print('Логин или пароль не верные!')


if __name__ == '__main__':
    category = Category
    category.checCategory()
    item = Item



    """""""""
    Список товаров:
    """""""""

    a = int(input('Введите номер категории: '))
    lines1 = []
    if a == 1:
        with open(r"spisok.txt", "r", encoding='utf-8') as f:
            print("".join(f.readlines()[1:14]))
    lines1 = []
    if a == 2:
        with open(r"spisok.txt", "r", encoding='utf-8') as f:
            print("".join(f.readlines()[15:26]))
    lines1 = []
    if a == 3:
        with open(r"spisok.txt", "r", encoding='utf-8') as f:
            print("".join(f.readlines()[27:38]))

    lines1 = []
    if a == 4:
        with open(r"spisok.txt", "r", encoding='utf-8') as f:
            print("".join(f.readlines()[39:53]))

    lines1 = []
    if a == 5:
        with open(r"spisok.txt", "r", encoding='utf-8') as f:
            print("".join(f.readlines()[56:66]))
    if a > 5:
        print('Выбранной категории не существует'), exit()

    interview = {}
    active = True
    while active:
        with open(r"spisok.txt", "r", encoding='utf-8') as f:
            good = input('Ведите наименование товара: ')
            if good in f.read():
                print("Товар добавлен в карзину")
                basket.append(good)
                print(basket)
            else: print('Данного товара нет в продаже')
            repeat = str(input("Желаете продолжить покупки? (y/n): "))
            if repeat not in 'y' and repeat not in 'n':
                continue
            if repeat in 'y':
                continue
            elif repeat in 'n':
                print('Покупка завершена')
                break










