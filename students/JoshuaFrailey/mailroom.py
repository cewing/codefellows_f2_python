import random

random.seed(0)

donor_list = [
    [u"Jonathan Blow"], [u"Markus Persson"], [u"Mike Bithell"],
    [u"Calvin Goble"], [u"Alix Stolzer"], [u"Jeff Vogel"]
    ]

for donor in donor_list:
    for donations in range(random.randint(1, 3)):
        donor.append(round(random.random()*10000, 2))


def _get_donor():
    pass


def _get_donation():
    pass


def _send_thankyou():
    pass


def _create_report():
    pass


while True:
    menu = u"""
        Please select from the following:
        '1: Send a Thank You'
        '2: Create a Report'
        '3: Exit'
        """
    input_ = raw_input(menu)
    if input_.lower() in ['1', 's', 'send a thank you']:
        _send_thankyou()
    elif input_.lower() in ['2', 'c', 'create a report']:
        _create_report()
    elif input_.lower() in ['3', 'e', 'exit']:
        break
    else:
        input_ = raw_input(u"Please enter '1', '2', or '3'")
