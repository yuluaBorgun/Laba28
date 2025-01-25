class Flower: #Цветы
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Order: #Заказ
    def __init__(self, flower, client, quantity):
        self.flower = flower
        self.client = client
        self.quantity = quantity

class Client:#Клиент
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

# Список для хранения сущностей
flowers = []
clients = []
orders = []

def add_flower(name, price, quantity):
    flowers.append(Flower(name, price, quantity))

def view_flowers():
    for flower in flowers:
        print(f'Name: {flower.name}, Price: {flower.price}, Quantity: {flower.quantity}')

def update_flower(name, price=None, quantity=None):
    for flower in flowers:
        if flower.name == name:
            if price is not None:
                flower.price = price
            if quantity is not None:
                flower.quantity = quantity

def delete_flower(name):
    global flowers
    flowers = [flower for flower in flowers if flower.name != name]

# Интерактивный интерфейс
def interactive_mode():
    while True:
        action = input("Введите действие (add/view/update/delete/exit): ")
        if action == 'add':
            name = input("Введите имя цветка: ")
            price = float(input("Введите цену цветка: "))
            quantity = int(input("Введите количество цветка: "))
            add_flower(name, price, quantity)
        elif action == 'view':
            view_flowers()
        elif action == 'update':
            name = input("Введите имя цветка для обновления: ")
            price = input("Введите новую цену цветка (оставьте пустым, чтобы не изменять): ")
            quantity = input("Введите новое количество цветка (оставьте пустым, чтобы не изменять): ")
            update_flower(name, float(price) if price else None, int(quantity) if quantity else None)
        elif action == 'delete':
            name = input("Введите имя цветка для удаления: ")
            delete_flower(name)
        elif action == 'exit':
            break
        else:
            print("Неизвестное действие!")

if __name__ == "__main__":
    interactive_mode()