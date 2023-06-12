from otree.api import *

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'stock_trading'
    PLAYERS_PER_GROUP = 4 #１グループあたりの人数
    NUM_ROUNDS = 5 #何ラウンドするか
##　ここから独自変数の記述　##
    DOWN_IMAGES = [1, 4, 8, 17]#ここに下落するものを指定
    CHART_IMAGES = 20  #何種類あるか


class Subsession(BaseSubsession):
    pass

def creating_session(subsession: Subsession):
    for i in subsession.get_players():
        participant = i.participant
        chart_image_ids = generate_updown()
        for downlist in chart_image_ids:
            decline = downlist in C.DOWN_IMAGES
            Trial.create(player=i, chart_image_ids=downlist, decline=decline)




class Group(BaseGroup):
    pass

class Player(BasePlayer):
    choice = models.LongStringField()
    # TrialモデルをPlayerモデルに関連付ける

class Trial(ExtraModel):
    player = models.Link(Player)
    chart_image_ids = models.IntegerField()
    decline = models.BooleanField()


#Functions
def generate_updown():
    import random
    output_number = list(range(C.CHART_IMAGES ))
    random.shuffle(output_number)
    return output_number


# PAGES

class MyPage(Page):
    pass

class Checkpage(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.choice.field_maybe_none() == 'No' if player.choice is not None else False

class ResultsWaitPage(WaitPage):
    all_players_done = "payoff_calculate"


class Results(Page):
    pass


page_sequence = [Checkpage, ResultsWaitPage, Results]
