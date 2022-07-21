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
            else:
                data[id - 1]['likes'] -= 1
            cls.send_data_to_json(data)
            return 'liked'
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
Cars.get_likes(1)
Cars.get_likes(2)
Cars.get_likes(3)
print(Cars.listing())

Cars.get_comment(1, 'Была бы белая, взял бы')
Cars.get_comment(2, 'Слишком много жрет')
Cars.get_comment(3, 'Ремонт дорогой')
print(Cars.listing())

print(Cars.delete_car(1))

