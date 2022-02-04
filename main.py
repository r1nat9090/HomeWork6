# class Transport:
#     # атрибуты класса
#     # name = 'Ferrari'
#     # color = 'red'
#     # year = 2021
#     count = 0
#
#     # методы класса
#     def __init__(self, name, color, year): # конструктор
#         self.n = name # публичный доступ
#         #self._n = name  # защищенный доступ
#         #self._n = name  # приватный доступ
#         self.c = color
#         self.y = year
#         print(f'создан объект: name = {self.n}, color = {self.c}, year = {self.y}')
#
#     # def count_car(self):
#     #     # self.count += 1
#     #     Auto.count += 1
#     #     print(self.count)
#
#     def go(self):
#         print('Едет')
#
#     def stop(self):
#         print('Останавливается')
#
# class Auto(Transport): # Дочерний класс
#     def __init__(self, name, color, year, pas):  # конструктор
#         super().__init__(name, color, year) #Беру параметры из родительского класса (выше)
#         self.p = pas
#         print(f'Количество мест: {self.p}')
#         #print(f'создан объект: name = {self.n}, color = {self.c}, year = {self.y}, pas = {self.p}')
#
#     def drif(self):
#         print('Дрифт')
#
# class Bus(Transport):
#     def route(self):
#         print('Автобус следует по маршруту')
#
# car_1 = Auto('Ferrari', 'red', 2021, 5) # Создание экземпляра класса
# #car_1 = Transport('Ferrari', 'red', 2021) # Создание экземпляра класса
# print(car_1.n)
# print(car_1.y)
# # print(car_1.name)
# # print(car_1.color)
# car_1.go() # публичный доступ
# car_1.stop()
# #car_1.count_car()
# car_1.drif()
#
# car_2 = Auto('Audi', 'green', 2022, 3)
# # car_2.color = 'green'
# # print(car_2.name)
# # print(car_2.color)
# car_2.go()
# car_2.stop()
# #car_2.count_car()
#
# bus_1 = Bus('Ikarus', 'white', 2017)
# # car_2.color = 'green'
# # print(car_2.name)
# # print(car_2.color)
# bus_1.go()
# bus_1.stop()
# bus_1.route()

# class Player:
#     def player_method(self):
#         print("Родительский метод класса Player")
#
#
# class Navigator:
#     def navigator_method(self):
#         print("Родительский метод класса Navigator")
#
#
# class MobilePhone(Player, Navigator):
#     def mobile_phone_method(self):
#         print("Дочерний метод класса MobilePhone")
#
# phone = MobilePhone()
# phone.mobile_phone_method()
# phone.player_method()

import time

print('Hello')
time.sleep(5)
print('How are you')