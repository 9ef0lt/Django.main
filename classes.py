class Person:
    # if zapros=='Oleg'
        ves = '45KG'
        rost = '190cm'
        def __init__(self, name):
            self.name = name
        def display_info(self):
            print('Меня зовут', self.name)
        def display_info2(self):
            print('Мой рост: ',self.rost,'Мой вес: ',self.ves)

class Person2:
    # if zapros=="Audi"
    color='Red'
    put='65km'
    def __init__(self, name):
        self.name = name
    def display_info(self):
        print('Марка:', self.name)
    def display_info2():
        print('Цвет:', color, 'Расстояние авто:', put)







# person1 = Person('oleg','33','SPB')
# person1.display_info()