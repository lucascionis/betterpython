from api.user import register_new_user, password_forgotten
from api.plan import upgrade_plan

from api.email_listener import setup_email_listeners
from api.log_listener import setup_log_listeners
from api.slack_listener import setup_slack_listeners

def main():
    # setup all listeners
    setup_email_listeners()
    setup_log_listeners()
    setup_slack_listeners()

    # register a new user
    register_new_user("Arjan", "BestPasswordEva", "hi@arjanegges.com")

    # send a password reset message
    password_forgotten("hi@arjanegges.com")

    # upgrade the plan
    #upgrade_plan("hi@arjanegges.com")


if __name__ == '__main__':
    main()
