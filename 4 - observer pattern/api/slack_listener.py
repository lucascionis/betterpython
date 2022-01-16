from lib.slack import post_slack_message
from .event_system import EventListener
from .event import event_system

class HandleUserRegistered(EventListener):

    def update(self, user):
        post_slack_message(
            "sales",
            f"{user.name} has registered with email address {user.email}. Please spam this person incessantly."
        )

def setup_slack_listeners():
    '''
    Setup all slack event listeners. Those will post
    a slack message (through update method) every time an
    event, in which they are subscribed, will happen.

    :return None:
    '''

    handle_user_registered = HandleUserRegistered()
    event_system.add_subscriber('user_registered', handle_user_registered)
