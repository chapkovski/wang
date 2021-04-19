from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):
    form_fields = ['understand']
    form_model = 'player'


class Decision(Page):
    form_fields = ['decision']
    form_model = 'player'


class SurveyLink(Page):
    pass
class Last(Page):
    pass


page_sequence = [
    Intro,
    Decision,
    SurveyLink,
    Last,

]
