from database import Database
from os import stat
import queue
from threading import Thread
from request import *
import time
from collections import deque
from amazon import AmazonScraper

class Worker:
    maxQueue = 10
    def __init__(self):
        self._running = True
        self.thread = Thread(target=self.run)
        self.requestQueue = deque(maxlen=self.maxQueue)
        self.occupied = False
        
        self.thread.start()
        print("Starting worker.", self.thread.native_id)

    def run(self):
        while self._running:
            if not self.occupied:
                self.nextRequest()
            time.sleep(2)
        self.thread.join()

    def process(self, request: Request):
        self.occupied = True
        # Actual process
        if request.validDomain():
            print("Processing request on worker -->", self.thread.native_id)
            if request.domain == 'amazon.ca':
                product = AmazonScraper().scrapeCA(request=request)
                retrievedID = Database().newProduct(product)
                print("Processing request on worker over. "+ product.name+ " with ID:", retrievedID )
            elif request.domain == 'amazon.com':
                pass
        else:
            print("[Error] Request domain is invalid. Aborting.")
        # End of process
        self.occupied = False

    def nextRequest(self) -> None:
        print("Looking for a request. -->", self.thread.native_id)
        if len(self.requestQueue) > 0:
            self.process(self.requestQueue.pop())

    def terminate(self):
        self._running = False

