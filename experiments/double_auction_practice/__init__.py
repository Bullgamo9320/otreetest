from otree.api import *
import time
import random


doc = "Double auction market"


class C(BaseConstants):
    NAME_IN_URL = 'double_auction_practice'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    ITEMS_PER_SELLER = 3
    VALUATION_MIN = cu(50)
    VALUATION_MAX = cu(110)
    PRODUCTION_COSTS_MIN = cu(10)
    PRODUCTION_COSTS_MAX = cu(80)


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    players = subsession.get_players()
    for p in players:
        # this means if the player's ID is not a multiple of 2, they are a buyer.
        # for more buyers, change the 2 to 3
        #ランダムに振られるplayerのidでbuyerかsellerを決定する
        p.is_buyer = p.id_in_group % 2 > 0
        if p.is_buyer:
            p.num_items = 0
            p.break_even_point = random.randint(C.VALUATION_MIN, C.VALUATION_MAX)
            p.current_offer = 0
        else:
            p.num_items = C.ITEMS_PER_SELLER
            p.break_even_point = random.randint(
                C.PRODUCTION_COSTS_MIN, C.PRODUCTION_COSTS_MAX
            )
            p.current_offer = C.VALUATION_MAX + 1


class Group(BaseGroup):
    start_timestamp = models.IntegerField()


class Player(BasePlayer):
    is_buyer = models.BooleanField()
    current_offer = models.CurrencyField()# 0もしくはC.VALUATION_MAX + 1を初期値として、その値だと表示されない。
    break_even_point = models.CurrencyField()# その人にとっての財の価値
    num_items = models.IntegerField()


class Transaction(ExtraModel):
    # 
    # live pageで使うExtraModelを用いる。
    # 他の変数はページ遷移ごとに保存されるが、こちらは(多分)ページ遷移無しで一時的に変数を保存するときに使う。
    # https://otree.readthedocs.io/ja/latest/misc/advanced.html
    # 他のモデルを用いて定義する必要がある。GroupやPlayerと紐付けるときはLink関数を使う
    group = models.Link(Group)
    buyer = models.Link(Player)
    #(問題)Player クラスと紐付いたsellerモデルを作成する
    seller = ;
    seconds = models.IntegerField(doc="Timestamp (seconds since beginning of trading)")
    #(問題)CurrencyFieldで定義したpriceを定義する
    price = ;

# offerに対して、取引が成立したbuyerとsellerがいたら返す。
#(問題)取引成立の条件式を記入する。
def find_match(buyers, sellers):
    for buyer in buyers:
        for seller in sellers:
            if :
                # return as soon as we find a match (the rest of the loop will be skipped)
                return [buyer, seller]

# javascriptからデータを受信したときに動くlive_methodを定義しておく。
# 引数はplayerとdataと書くらしい
def live_method(player: Player, data):
    group = player.group
    players = group.get_players()
    buyers = [p for p in players if p.is_buyer]
    sellers = [p for p in players if not p.is_buyer]
    news = None

    if data:
        offer = int(data['offer'])
        player.current_offer = offer
        if player.is_buyer:
            match = find_match(buyers=[player], sellers=sellers)
        else:
            match = find_match(buyers=buyers, sellers=[player])
        if match:
            [buyer, seller] = match
            price = buyer.current_offer
            Transaction.create(
                group=group,
                buyer=buyer,
                seller=seller,
                price=price,
                seconds=int(time.time() - group.start_timestamp),
            )
            #取引成立に伴い各変数の変更
            #(問題)適宜埋める
            buyer.num_items = buyer.num_items + 1
            seller.num_items = ;
            buyer.payoff += buyer.break_even_point - price
            seller.payoff += ;
            buyer.current_offer = ;#表示されないように初期値に戻す
            seller.current_offer = ;#表示されないように初期値に戻す
            news = dict(buyer=buyer.id_in_group, seller=seller.id_in_group, price=price)

    bids = sorted([p.current_offer for p in buyers if p.current_offer > 0], reverse=True)
    asks = sorted([p.current_offer for p in sellers if p.current_offer <= C.VALUATION_MAX])
    highcharts_series = [[tx.seconds, tx.price] for tx in Transaction.filter(group=group)]

    return {
        p.id_in_group: dict(
            num_items=p.num_items,
            current_offer=p.current_offer,
            payoff=p.payoff,
            bids=bids,
            asks=asks,
            highcharts_series=highcharts_series,
            news=news,
        )
        for p in players
    }


# PAGES
class WaitToStart(WaitPage):
    @staticmethod
    def after_all_players_arrive(group: Group):
        group.start_timestamp = int(time.time())


class Trading(Page):
    live_method = live_method

    @staticmethod
    #(問題)is_buyerも取ってこれるようにする
    def js_vars(player: Player):
        return dict(id_in_group=player.id_in_group, )#ここに記入

    @staticmethod
    def get_timeout_seconds(player: Player):
        import time

        group = player.group
        return (group.start_timestamp + 2 * 60) - time.time()


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [WaitToStart, Trading, ResultsWaitPage, Results]
