class Category:

    def __init__(self, num, name):
        self.num = num
        self.name = name

    """""
            Функция выбора категории товара
    """""
    @staticmethod
    def checCategory():
        category_list = {1: 'Фрукты',
                         2: 'Овощи',
                         3: 'Напитки',
                         4: 'Молочные продукты',
                         5: 'Хлеб'
                         }
        print(category_list)
