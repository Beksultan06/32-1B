


from models.base import BaseModel


class Customer(BaseModel):
    def __init__(self, id, name, email):
        super().__init__(id)
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} - {self.email}"

    def save(self):
        print(f"User {self.name} save to DB")