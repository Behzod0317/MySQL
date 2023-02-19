import sqlite3

connection = sqlite3.connect("ichimliklar.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE Korzinka (name TEXT, species TEXT, cost INTEGER)")


class Korzinka:
    cart = []
    cost = []
    
    def tovar_qoshish(self,tovar):
        self.tovar_royxati.append(tovar)
        
    def chek(self):
        for tovar in self.tovar_royxati:
            print(f"(tovar.tovar_narxi)\n(tovar.nomi)\n(tovar.narxi)")
            
    def olingan_tovar(self, tovar, soni):
        items = cursor.execute("SELECT name, species, cost FROM Korzinka".fetchall())
        for narsa in range(0,len(items)):
            if tovar == items[narsa][0]:
                self.cart.append(narsa)
                self.cost.append(soni * items[narsa][2])
                print("success")
                
    def bozorlik_narxi(self):
        miqdori = 0
        for tovar in olingan_tovar:
            miqdori += tovar_narxi
        
        print(f"Sizning jami xarid qilgan maxsulotiz narxi: ",miqdori)


# Integration with python vars
category = ['Gazlangan ichimliklar', 'Energetik ichimliklar']
products = [
                ('Coca-Cola 1.5-l', 10000, 0),
                ('Pepsi 1.5-l', 10000, 0),
                ('Fanta 1.5-l', 10000, 0),
                ('Sprite 1.5-l', 10000, 0),
                ('Flash 0.5-l', 8000, 1),
                ('Adrenlin(Rush) 0.5-l', 11000, 1),
                ('Redbull 0.5-l', 18000, 1),
                ('18+ 0.5-l', 12000, 1)
           ]

for product in products:
    sql_query = "INSERT INTO Korzinka VALUES "
    category_name = category[0] if product[2]==0 else category[0]
    sql_query += f"({product[0]}, {category_name}, {product[1]})"
    cursor.execute(sql_query)


# fetching final result
rows = cursor.execute("SELECT name, species, cost FROM Korzinka").fetchall()
print(rows)

# using our class
cart = Korzinka()
cart.olingan_tovar('Redbull', 2)
print('cost: ', cart.cost)