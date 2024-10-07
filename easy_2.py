class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police 

    def go(self):
        print(f'{self.name} поехала.')

    def stop(self):
        print(f'{self.name} остановилась.')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}.')


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=False)


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=False)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=False)


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)


town_car = TownCar(60, "Синий", "Городская")
sport_car = SportCar(120, "Красный", "Спортивная")
work_car = WorkCar(50, "Белый", "Грузовая")
police_car = PoliceCar(100, "Черный", "Полицейская")

town_car.go()
sport_car.turn("направо")
work_car.stop()
police_car.go()
