class Order:
    def __init__(self, order_id, customer_name, amount):
        self.__order_id = order_id
        self.__customer_name = customer_name
        self.__amount = amount

    def set_order_id(self, order_id):
        self.__order_id = order_id

    def set_customer_name(self, customer_name):
        self.__customer_name = customer_name

    def set_amount(self, amount):
        self.__amount = amount

    def get_order_id(self):
        return self.__order_id

    def get_customer_name(self):
        return self.__customer_name

    def get_amount(self):
        return self.__amount

    def display_order(self):
        print(f"ID заказа: {self.__order_id}, Клиент: {self.__customer_name}, Сумма: {self.__amount} сом.")


class OrderManager:
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)
        print(f"Заказ с ID {order.get_order_id()} добавлен.")

    def remove_order(self, order_id):
        order = self.find_order(order_id)
        if order:
            self.orders.remove(order)
            print(f"Заказ с ID {order_id} удален.")
        else:
            print(f"Заказ с ID {order_id} не найден.")

    def find_order(self, order_id):
        for order in self.orders:
            if order.get_order_id() == order_id:
                return order
        return None

    def display_all_orders(self):
        if not self.orders:
            print("Список заказов пуст.")
        else:
            print("Список всех заказов:")
            for idx, order in enumerate(self.orders, start=1):
                print(f"{idx}. ID: {order.get_order_id()}, Клиент: {order.get_customer_name()}, Сумма: {order.get_amount()} сом.")


def main():
    manager = OrderManager()

    while True:
        command = input("Введите команду (add, remove, find, display, exit): ").strip().lower()

        if command == "add":
            order_id = input("Введите идентификатор заказа: ").strip()
            customer_name = input("Введите имя клиента: ").strip()
            amount = float(input("Введите сумму заказа: ").strip())
            new_order = Order(order_id, customer_name, amount)
            manager.add_order(new_order)

        elif command == "remove":
            order_id = input("Введите идентификатор заказа для удаления: ").strip()
            manager.remove_order(order_id)

        elif command == "find":
            order_id = input("Введите идентификатор заказа для поиска: ").strip()
            order = manager.find_order(order_id)
            if order:
                order.display_order()
            else:
                print(f"Заказ с ID {order_id} не найден.")

        elif command == "display":
            manager.display_all_orders()

        elif command == "exit":
            print("Закончена.")
            break

        else:
            print("Неверно, попробуйте снова.")

if __name__ == "__main__":
    main()
