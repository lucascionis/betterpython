from abc import ABC, abstractmethod

'''Comments
In the original solution only functions were used to
implement the event system (observer pattern).

In this implementation I wanted to write classes (to be as
nearest as possible to the pattern (?)).

It is surely better to use python first-citizen functions to create
the event handles (basically this is what I done, I created handle 
classes to write different implementations of update method).
'''

class EventListener(ABC):

    @abstractmethod
    def update(self, data):
        pass


class EventSystem():

    def __init__(self):
        self.subscribers = {}

    def add_subscriber(self, event: str, subscriber: EventListener):
        if event in self.subscribers:
            self.subscribers[event].append(subscriber)
            return
        
        self.subscribers[event] = [subscriber,]

    def trigger_event(self, event: str, data):
        for subscriber in self.subscribers[event]:
            subscriber.update(data)


