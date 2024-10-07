class Toy:
    def __init__(self, name, color, toy_type):
        self.name = name
        self.color = color
        self.toy_type = toy_type

    def __str__(self):
        return f"Игрушка: {self.name}, Тип: {self.toy_type}, Цвет: {self.color}"


class ToyFactory:
    def __init__(self):
        pass

    def buy_materials(self, name, color, toy_type):
        print(f"Закупаем материалы для создания {toy_type} с именем {name} и цветом {color}.")

    def sew_toy(self, name):
        print(f"Шьем игрушку с именем {name}.")

    def paint_toy(self, color):
        print(f"Окрашиваем игрушку в цвет {color}.")

    def create_toy(self, name, color, toy_type):
        self.buy_materials(name, color, toy_type)
        self.sew_toy(name)
        self.paint_toy(color)
        return Toy(name, color, toy_type)



factory = ToyFactory()

new_toy = factory.create_toy(name="Медвежонок", color="Коричневый", toy_type="Животное")

print(new_toy)

