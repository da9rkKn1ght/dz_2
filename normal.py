class Person:
    def __init__(self, name_of_class, health, damage, armor):
        self.name_of_class = name_of_class
        self.health = health
        self.damage = damage
        self.armor = armor

    def _calculate_damage(self, incoming_damage):
         reduced_damage = incoming_damage - self.armor
         return max(5, reduced_damage)

    def take_damage(self, incoming_damage):
         damage_taken = self._calculate_damage(incoming_damage)
         self.health -= damage_taken
         if self.health <= 0:
             self.health = 0
         return damage_taken

    def is_alive(self):
         return self.health > 0

class Player(Person):
    def attack(self, enemy):
        print(f'{self.name_of_class} атакует {enemy.name_of_class} с уроном {self.damage}.')
        damage_dealt =  enemy.take_damage(self.damage)
        print(f'{enemy.name_of_class} получил {damage_dealt} урона, осталось {enemy.health} здоровья.')

class Enemy(Person):
    def attack(self, player):
        print(f'{self.name_of_class} атакует {player.name_of_class} с уроном {self.damage}.')
        damage_dealt = player.take_damage(self.damage)
        print(f'{player.name_of_class} получил {damage_dealt} урона, осталось {player.health} здоровья.')

class Game:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def fighting(self):
        turn = 0
        while self.player.is_alive() and self.enemy.is_alive():
            if turn % 2 == 0:
                self.player.attack(self.enemy)
            else:
                self.enemy.attack(self.player)
            turn += 1
        if self.player.is_alive():
            print(f'{self.player.name_of_class} победил!!!')
        else:
            print(f'{self.enemy.name_of_class} победил!!!')


player = Player(name_of_class="Герой", health=100, damage=40, armor=5)
enemy = Enemy(name_of_class="Орк", health=100, damage=35, armor=3)

game = Game(player, enemy)

game.fighting()