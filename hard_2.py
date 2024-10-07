class Toy:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"Игрушка: {self.name}, Цвет: {self.color}"


class AnimalToy(Toy):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.toy_type = "Животное"

    def __str__(self):
        return f"Животное: {self.name}, Цвет: {self.color}"


class CartoonCharacterToy(Toy):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.toy_type = "Персонаж мультфильма"

    def __str__(self):
        return f"Персонаж мультфильма: {self.name}, Цвет: {self.color}"


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

        if toy_type == "Животное":
            return AnimalToy(name, color)
        elif toy_type == "Персонаж мультфильма":
            return CartoonCharacterToy(name, color)
        else:
            raise ValueError(f"Неизвестный тип игрушки: {toy_type}")



factory = ToyFactory()

animal_toy = factory.create_toy(name="Лев", color="Желтый", toy_type="Животное")
print(animal_toy)

cartoon_toy = factory.create_toy(name="Микки Маус", color="Черный", toy_type="Персонаж мультфильма")
print(cartoon_toy)
