from os import environ

SESSION_CONFIGS = [
    dict(
        name='dg1',
        display_name="DG - treatment 1 - low value NGO - text",
        num_demo_participants=1,
        app_sequence=['dg'],
        high=False,
        image=False,
    ),
    dict(
        name='dg2',
        display_name="DG - treatment 1 - high value NGO - text",
        num_demo_participants=1,
        app_sequence=['dg'],
        high=True,
        image=False,
    ),
    dict(
        name='dg3',
        display_name="DG - treatment 1 - low value NGO - image",
        num_demo_participants=1,
        app_sequence=['dg'],
        high=False,
        image=True,
    ),
    dict(
        name='dg4',
        display_name="DG - treatment 1 - high value NGO - image",
        num_demo_participants=1,
        app_sequence=['dg'],
        high=True,
        image=True,
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc="",
    link_to_survey='https://docs.google.com/forms/d/e/1FAIpQLSeWWD_elnN7J-aYAn4SZjT76FDy6NvZh8O1S2SwauDrAZegCQ/viewform?usp=pp_url&entry.1108649833='
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '*q3r3tw56kc0^3j9kef+jx6&75k^$ua-o_%9m_jqf8(dt2(azu'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
