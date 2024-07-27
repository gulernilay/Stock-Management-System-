
from Product import Suitcase ,Belt,Wallet, Bag


class Stock :
  def __init__(self):
    self.products={}  # her bir stock objesi için bir products tuple atanır
  def add(self,product):
    if product.stock_code not in self.products:
            self.products[product.stock_code] = product
    else:
            print(f"Product with stock code {product.stock_code} already exists.")
  def remove_product(self, product):
      if product.stock_code not in self.products:
           print(f"Product with stock code {product.stock_code} not exists.")
      else:
          removed_product=self.products.pop(product.stock_code)
          print(f"Ürün stoktan kaldırıldı:{removed_product}")
  def update_stock(self, product_id, quantity):
      if product_id in self.products:
       self.products[product_id].quantity += quantity    
       print(f"Stok güncellendi: {self.products[product_id]}")
      else:
       print("Ürün bulunamadı!")
 
  def list_products(self):
        if not self.products:
            print("Stokta hiç ürün yok.")
        else:
            for product in self.products.values():
                if isinstance(product, Suitcase):
                    print(f'("{product.name}", "{product.color}", "{product.brand}", "{product.stock_code}", "{product.date}", {product.stock_amount}, "{product.size}")')
                elif isinstance(product, Wallet):
                    print(f'("{product.name}", "{product.color}", "{product.brand}", "{product.stock_code}", "{product.date}", {product.stock_amount})')
                elif isinstance(product, Belt):
                    print(f'("{product.name}", "{product.color}", "{product.brand}", "{product.stock_code}", "{product.date}", {product.stock_amount}, "{product.height}")')
                elif isinstance(product, Bag):
                    print(f'("{product.name}", "{product.color}", "{product.brand}", "{product.stock_code}", "{product.date}", {product.stock_amount}, "{product.type}")')
    
  def __str__(self):
        return "\n".join(str(product) for product in self.products.values())


