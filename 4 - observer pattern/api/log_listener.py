from lib.log import log
from .event_system import EventListener
from .event import event_system

class HandleUserRegistered(EventListener):

    def update(self, user):
        log(f"User registered with email address {user.email}")


class HandlePasswordForgotten(EventListener):

    def update(self, user):
        log(f"User with email address {user.email} requested a password reset")


def setup_log_listeners():
    '''
    Setup all log event listeners. Those will log a 
    message (through update method) every time an
    event, in which they are subscribed, will happen.

    :return None:
    '''

    handle_user_registered = HandleUserRegistered()
    handle_password_forgotten = HandlePasswordForgotten()

    event_system.add_subscriber('user_registered', handle_user_registered)
    event_system.add_subscriber('password_forgotten', handle_password_forgotten)
