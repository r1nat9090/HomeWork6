# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд,
# второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов.
# При его нарушении выводить соответствующее сообщение и завершать скрипт.

# class Trafficlight():
#     _color_1 = 'Red'
#     _color_2 = 'Yellow'
#     _color_3 = 'Green'
#
#     def running(self):
#         print('Запуск')
#
# import time
#
# Trafficlight_1 = Trafficlight()
# Trafficlight_1.running()
# print("Загорелся красный: ",Trafficlight_1._color_1)
# time.sleep(7)
# print("Красный потух, загорелся желтый: ", Trafficlight_1._color_2)
# time.sleep(2)
# print("Желтый потух, загорелся зеленый: ", Trafficlight_1._color_3)
# time.sleep(3)

# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

# class Road():
#     __length = 0
#     __width = 0
#
#     def mass_calculating(self, length, width, density, thickness):
#         self.__length = length
#         self.__width = width
#         self.d = density
#         self.t = thickness
#         return self.__length*self.__width*self.d*self.t
#
# Road_1 = Road()
# print(f'Масса асфальта составляет: {Road_1.mass_calculating(20, 5000, 25, 5)/1000} т.')


# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры
# класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.

# class Worker:
#     name = ''
#     surname = ''
#     position = ''
#     _income = {}
#
#     def __init__(self, name, surname, position, wage, bonus):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = {'wage': wage, 'bonus': bonus}
#
# class Position(Worker):
#
#     def full_name(self):
#         return f'Полное имя сотрудника: {self.name} {self.surname}'
#
#     def full_salary(self):
#         return f'Доход с учетом премии: {sum(self._income.values())} у.е.'
#
# Worker_1 = Position('Tom', 'Marvolo Riddle', 'Director', 100000, 500)
# print(Worker_1.position)
# print(Worker_1.full_name())
# print(Worker_1.full_salary())

# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

# class Car:
#     def __init__(self, color, name, is_police):
#         self.speed = 0
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#
#     def go(self, speed):
#         self.speed = speed
#         print(f'Трогаемся или продолжаем движение, скорость составляет {speed} км/ч')
#
#     def stop(self):
#         self.speed = 0
#         print('Автомобиль останавливается')
#
#     def turn_left(self):
#         print(f'Поворачиваем налево')
#
#     def turn_right(self):
#         print(f'Поворачиваем направо')
#
#     def show_speed(self):
#         print(f'Текущая скорость автомобиля составляет {self.speed} км/ч')
#
#
# class TownCar(Car):
#     def __init__(self, color: str, name: str):
#         self.speed = 0
#         self.color = color
#         self.name = name
#         self.is_police = False
#
#     def show_speed(self):
#         if self.speed > 60:
#             print(f'Скорость превышена и составляет {self.speed} км/ч, допустимая скорость 60 км/ч')
#         else:
#             print(f'Текущая скорость автомобиля составляет {self.speed} км/ч, превышения нет')
#
#
# class SportCar(Car):
#     def __init__(self, color: str, name: str):
#         self.speed = 0
#         self.color = color
#         self.name = name
#         self.is_police = False
#
#
# class WorkCar(Car):
#     def __init__(self, color: str, name: str):
#         self.speed = 0
#         self.color = color
#         self.name = name
#         self.is_police = False
#
#     def show_speed(self):
#         if self.speed > 40:
#             print(f'Скорость превышена и составляет {self.speed} км/ч, допустимая скорость 40 км/ч')
#         else:
#             print(f'Текущая скорость автомобиля составляет {self.speed} км/ч, превышения нет')
#
#
# class PoliceCar(Car):
#     def __init__(self, color: str, name: str):
#         self.speed = 0
#         self.color = color
#         self.name = name
#         self.is_police = True
#
#
# def test_drive(Auto):
#     print(f"Тест-драйв {'полицейского' if Auto.is_police else 'гражданского'} автомобиля {Auto.name}, цвет {Auto.color}")
#     Auto.go(20)
#     Auto.show_speed()
#     Auto.turn_left()
#     Auto.stop()
#     Auto.go(40)
#     Auto.show_speed()
#     Auto.turn_right()
#     Auto.go(60)
#     Auto.show_speed()
#     Auto.turn_left()
#     Auto.go(100)
#     Auto.show_speed()
#     Auto.turn_right()
#     Auto.stop()
#     print("Тест-драйв окончен", end="\n\n")
#
#
# car = Car('Black', 'Porsche', False)
# test_drive(car)
#
# car_1 = TownCar('White', 'Hyundai Solaris')
# test_drive(car_1)
#
# car_2 = SportCar('White', 'Ferrari')
# test_drive(car_2)
#
# car_3 = WorkCar('Yellow', 'Volkswagen Beetle')
# test_drive(car_3)
#
# car_4 = PoliceCar('Black', 'Porsche Panamera')
# test_drive(car_4)


# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

# class Stationery:
#     def __init__(self, title):
#         self.t = title
#
#     def draw(self):
#         print(f'Запуск отрисовки {self.t}')
#
# class Pen(Stationery):
#     def draw(self):
#         print(f'Запуск отрисовки {self.t} ручкой')
#
# class Pencil(Stationery):
#     def draw(self):
#         print(f'Запуск отрисовки {self.t} карандашом')
#
# class Handle(Stationery):
#     def draw(self):
#         print(f'Запуск отрисовки {self.t} маркером')
#
#
# Stationery_1 = Stationery('мелом')
# Stationery_1.draw()
#
# Pen_1 = Pen('зеленой')
# Pen_1.draw()
#
# Pencil_1 = Pencil('механическим')
# Pencil_1.draw()
#
# Handle = Handle('красным')
# Handle.draw()