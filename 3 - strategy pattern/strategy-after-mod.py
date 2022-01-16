from abc import ABC, abstractmethod

import random
import string

def generate_id(length=8):
    # helper function for generating an id
    return ''.join(random.choices(string.ascii_uppercase, k=length))

class SupportTicket():

    def __init__(self, customer, issue):
        self.id = generate_id()
        self.customer = customer
        self.issue = issue

class ProcessStrategy(ABC):
    
    @abstractmethod
    def process_ticket(self, tickets: 'list[SupportTicket]') -> 'list[SupportTicket]':
        pass


class Fifo(ProcessStrategy):

    def process_ticket(self, tickets: 'list[SupportTicket]'):
        return tickets
        
class Lifo(ProcessStrategy):

    def process_ticket(self, tickets: 'list[SupportTicket]'):
        return reversed(tickets)

class Random(ProcessStrategy):

    def process_ticket(self, tickets: 'list[SupportTicket]'):
        list_copy = tickets.copy()
        random.seed()
        random.shuffle(list_copy)

        return list_copy

class CustomerSupport():
    
    def __init__(self, processing_strategy: ProcessStrategy = Fifo()):
         self.tickets = []
         self.processing_strategy = processing_strategy

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self):
        # if it's empty, don't do anything
        if len(self.tickets) == 0:
            print("There are no tickets to process. Well done!")
            return

        tickets_to_process = self.processing_strategy.process_ticket(self.tickets)
        for ticket in tickets_to_process:
            self.process_ticket(ticket)

    def process_ticket(self, ticket: SupportTicket):
        print("==================================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("==================================")


def main():
    # create the application
    app = CustomerSupport(Fifo())

    # register a few tickets
    app.create_ticket("John Smith", "My computer makes strange sounds!")
    app.create_ticket("Linus Sebastian", "I can't upload any videos, please help.")
    app.create_ticket("Arjan Egges", "VSCode doesn't automatically solve my bugs.")

    # process the tickets
    app.process_tickets()


if __name__=='__main__':
    main()

