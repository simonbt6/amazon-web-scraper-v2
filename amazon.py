from requests_html import HTMLSession
from product import Product
from request import Request

class AmazonScraper:
    def __init__(self):
        pass

    def scrapeCA(self, request: Request) -> Product:
        if request.domain != "amazon.ca":
            return
        session = HTMLSession()
        session.headers = {
            'content-type': 'text/html;charset=UTF-8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        }
        r = session.get(request.url)
        product = {
            'name': r.html.xpath('//*[@id="productTitle"]', first=True).text,
            'price': r.html.xpath('//*[@id="priceblock_ourprice"]', first=True).text,
            'rating': r.html.xpath('//*[@id="acrPopover"]/span[1]/a/i[1]/span', first=True).text,
            'imageURL': r.html.xpath('//*[@id="landingImage"]', first=True).attrs['src'],
            'brand': r.html.xpath('//*[@id="bylineInfo"]', first=True).text
        }
        
        return Product(
            product['name'],
            request.url, # page url
            product['price'], 
            1, # Shop id 
            product['brand'], 
            product['rating'],
            product['imageURL'])

        
        