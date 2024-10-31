class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, engine_power, color):
        self.owner = str(owner)
        self.__model = str(model)
        self.__engine_power = int(engine_power)
        self.__color = str(color)

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def get_owner(self):
        return f"Владелец: {self.owner}"

    def print_info(self):
        print(f'{self.get_model()} \n{self.get_horsepower()} \n{self.get_color()} \n{self.get_owner()}')

    def set_color(self, new_color):
        color_example = new_color
        new_color = str((new_color.lower()))
        if new_color in self.__COLOR_VARIANTS:
            self.__color = color_example
        else:
            print(f'Нельзя сменить цвет на {color_example}')

    def get_color_variants(self):
        return f"Cписок допустимых цветов для окрашивания: {self.__COLOR_VARIANTS}"


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def get_passengers_limit(self):
        return f'Максимальное количество пассажиров: {self.__PASSENGERS_LIMIT}'


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500,'blue')
vehicle1.print_info()

vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()
