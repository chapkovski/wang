from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'dg'
    players_per_group = None
    num_rounds = 1
    endowment = c(10)


class Subsession(BaseSubsession):
    treatment = models.StringField()

    def creating_session(self):
        high = 'high' if self.session.config.get('high') else 'low'
        image = 'image' if self.session.config.get('image') else 'text'
        self.treatment = f'{high} - {image}'


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    def get_link_to_survey(self):
        return f'{self.session.config.get("link_to_survey")}{self.participant.code}'

    understand = models.BooleanField(widget=widgets.CheckboxInput,
                                     label='Do you fully understand the rules? You get to keep whatever remaining.')
    decision = models.CurrencyField(min=0, max=Constants.endowment,
                                    label=f'Please enter the amount you would like to donate to the non-profit'
                                          f' organization you just read about (from 0 to {Constants.endowment}) ')
    gender = models.StringField(label='What is your gender?',
                                choices=['female', 'male', 'gender diverse'],
                                widget=widgets.RadioSelect)

    age = models.IntegerField(label='How old are you?', min=0, max=100)
    donation_history = models.BooleanField(
        label='Have you donated to a children support organization in the past 6 months?')
    children = models.BooleanField(label='Do you have children?')
    working = models.BooleanField(label='Are you working in a field helping children')
