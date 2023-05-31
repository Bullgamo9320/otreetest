from otree.api import *



doc = """
One player decides how to divide a certain amount between himself and the other
player.
See: Kahneman, Daniel, Jack L. Knetsch, and Richard H. Thaler. "Fairness
and the assumptions of economics." Journal of business (1986):
S285-S300.
"""


class C(BaseConstants):
    NAME_IN_URL = 'bargaining_practice'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1
    INSTRUCTIONS_TEMPLATE = 'bargaining_practice/instructions.html'
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
    p1 = #player1を参照する
    p2 = #player2を参照する
    if #player2がアクセプトしたかどうかで条件分ける:
        p1.payoff = #p1のpayoffを計算する
        p2.payoff = #p2のpayoffを計算する
    else:
        p1.payoff = #p1のpayoffを計算する
        p2.payoff = #p2のpayoffを計算する


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
