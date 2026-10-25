class SpaceShip:
    def __init__(self, fuel, max_fuel, hull_status, speed, max_speed):
        self.fuel = fuel
        self.max_fuel = max_fuel
        self.hull_status = hull_status
        self.speed = speed
        self.max_speed = max_speed

    def add_fuel(self, value):
        # Топливо добавляется, но не может превышать размер бака
        self.fuel = min(self.max_fuel, self.fuel + value)

    def burn_fuel(self, value):
        if self.fuel >= value:
            self.fuel -= value
        else:
            print("Недостаточно топлива!")

    def speed_up(self, value):
        # Увеличиваем скорость, но ограничиваем её максимумом
        self.speed = min(self.max_speed, self.speed + value)

    def speed_down(self, value):
        if self.speed >= value:
            self.speed -= value
        else:
            print("Вы не можете развернуть корабль!")

    def repair(self, value):
        # Корпус чинится, но не может превышать 100%
        self.hull_status = min(100, self.hull_status + value)

    def __str__(self):
        return f"Космический корабль [Топливо: {self.fuel}/{self.max_fuel}, Корпус: {self.hull_status}%, Скорость: {self.speed}/{self.max_speed}]"


class CrewMember:
    def __init__(self, health, max_health, skill, role):
        self.health = health
        self.max_health = max_health
        self.skill = skill
        self.role = role

    def damage(self, value):
        self.health -= value
        # Защищаем от ухода в минус и проверяем гибель
        if self.health <= 0:
            self.health = 0
            print(f"Член экипажа ({self.role}) погиб!")

    def heal(self, value):
        if self.health > 0:
            # Лечим, но здоровье не может превышать максимум
            self.health = min(self.max_health, self.health + value)
            print(f"Здоровье ({self.role}) восстановлено: {self.health}/{self.max_health}")
        else:
            print(f"Нельзя вылечить погибшего члена экипажа ({self.role})!")

    def train(self, value):
        self.skill += value
        print(f"Навык роли '{self.role}' улучшен! Текущий уровень: {self.skill}")

    def __str__(self):
        return f"Экипаж [{self.role}] — здоровье: {self.health}/{self.max_health}, навык: {self.skill}"

class Mission:
    def __init__(self, goal, resources, event):
        self.goal = goal
        self.resources = resources
        self.event = event

    def handle_event(self, event):
        print(f"Внимание! Во время миссии произошло событие: {self.event}")

    def __str__(self):
        return f"Цель миссии: {self.goal} | Ресурсы корабля: {self.resources} | Угроза: {self.event} "



# тест

# Создаем корабль
my_ship = SpaceShip(fuel=70, max_fuel=100, hull_status=95, speed=30, max_speed=180)

# Создаем членов экипажа
pilot = CrewMember(health=100, max_health=100, skill=5, role="Пилот")
engineer = CrewMember(health=80, max_health=100, skill=7, role="Инженер")

# Создаем миссию
mission = Mission(
    goal="Долететь до сектора Альфа",
    resources=my_ship,
    event="Метеоритный дождь"
)

# Проверяем вывод через __str__
print(mission)
print(pilot)
print(engineer)


print("\n--- Проверяем методы корабля ---")
my_ship.add_fuel(100)  # Проверяем лимит max_fuel (должно упереться в 100)
my_ship.repair(50)     # Проверяем лимит корпуса (должно упереться в 100)
print(my_ship)

print("\n--- Проверяем методы экипажа ---")
pilot.heal(20)         # Проверяем лечение пилота
engineer.train(3)      # Проверяем прокачку навыка инженера
print(pilot)
print(engineer)

print("\n--- Проверяем критический урон ---")
pilot.damage(150)      # Наносим смертельный урон пилоту
pilot.heal(50)         # Пытаемся вылечить погибшего
print(pilot)