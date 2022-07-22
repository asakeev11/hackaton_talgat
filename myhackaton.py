import json
class Cars:
    FILE = 'myhack/myjs.json'
    id = 0
    likes = 0
    comments = []
   
    def __init__(self, brand, model, year, volume, color, body, mileage, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.volume = volume
        self.color = color
        self.body = body
        self.mileage = mileage
        self.price = price
        self.create()
    
    @classmethod
    def get_id(cls):
        cls.id += 1
        return cls.id
    
    @classmethod
    def listing(cls):
        with open(cls.FILE) as file:
            return json.load(file)

    @classmethod
    def send_data_to_json(cls, data):
        with open(cls.FILE, 'w') as file:
            json.dump(data, file)

    def create(self):
        data = Cars.listing()
        car = {
            'id' : Cars.get_id(),
            'brand' : self.brand,
            'model' : self.model,
            'year' : self.year,
            'volume' : round(self.volume, 1),
            'color' : self.color,
            'body' : self.body,
            'mileage' : self.mileage,
            'price' : round(self.price, 2),
            'likes' : self.likes,
            'comments' : self.comments
        }
        data.append(car)

        with open(Cars.FILE, 'w') as file:
            json.dump(data, file)
        return {'status' : '201', 'msg' : car}

    @classmethod
    def retrieve_car(cls, id):
        car = list(filter(lambda x: x['id'] == id, cls.listing()))
        if not car:
            return 'Нет такого автомобиля'
        return car[0]

    @classmethod
    def update_car(cls, id, **kwargs):
        data = cls.listing()
        car = cls.retrieve_car(id)
        if type(car) != dict:
            return car
        index = data.index(car)
        data[index].update(**kwargs)
        cls.send_data_to_json(data)
        return {'status' : '200', 'msg' : 'Updated'}

    @classmethod
    def delete_car(cls, id):
        data = cls.listing()
        car = cls.retrieve_car(id)
        if type(car) != dict:
            return car
        index = data.index(car)
        data.pop(index)
        cls.send_data_to_json(data)
        return {'status' : '204', 'msg' : 'deleted'}

    @classmethod
    def get_likes(cls, id):
        try:
            data = cls.listing()
            if data[id - 1]['likes'] == 0:
                data[id - 1]['likes'] += 1
                print('liked')
            else:
                data[id - 1]['likes'] -= 1
                print('unliked')
            cls.send_data_to_json(data)
        except IndexError:
            print('Нет такого автомобиля')


    @classmethod
    def get_comment(cls, id, comment):
        try:
            data = cls.listing()
            data[id - 1]['comments'].append(comment)
            cls.send_data_to_json(data)
            return 'commented'
        except IndexError:
            print('Нет такого автомобиля')

with open(Cars.FILE, 'w') as file:
    json.dump([], file)

car1 = Cars('Mercedes', 'S-Class', 2012, 4.663, 'Black', 'Sedan', 77000, 21200.5543)
car2 = Cars('Lexus', 'LX570', 2021, 5.667, 'Black', 'Jeep', 0, 145000.345)
car3 = Cars('Tesla', 'S Plaid', 2021, 0, 'Black', 'Sedan', 0, 135000.238723)

Cars.update_car(3, mileage = 100)
Cars.get_likes(1)
Cars.get_likes(2)
Cars.get_likes(3)
print(Cars.listing())

print(Cars.listing())

Cars.get_comment(1, 'Была бы белая, взял бы')
Cars.get_comment(2, 'Слишком много жрет')
Cars.get_comment(3, 'Ремонт дорогой')
print(Cars.listing())

print(Cars.delete_car(1))


'''ЗДЕСЬ МОЖНО УПРАВЛЯТЬ МАГАЗИНОМ С ПОМОЩЬЮ ТЕРМИНАЛА'''

def urls():
    
    print('Добрый день! Вас приветсвует автосалон "Super expensive cars". Вам доступны следующие функции: \n\tListOfCars - 1\n\tRetrieve - 2\n\tUpdate - 3\n\tDelete - 4\n\tLike - 5\n\tComment - 6')
    
    choice = input('Введите действие (1,2,3,4,5,6): ')
    if choice == '1':
        print(Cars.listing())
    
    elif choice == '2':
        id = int(input('Введите ID автомобиля: '))
        print(Cars.retrieve_car(id))
    
    elif choice == '3':
        id = int(input('Введите ID автомобиля: '))
        print('Что вы хотите изменить:\n\tbrand - 1\n\tmodel - 2\n\tyear - 3\n\tvolume - 4\n\tcolor - 5\n\tbody - 6\n\tmileage - 7\n\tprice - 8')
        choice = input('Введите действие (1,2,3,4,5,6,7): ')
        if choice == '1':
            new_val = input('Введите новое значение: ')
            print(Cars.update_car(id, brand = new_val))
        elif choice == '2':
            new_val = input('Введите новое значение: ')
            print(Cars.update_car(id, model = new_val))
        elif choice == '3':
            new_val = int(input('Введите новое значение: '))
            print(Cars.update_car(id, year = new_val))
        elif choice == '4':
            new_val = float(input('Введите новое значение: '))
            print(Cars.update_car(id, volume = round(new_val, 1)))
        elif choice == '5':
            new_val = input('Введите новое значение: ')
            print(Cars.update_car(id, color = new_val))
        elif choice == '6':
            new_val = input('Введите новое значение: ')
            print(Cars.update_car(id, body = new_val))
        elif choice == '7':
            new_val = int(input('Введите новое значение: '))
            print(Cars.update_car(id, mileage = new_val))
        elif choice == '8':
            new_val = float(input('Введите новое значение: '))
            print(Cars.update_car(id, price = round(new_val, 2)))
        else:
            print('Отсутствует значение')
    
    elif choice == '4':
        id = int(input('Введите ID автомобиля: '))
        print(Cars.delete_car(id))
    
    elif choice == '5':
        id = int(input('Введите ID автомобиля: '))
        print(Cars.get_likes(id))
    
    elif choice == '6':
        id = int(input('Введите ID автомобиля: '))
        comment = input('Напишите комментарий: ')
        print(Cars.get_comment(id, comment))
    else:
        print('Invalid choice!')
        urls()
    
    ask = input('Хотите продолжить\'?(YES/NO)\n\t')
    if ask.lower() == 'yes':
        urls()
    else:
        print('Bye!')
   
    print('Нет такого автомобиля')
urls()
