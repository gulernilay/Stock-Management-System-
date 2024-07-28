class Product: 
    def __init__(self, name, color, brand, stock_code, date, stock_amount):
        self.name = name
        self.color = color
        self.brand = brand
        self.stock_code = stock_code
        self.date = date
        self.stock_amount = stock_amount
    
    def __str__(self):
        return (f"Product Name: {self.name}\n"
                f"Color: {self.color}\n"
                f"Brand: {self.brand}\n"
                f"Stock Code: {self.stock_code}\n"
                f"Date Added: {self.date}\n"
                f"Stock Amount: {self.stock_amount} units")
    
class Bavul(Product):
    def __init__(self, name, color, brand, stock_code, date, stock_amount, size):
        super().__init__(name, color, brand, stock_code, date, stock_amount)
        self.size = size
    
    def __str__(self):
        return (super().__str__() + 
                f"\nSize: {self.size}")
 
class Cuzdan(Product):
    def __init__(self, name, color, brand, stock_code, date, stock_amount):
        super().__init__(name, color, brand, stock_code, date, stock_amount)
    
    def __str__(self):
        return super().__str__()
  
class Kemer(Product):
    def __init__(self, name, color, brand, stock_code, date, stock_amount, height):
        super().__init__(name, color, brand, stock_code, date, stock_amount)
        self.height = height
    
    def __str__(self):
        return (super().__str__() +  
                f"\nHeight: {self.height}")

class Canta(Product):
    def __init__(self, name, color, brand, stock_code, date, stock_amount, type_):
        super().__init__(name, color, brand, stock_code, date, stock_amount)
        self.type = type_
    
    def __str__(self):
        return (super().__str__() + 
                f"\nType: {self.type}")
