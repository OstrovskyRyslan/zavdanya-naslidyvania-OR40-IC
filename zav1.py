class Car:
    def __init__(self, brand, year):
        self.__brand = brand
        self.__year = year
    def get_brand(self):
        return self.__brand
    def set_brand(self, brand):
        self.__brand = brand
    def get_year(self):
        return self.__year
    def set_year(self, year):
        self.__year = year
    def display_info(self):
        print(f"Марка: {self.__brand}, Рік: {self.__year}")
class ElectricCar(Car):
    def __init__(self, brand, year, battery_capacity):
        super().__init__(brand, year)
        self.__battery_capacity = battery_capacity
    def get_battery_capacity(self):
        return self.__battery_capacity
    def set_battery_capacity(self, battery_capacity):
        self.__battery_capacity = battery_capacity
    def display_info(self):
        super().display_info()
        print(f"Ємність батареї: {self.__battery_capacity} кВт⋅год")
car = Car("Toyota", 2020)
car.display_info()
electric_car = ElectricCar("Tesla", 2022, 75)
electric_car.display_info()
