from otree.api import *
import random
import time


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'stock_game'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    #stock_price = models.IntegerField()


class Subsession(BaseSubsession):
    pass



class Group(BaseGroup):
    pass
    #start_timestamp = models.IntegerField()


class Player(BasePlayer):
    cash = models.CurrencyField(initial=3000)
    stock = models.IntegerField(initial=random.randint(0, 5))
    stock_price = models.CurrencyField(initial=random.randint(50, 200))

    def total_assets(self):
        return self.cash + self.stock_price * self.stock

    
    def buy_stock(self):
        if self.cash >= self.stock_price:
            self.stock += 1
            self.cash -= self.stock_price
            total = self.cash + self.stock_price * self.stock
        return [self.cash, self.stock, total]

    def sell_stock(self):
        if self.stock > 0:
            self.stock -= 1
            self.cash += self.stock_price
            total = self.cash + self.stock_price * self.stock
        return [self.cash, self.stock, total]
    




class MyPage(Page):
    pass
    #form_model = 'player'

class Trading(Page):
    timeout_seconds = 10

    @staticmethod

    def before_next_page(player: Player, timeout_happened):
        player.stock_price = random.randint(900, 1000)

    def live_method(player: Player, data):
        if data['action'] == 'buy':
            Player.cash = player.buy_stock()[0]
            Player.stock = player.buy_stock()[1]
            #return { 'cash': player.buy_stock()[0], 'stock': player.buy_stock()[1], 'stock_price': player.stock_price }
        elif data['action'] == 'sell':
            Player.cash = player.sell_stock()[0]
            Player.stock = player.sell_stock()[1]
            #return { 'cash': player.sell_stock()[0], 'stock': player.sell_stock()[1], 'stock_price': player.stock_price }
        return [Player.cash, Player.stock, Player.stock_price]

class Trading2(Page):
    timeout_seconds = 10

    @staticmethod

    def before_next_page(player: Player, timeout_happened):
        player.stock_price = random.randint(1, 30)

    def live_method(player: Player, data):
        if data['action'] == 'buy':
            return { 'cash': player.buy_stock()[0], 'stock': player.buy_stock()[1], 'stock_price': player.stock_price }
        elif data['action'] == 'sell':
            return { 'cash': player.sell_stock()[0], 'stock': player.sell_stock()[1], 'stock_price': player.stock_price }
    

class Trading3(Page):
    timeout_seconds = 10

    @staticmethod

    def before_next_page(player: Player, timeout_happened):
        player.stock_price = random.randint(900, 1000)

    def live_method(player: Player, data):
        if data['action'] == 'buy':
            return { 'cash': player.buy_stock()[0], 'stock': player.buy_stock()[1], 'stock_price': player.stock_price }
        elif data['action'] == 'sell':
            return { 'cash': player.sell_stock()[0], 'stock': player.sell_stock()[1], 'stock_price': player.stock_price }
    


page_sequence = [Trading, Trading2, Trading3]




class Results(Page):
    pass


page_sequence = [MyPage, Trading, Trading2, Trading3, Results]
