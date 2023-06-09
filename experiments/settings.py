from os import environ

SESSION_CONFIGS = [
    dict(
        name='survey',
        display_name='survey',
        num_demo_participants=1,
        app_sequence=['survey', 'payment_info'],
    ),
    dict(
        name='auction',
        display_name='auction',
        num_demo_participants=3,
        app_sequence=['auction', 'payment_info'],
    ),
    dict(
        name='motivation_experiment',
        display_name='motivation_experiment',
        num_demo_participants=3,
        app_sequence=['motivation_experiment', 'payment_info'],
    ),
    dict(
     name="my_public_goods",
     display_name="My Public Goods",
     num_demo_participants=4,
     app_sequence=["my_public_goods"],
    ),
    dict(
        name="double_auction",
        display_name="Double Auction",
        num_demo_participants=2,
        app_sequence=["double_auction"],
    ),
    dict(
        name="stock_game",
        display_name="Stock Game",
        num_demo_participants=2,
        app_sequence=["stock_game"],
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'JPY'
USE_POINTS = False

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""

SECRET_KEY = '{{ secret_key }}'

INSTALLED_APPS = ['otree']
