import string
import unicodedata
class Product:
    def __init__(self, name: str, url: str, price: str, shop: int, brand: str, rating : int, imageURL: str):
        self.name = unicodedata.normalize('NFKD', name)
        self.url = str(url)
        self.shop = int(shop)
        self.brand = unicodedata.normalize('NFKD', brand)
        self.rating = int(str(rating)[0])
        self.imageURL = unicodedata.normalize('NFKD', imageURL)
        self.price = float(unicodedata.normalize('NFKD', price).replace(' CDN$', '').replace(',', '.'))