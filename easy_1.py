class TownCar:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print(f'{self.name} поехала.')

    def stop(self):
        print(f'{self.name} остановилась.')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}.')


class SportCar:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print(f'{self.name} поехала.')

    def stop(self):
        print(f'{self.name} остановилась.')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}.')


class WorkCar:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print(f'{self.name} поехала.')

    def stop(self):
        print(f'{self.name} остановилась.')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}.')


class PoliceCar:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = True

    def go(self):
        print(f'{self.name} поехала.')

    def stop(self):
        print(f'{self.name} остановилась.')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}.')


town_car = TownCar(60, "Синий", "Городская")
sport_car = SportCar(120, "Красный", "Спортивная")
work_car = WorkCar(50, "Белый", "Грузовая")
police_car = PoliceCar(100, "Черный", "Полицейская")


town_car.go()
sport_car.turn("направо")
work_car.stop()
police_car.go()
