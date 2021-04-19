from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):
    form_fields = ['understand']
    form_model = 'player'


class Decision(Page):
    form_fields = ['decision']
    form_model = 'player'

class Survey(Page):
    form_fields = [
        'gender',
        'age',
        'donation_history',
        'children',
        'working'

    ]
    form_model = 'player'
class Last(Page):
    pass


page_sequence = [
    Intro,
    Decision,
    Survey,
    Last,

]
