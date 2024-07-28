from pymongo import MongoClient

# MongoDB sunucusuna bağlan
client = MongoClient('mongodb://localhost:27017/')

# Veritabanını seç
db = client['gokhancanta'] 

# Koleksiyonu seç
collection = db['Kullanıcılar']  

# Veri ekleme
data = {
    "name": "Nilay Güler",
    "username": "nilay",
    "password": "biomedicalcomputer"
}
result = collection.insert_one(data)
print(f"Inserted document id: {result.inserted_id}")

# Veri sorgulama
query = {"name": "John Doe"}
document = collection.find_one(query)
print("Found document:", document)

# Verilerin tümünü listeleme
all_documents = collection.find()
for doc in all_documents:
    print(doc)

# Belirli bir veriyi güncelleme
update_query = {"name": "John Doe"}
new_values = {"$set": {"age": 31}}
collection.update_one(update_query, new_values)
print("Document updated")

# Veriyi silme
delete_query = {"name": "John Doe"}
collection.delete_one(delete_query)
print("Document deleted")

# Bağlantıyı kapat
client.close()
