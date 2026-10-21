class Product():
    def __init__(self, price, quantity, category):
        self.price = price
        self.quantity = quantity
        self.category = category
    def __str__(self):
        return f"Товар: {self.category} (цена: {self.price}, кол-во: {self.quantity})"


class Order():
    def __init__(self, items, tax, discount=0):
        self.items = items
        self.tax = tax
        self.discount = discount
    def calculate_total(self):
        result = 0
        for x in self.items:
            result += x.price * x.quantity # считаем сумму
        # к сумме прибавляем налог и вычитаем скидку
        result = result * (1 + self.tax)
        result = result * (1 - self.discount)
        return result
    def __str__(self):
        return f"Заказ на сумму {self.calculate_total()} руб."

class Customer():
    def __init__(self, name):
        self.name = name
        self.orders = []
    def add_order(self, order):
        self.orders.append(order)
    def __str__(self):
        return f"Покупатель: {self.name} (заказов: {len(self.orders)})"

class ShoppingCart():
    def __init__(self):
        self.items = []
    def add_item(self, item):
        self.items.append(item)
    def remove_item(self, item):
        self.items.remove(item)
    def update_quantity(self, product, new_quantity):
        product.quantity = new_quantity # обновляем количество


# создаем товары (цена, количество, категория)
apple = Product(50, 10, "Фрукты")
bread = Product(40, 2, "Выпечка")

# создаем корзину и добавляем товары
cart = ShoppingCart()
cart.add_item(apple)
cart.add_item(bread)

# обновляем количество яблок (5 штук вместо 10)
cart.update_quantity(apple, 5)

# удаляем хлеб из корзины (передумал)
cart.remove_item(bread)

# cоздаем заказ из оставшегося в корзине (только яблоки)
# Налог 10% (0.1), скидка 5% (0.05)
order = Order(cart.items, tax=0.1, discount=0.05)

# cоздаем покупателя и привязываем к нему заказ
customer = Customer("Иван")
customer.add_order(order)

# cчитаем итоговую сумму
total = order.calculate_total()

# Выводим результат
print(f"Покупатель: {customer.name}")
print(f"Стоимость заказа с учетом налога и скидки: {total} руб.")
for o in customer.orders:
    print(o)