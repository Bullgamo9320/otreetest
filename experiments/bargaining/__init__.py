from otree.api import *



doc = """
One player decides how to divide a certain amount between himself and the other
player.
See: Kahneman, Daniel, Jack L. Knetsch, and Richard H. Thaler. "Fairness
and the assumptions of economics." Journal of business (1986):
S285-S300.
"""


class C(BaseConstants):
    NAME_IN_URL = 'bargaining'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1
    INSTRUCTIONS_TEMPLATE = 'bargaining/instructions.html'
    BICYCLE = cu(100)

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    price = models.CurrencyField(
        doc="""The price that buyer wants to pay for the bicycle""",
        min=0,
        max=C.BICYCLE,
        label="I will pay",
    )
    is_accept = models.StringField(
        doc="""""",
        label="Do you accept the offer?",
        choices=[
            ["Reject", 'Reject'],
            ["Accept", 'Accept'],
        ]
    )


class Player(BasePlayer):
    pass


# FUNCTIONS
def set_payoffs(group: Group):
    p1 = group.get_player_by_id(1)
    p2 = group.get_player_by_id(2)
    if group.is_accept=="Accept":
        p1.payoff = C.BICYCLE - group.price
        p2.payoff = group.price
    else:
        p1.payoff = 0
        p2.payoff = 0


# PAGES
class Introduction(Page):
    pass


class Offer(Page):
    form_model = 'group'
    form_fields = ['price']

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 1

class ResultsWaitPage(WaitPage):
    wait_for_all_groups = True

class AcceptOrReject(Page):
    form_model = 'group'
    form_fields = ['is_accept']

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 2

class ResultsWaitPage2(WaitPage):
    after_all_players_arrive = set_payoffs


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group

        return dict(offer=C.BICYCLE - group.price)


page_sequence = [Introduction, Offer,ResultsWaitPage,AcceptOrReject, ResultsWaitPage2, Results]
