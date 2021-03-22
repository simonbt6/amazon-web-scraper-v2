from mysql import connector
from mysql.connector.cursor import MySQLCursor
from product import Product
import mysql
class Database:

    hostname = "149.28.37.80"
    username = "store_admin"
    password = "_f3J)QqZ)MXp7~6"
    database = "StoreAPI"
    
    def __init__(self):
        self.connection = mysql.connector.connect(host=self.hostname, user=self.username, password=self.password, database=self.database)
        
    def newProduct(self, product: Product) -> int:
        if product.imageURL[0] == "d":
            return 0
        c : MySQLCursor = self.connection.cursor()
        preparedStatement = "INSERT INTO product (name, url, price, shop, brand, img_url, rating) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (product.name, product.url, product.price, product.shop, product.brand, product.imageURL, product.rating)
        try:
            c.execute(preparedStatement, values)
            self.connection.commit()
            return c._last_insert_id
        except:
            return 0
        
