# hangi kategoride biir productsa ona göre otomatik kod eklet 

from Product import Bavul,Cuzdan, Kemer,Canta
from Stock import Stock

suitcase = Bavul("Travel Pro","Black","Samsonite", "SC123", "2024-07-26", 50, "Large" )
wallet = Cuzdan("Leather Wallet", "Brown", "Gucci", "WL456", "2024-07-26", 100)
belt = Kemer("Leather Belt", "Black", "Hermes", "BT789", "2024-07-26", 5,1.60)
bag = Canta("Handbag", "Red", "Louis Vuitton", "BG012", "2024-07-26", "Shoulder Bag","Kadın Çantası")

stock=Stock()
stock.add(suitcase)
stock.add(wallet)
stock.add(belt)
stock.add(bag)

stock.list_products()

stock.remove_product(suitcase)
stock.list_products()

