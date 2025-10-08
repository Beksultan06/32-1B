

from models.base import BaseModel


class Product(BaseModel):
    def __init__(self, id, name, price, stock):
        super().__init__(id)

        self.name = name
        self.price = price 
        self.stock = stock

    def __str__(self):
        return f"{self.name} {self.price}$ ({self.stock})"
    
    def update_stock(self, quantity):
        self.stock -= quantity

    def save(self):
        print(f"Product {self.name} save to DB")

class DiscountMixin:
    def apply_discount(self, percent):
        self.price -= self.price * percent / 100

class SmartProduct(Product, DiscountMixin):
    def __init__(self, id, name, price, stock, warranty_years):
        super().__init__(id, name, price, stock)
        self.warranty_years = warranty_years