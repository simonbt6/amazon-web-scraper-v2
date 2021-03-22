domains = [
    'amazon.com',
    'amazon.ca'
]


class Request:
    """
        Request class structure
    """
    def __init__( self, url: str, priority: int):
        self.url = url
        self.priority = priority
        self.domain = self.findDomain()
        print(url)
        
    def findDomain(self) -> str:
        for domain in domains:
            if domain in self.url:
                return domain
    
    def validDomain(self) -> bool:
        if self.domain != None: 
            return True
        return False