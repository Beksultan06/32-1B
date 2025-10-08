


from models.product import SmartProduct
from models.customer import Customer
from models.order import Order
from utils.data_structures import OrderQueue
from db import add_product, get_all_products

p1 = SmartProduct(1, "Phone", 800, 10, 2)
p2 = SmartProduct(2, "Car", 10000, 3, 5)

p1.apply_discount(10)

add_product(p1)
add_product(p2)

c1 = Customer(1, "Bob", "bob@gmail.com")

order = Order(1, c1, [p1, p2])
order.save()

queue = OrderQueue()
queue.add_order(order)

print(order)
print(f"Всего заказов: {Order.total_orders()}")
print(f"Следующий заказ : {queue.process_next()}")