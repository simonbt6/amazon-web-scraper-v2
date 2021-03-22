import _thread
from typing import Collection, List
from workers import Worker
from request import Request
from threading import Thread, active_count, currentThread, current_thread, main_thread
import os

import collections

"""
 - Request queue.
 - Dispatch
    - Thread
    - Domain

"""
class Dispatch:
    """
    Dispatcher for requests.
    Is responsible for management of multi-threading.
    """
    activeWorkers : List[Worker] = []
    sleepingThread = 0 
    _Q = collections.deque(maxlen=10)

    maxWorkers = os.cpu_count()
    #maxWorkers = 1
    def __init__(self):
        print("Starting multi-threading dispatch on %s threads." % os.cpu_count())
        self.startWorkers()

    def sortWorkers(self):
        self.activeWorkers.sort(key=self.sortingKey)

    def sortingKey(self, worker: Worker) -> int:
        return len(worker.requestQueue)

    def startWorkers(self):
        for i in range(self.maxWorkers):
            if self.activeWorkers.count(Worker) >= os.cpu_count():
                return
            self.activeWorkers.append(Worker())

    async def newRequest(self, request: Request) -> None:
        # Check if the request is for a valid and supported domain.
        if not request.validDomain():
            print('Invalid domain name ->', request.domain)
            return
        # Checks if request queue is full.
        if len(self._Q) == self._Q.maxlen:
            print('Request queue is full.')
            return
        # Looks for sleeping thread to delegate the request.
        if self.sleepingThread > 0:
            return self.processRequest(request=request)
        # Puts the request into queue for furter processing.
        self._Q.append(request)
        print("Added request to queue. -->", request.domain)
        self.lookforspot()
    
    def lookforspot(self):
        # Sort workers by queue length.
        self.sortWorkers()
        """ Looks for a spot in a running worker for queued requests."""
        while len(self._Q) > 0:
            for worker in self.activeWorkers:
                if len(self._Q) > 0:
                    if len(worker.requestQueue) != worker.maxQueue:
                        print("Found worker for request. %s requests waiting."% len(self._Q))
                        worker.requestQueue.append(self._Q.pop())