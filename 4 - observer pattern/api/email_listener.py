from lib.email import send_email
from .event_system import EventListener
from .event import event_system

class HandleUserRegistered(EventListener):

    def update(self, user):
        send_email(
            user.name,
            user.email,
            "Welcome",
            f"Thanks for registering, {user.name}!\nRegards, The DevNotes team"
        )

class HandlePasswordForgotten(EventListener):

    def update(self, user):
        send_email(
            user.name,
            user.email,
            "Reset your password",
            f"To reset your password, use this very secure code: {user.reset_code}.\nRegards, The DevNotes team"
        )

def setup_email_listeners():
    '''
    Setup all email event listeners. Those will send
    and email (through update method) every time an
    event, in which they are subscribed, will happen.

    :return None:
    '''

    handle_user_registered = HandleUserRegistered()
    handle_password_forgotten = HandlePasswordForgotten()

    event_system.add_subscriber('user_registered', handle_user_registered)
    event_system.add_subscriber('password_forgotten', handle_password_forgotten)
