from otree.api import *
import random

class Constants(BaseConstants):
    name_in_url = 'Task1'
    players_per_group = 20
    num_rounds = 1


class Subsession(BaseSubsession):
    #ここはrandom一覧
    def creating_session(self):
            return [random.randint(1,10),random.randint(10,100),random.randint(100,1000),random.randint(1000,10000)]


class Group(BaseGroup):
    pass

class Player(BasePlayer):

#ここはタスクに対する入力値一覧
    taskA_b = models.CurrencyField(
        min=0, doc="The amount for taskA beforehand"
    )

    taskA_a = models.CurrencyField(
        min=0, doc="The amount for taskA afterhand"
    )


#ここはLegoチョイスの入力値一覧

    Lego_best = models.IntegerField(
        choices = [[1,'①'],[2,'②'],[3,'③'] ]
    )


#ここはroleの配分の入力値一覧
    def role(self):
        if self.id_in_group in range(1,3):
            return "4-1"
        elif self.id_in_group in range(3,7):
            return "4-2"
        elif self.id_in_group in range(7,11):
            return "4-3"
        else: 
            return "4-4"

#ここはtask用


    taskA_01 = models.IntegerField()
    taskA_02 = models.IntegerField()
    taskA_03 = models.IntegerField()
    taskA_04 = models.IntegerField()
    taskA_05 = models.IntegerField()
    taskA_06 = models.IntegerField()
    taskA_07 = models.IntegerField()
    taskA_08 = models.IntegerField()
    taskA_09 = models.IntegerField()
    taskA_10 = models.IntegerField()
    taskA_11 = models.IntegerField()
    taskA_12 = models.IntegerField()
 

        

    #Session B
     #random関数
    randomB1 = models.IntegerField()
    randomB2 = models.IntegerField()
    randomB3 = models.IntegerField()
    randomB4 = models.IntegerField()

    #ここはtaskの適正価格の入力箇所        
    taskB_1 = models.CurrencyField()
    taskB_2 = models.CurrencyField()
    taskB_3 = models.CurrencyField()
    taskB_4 = models.CurrencyField()
    
    #ここはflagの位置
    flagB1 = models.IntegerField(initial=0)
    flagB2 = models.IntegerField(initial=0)
    flagB3 = models.IntegerField(initial=0)
    flagB4 = models.IntegerField(initial=0)




    #ここはtask用
    taskB1_01 = models.IntegerField()
    taskB1_02 = models.IntegerField()
    taskB1_03 = models.IntegerField()
    taskB1_04 = models.IntegerField()
    taskB1_05 = models.IntegerField()
    taskB1_06 = models.IntegerField()
    taskB1_07 = models.IntegerField()
    taskB1_08 = models.IntegerField()
    taskB1_09 = models.IntegerField()
    taskB1_10 = models.IntegerField()
    taskB1_11 = models.IntegerField()
    taskB1_12 = models.IntegerField()


    taskB2_01 = models.IntegerField()
    taskB2_02 = models.IntegerField()
    taskB2_03 = models.IntegerField()
    taskB2_04 = models.IntegerField()
    taskB2_05 = models.IntegerField()
    taskB2_06 = models.IntegerField()
    taskB2_07 = models.IntegerField()
    taskB2_08 = models.IntegerField()
    taskB2_09 = models.IntegerField()
    taskB2_10 = models.IntegerField()
    taskB2_11 = models.IntegerField()
    taskB2_12 = models.IntegerField()
   

    taskB3_01 = models.IntegerField()
    taskB3_02 = models.IntegerField()
    taskB3_03 = models.IntegerField()
    taskB3_04 = models.IntegerField()
    taskB3_05 = models.IntegerField()
    taskB3_06 = models.IntegerField()
    taskB3_07 = models.IntegerField()
    taskB3_08 = models.IntegerField()
    taskB3_09 = models.IntegerField()
    taskB3_10 = models.IntegerField()
    taskB3_11 = models.IntegerField()
    taskB3_12 = models.IntegerField()


    taskB4_01 = models.IntegerField()
    taskB4_02 = models.IntegerField()
    taskB4_03 = models.IntegerField()
    taskB4_04 = models.IntegerField()
    taskB4_05 = models.IntegerField()
    taskB4_06 = models.IntegerField()
    taskB4_07 = models.IntegerField()
    taskB4_08 = models.IntegerField()
    taskB4_09 = models.IntegerField()
    taskB4_10 = models.IntegerField()
    taskB4_11 = models.IntegerField()
    taskB4_12 = models.IntegerField()
 

    #ここはtask答え用
    def taskB1_01_error_message (self, value):
        if value != 913803255579807742:
            return "wrong number"
    def taskB1_02_error_message (self, value):
        if value != 577202586672698283:
            return "wrong number"
    def taskB1_03_error_message (self, value):
        if value != 529765794565389500:
            return "wrong number"
    def taskB1_04_error_message (self, value):
        if value != 947858029695445204:
            return "wrong number"    
    def taskB1_05_error_message (self, value):
        if value != 339484812456860452:
            return "wrong number"
    def taskB1_06_error_message (self, value):
        if value != 834595928466342928:
            return "wrong number"
    def taskB1_07_error_message (self, value):
        if value != 120319568634463957:
            return "wrong number"
    def taskB1_08_error_message (self, value):
        if value != 250654525059565714:
            return "wrong number"
    def taskB1_09_error_message (self, value):
        if value != 167403721239359872:
            return "wrong number"
    def taskB1_10_error_message (self, value):
        if value != 996783923204035553:
            return "wrong number"
    def taskB1_11_error_message (self, value):
        if value != 477655728589305665:
            return "wrong number"
    def taskB1_12_error_message (self, value):
        if value != 708086360463123393:
            return "wrong number"


    def taskB2_01_error_message (self, value):
        if value != 913803255579807742:
            return "wrong number"
    def taskB2_02_error_message (self, value):
        if value != 577202586672698283:
            return "wrong number"
    def taskB2_03_error_message (self, value):
        if value != 529765794565389500:
            return "wrong number"
    def taskB2_04_error_message (self, value):
        if value != 947858029695445204:
            return "wrong number"    
    def taskB2_05_error_message (self, value):
        if value != 339484812456860452:
            return "wrong number"
    def taskB2_06_error_message (self, value):
        if value != 834595928466342928:
            return "wrong number"
    def taskB2_07_error_message (self, value):
        if value != 120319568634463957:
            return "wrong number"
    def taskB2_08_error_message (self, value):
        if value != 250654525059565714:
            return "wrong number"
    def taskB2_09_error_message (self, value):
        if value != 167403721239359872:
            return "wrong number"
    def taskB2_10_error_message (self, value):
        if value != 996783923204035553:
            return "wrong number"
    def taskB2_11_error_message (self, value):
        if value != 477655728589305665:
            return "wrong number"
    def taskB2_12_error_message (self, value):
        if value != 708086360463123393:
            return "wrong number"


    def taskB3_01_error_message (self, value):
        if value != 913803255579807742:
            return "wrong number"
    def taskB3_02_error_message (self, value):
        if value != 577202586672698283:
            return "wrong number"
    def taskB3_03_error_message (self, value):
        if value != 529765794565389500:
            return "wrong number"
    def taskB3_04_error_message (self, value):
        if value != 947858029695445204:
            return "wrong number"    
    def taskB3_05_error_message (self, value):
        if value != 339484812456860452:
            return "wrong number"
    def taskB3_06_error_message (self, value):
        if value != 834595928466342928:
            return "wrong number"
    def taskB3_07_error_message (self, value):
        if value != 120319568634463957:
            return "wrong number"
    def taskB3_08_error_message (self, value):
        if value != 250654525059565714:
            return "wrong number"
    def taskB3_09_error_message (self, value):
        if value != 167403721239359872:
            return "wrong number"
    def taskB3_10_error_message (self, value):
        if value != 996783923204035553:
            return "wrong number"
    def taskB3_11_error_message (self, value):
        if value != 477655728589305665:
            return "wrong number"
    def taskB3_12_error_message (self, value):
        if value != 708086360463123393:
            return "wrong number"


    def taskB4_01_error_message (self, value):
        if value != 913803255579807742:
            return "wrong number"
    def taskB4_02_error_message (self, value):
        if value != 577202586672698283:
            return "wrong number"
    def taskB4_03_error_message (self, value):
        if value != 529765794565389500:
            return "wrong number"
    def taskB4_04_error_message (self, value):
        if value != 947858029695445204:
            return "wrong number"    
    def taskB4_05_error_message (self, value):
        if value != 339484812456860452:
            return "wrong number"
    def taskB4_06_error_message (self, value):
        if value != 834595928466342928:
            return "wrong number"
    def taskB4_07_error_message (self, value):
        if value != 120319568634463957:
            return "wrong number"
    def taskB4_08_error_message (self, value):
        if value != 250654525059565714:
            return "wrong number"
    def taskB4_09_error_message (self, value):
        if value != 167403721239359872:
            return "wrong number"
    def taskB4_10_error_message (self, value):
        if value != 996783923204035553:
            return "wrong number"
    def taskB4_11_error_message (self, value):
        if value != 477655728589305665:
            return "wrong number"
    def taskB4_12_error_message (self, value):
        if value != 708086360463123393:
            return "wrong number"


   
    pass





class A_Start(Page):
    pass

class B_readA(Page):
    pass

class C_priceA_before(Page):
    form_model = "player"
    form_fields = ["taskA_b"]

class D_taskA_start(Page):
    pass

class E_taskA(Page):
    form_model = "player"
    form_fields = ["taskA_01",
                  "taskA_02","taskA_03","taskA_04","taskA_05","taskA_06","taskA_07","taskA_08","taskA_09","taskA_10","taskA_11","taskA_12"
                   ]
    
    def error_message (player, value):
        if value["taskA_01"] != 379724543383292695:
            return "wrong number"

        if value["taskA_02"] != 226718295449262751:
            return "wrong number"

        if value["taskA_03"] != 242266448881093273:
            return "wrong number"

        if value["taskA_04"] != 132695584000430865:
            return "wrong number"    

        if value["taskA_05"] != 824728598221715870:
            return "wrong number"

        if value["taskA_06"] != 126680328239918111:
            return "wrong number"

        if value["taskA_07"] != 106883929245500099:
            return "wrong number"

        if value["taskA_08"] != 451930072293005153:
            return "wrong number"

        if value["taskA_09"] != 287170445483048289:
            return "wrong number"

        if value["taskA_10"] != 771086863250917357:
            return "wrong number"

        if value["taskA_11"] != 552071453489277446:
            return "wrong number"

        if value["taskA_12"] != 755436812386619961:
            return "wrong number"


class F_priceA_after(Page):
    form_model = "player"
    form_fields = ["taskA_a"]

class H_lego_choose(Page):
    form_model = "player"
    form_fields = ["Lego_best"]

class I_manual(Page):
    def before_next_page(self, timeout_happened):
        self.participant.vars['Lego_best'] = self.Lego_best


    
class Lego_1_1(Page):
    pass

class Lego_1_2(Page):
    pass


#分岐点1 
class taskB_1(Page):
    form_model = "player"
    form_fields = ["taskB_1"]

    def before_next_page(self, timeout_happened):
        self.flagB1 = 1
        self.randomB1 = random.randint(100,1000)
    def is_displayed(self):
        return self.role() == "4-1" 
    pass

class taskB_tell_1(Page):
    def is_displayed(self):
        return self.flagB1 == 1 and self.role() == "4-1" 
    def before_next_page(self, timeout_happened):
        if self.taskB_1 <= self.randomB1:
            self.flagB1 = 2
    

class taskB_do_1(Page):
    form_model = "player"
    form_fields = ["taskB1_01",
                   "taskB1_02","taskB1_03","taskB1_04","taskB1_05","taskB1_06","taskB1_07","taskB1_08","taskB1_09","taskB1_10","taskB1_11","taskB1_12"
                   ]
    
    def error_message (player, value):
        if value["taskB1_01"] != 913803255579807742:
            return "wrong number"

        if value["taskB1_02"] != 577202586672698283:
            return "wrong number"

        if value["taskB1_03"] != 529765794565389500:
            return "wrong number"

        if value["taskB1_04"] != 947858029695445204:
            return "wrong number"    

        if value["taskB1_05"] != 339484812456860452:
            return "wrong number"

        if value["taskB1_06"] != 834595928466342928:
            return "wrong number"

        if value["taskB1_07"] != 120319568634463957:
            return "wrong number"

        if value["taskB1_08"] != 250654525059565714:
            return "wrong number"

        if value["taskB1_09"] != 167403721239359872:
            return "wrong number"

        if value["taskB1_10"] != 996783923204035553:
            return "wrong number"

        if value["taskB1_11"] != 477655728589305665:
            return "wrong number"

        if value["taskB1_12"] != 708086360463123393:
            return "wrong number"

    def is_displayed(self):
        return self.flagB1 == 2 and self.role() == "4-1" 



   
class Lego_2_1(Page):
    def is_displayed(self):
        return self.flagB1 != 2

class Lego_2_2(Page):
    def is_displayed(self):
        return self.flagB1 != 2

class Lego_2_3(Page):
    def is_displayed(self):
        return self.flagB1 != 2

    
#分岐点2
class taskB_2(Page):
    form_model = "player"
    form_fields = ["taskB_2"]

    def before_next_page(self, timeout_happened):
        self.flagB2 = 1
        self.randomB2 = random.randint(100,1000)
    def is_displayed(self):
        return self.role() == "4-2" 

class taskB_tell_2(Page):
    def is_displayed(self):
        return self.flagB2 == 1 and self.role() == "4-2" 
    def before_next_page(self, timeout_happened):
        if self.taskB_2 <= self.randomB2:
            self.flagB2 = 2
    

class taskB_do_2(Page):
    form_model = "player"
    form_fields = ["taskB2_01",
                   "taskB2_02","taskB2_03","taskB2_04","taskB2_05","taskB2_06","taskB2_07","taskB2_08","taskB2_09","taskB2_10","taskB2_11","taskB2_12"
                   ]
    
    def error_message (player, value):
        if value["taskB2_01"] != 913803255579807742:
            return "wrong number"

        if value["taskB2_02"] != 577202586672698283:
            return "wrong number"

        if value["taskB3_03"] != 529765794565389500:
            return "wrong number"

        if value["taskB4_04"] != 947858029695445204:
            return "wrong number"    

        if value["taskB5_05"] != 339484812456860452:
            return "wrong number"

        if value["taskB6_06"] != 834595928466342928:
            return "wrong number"

        if value["taskB7_07"] != 120319568634463957:
            return "wrong number"

        if value["taskB8_08"] != 250654525059565714:
            return "wrong number"

        if value["taskB9_09"] != 167403721239359872:
            return "wrong number"

        if value["taskB10_10"] != 996783923204035553:
            return "wrong number"

        if value["taskB11_11"] != 477655728589305665:
            return "wrong number"

        if value["taskB12_12"] != 708086360463123393:
            return "wrong number"

    def is_displayed(self):
        return self.flagB2 == 2 and self.role() == "4-2" 




class Lego_3_1(Page):
    def is_displayed(self):
        return self.flagB1 != 2 and self.flagB2 != 2

class Lego_3_2(Page):
    def is_displayed(self):
        return self.flagB1 != 2 and self.flagB2 != 2



#分岐点3
class taskB_3(Page):
    form_model = "player"
    form_fields = ["taskB_3"]

    def before_next_page(self, timeout_happened):
        self.flagB3 = 1
        self.randomB3 = random.randint(100,1000)
    def is_displayed(self):
        return self.role() == "4-3" 

class taskB_tell_3(Page):
    def is_displayed(self):
        return self.flagB3 == 1 and self.role() == "4-3" 
    def before_next_page(self,timeout_happened):
        if self.taskB_3 <= self.randomB3:
            self.flagB3 = 2
    

class taskB_do_3(Page):
    form_model = "player"
    form_fields = ["taskB3_01","taskB3_02","taskB3_03","taskB3_04","taskB3_05","taskB3_06","taskB3_07","taskB3_08","taskB3_09","taskB3_10","taskB3_11","taskB3_12"]

    def error_message (player, value):
        if value["taskB3_01"] != 913803255579807742:
            return "wrong number"

        if value["taskB3_02"] != 577202586672698283:
            return "wrong number"

        if value["taskB3_03"] != 529765794565389500:
            return "wrong number"

        if value["taskB3_04"] != 947858029695445204:
            return "wrong number"    

        if value["taskB3_05"] != 339484812456860452:
            return "wrong number"

        if value["taskB3_06"] != 834595928466342928:
            return "wrong number"

        if value["taskB3_07"] != 120319568634463957:
            return "wrong number"

        if value["taskB3_08"] != 250654525059565714:
            return "wrong number"

        if value["taskB3_09"] != 167403721239359872:
            return "wrong number"

        if value["taskB3_10"] != 996783923204035553:
            return "wrong number"

        if value["taskB3_11"] != 477655728589305665:
            return "wrong number"

        if value["taskB3_12"] != 708086360463123393:
            return "wrong number"

    def is_displayed(self):
        return self.flagB3 == 2 and self.role() == "4-3" 




class Lego_4_1(Page):
    def is_displayed(self):
        return self.flagB1 != 2 and self.flagB2 != 2 and self.flagB3 !=2
class Lego_4_2(Page):
    def is_displayed(self):
        return self.flagB1 != 2 and self.flagB2 != 2 and self.flagB3 !=2





#分岐点4
class taskB_4(Page):
    form_model = "player"
    form_fields = ["taskB_4"]

    def is_displayed(self):
        return self.role()=="4-4"

    def before_next_page(self,timeout_happened):
        self.flagB4 = 1
        self.randomB4 = random.randint(100,1000)


class taskB_tell_4(Page):
    def is_displayed(self):
        return self.flagB4 == 1 and self.role()=="4-4"
    def before_next_page(self,timeout_happened):
        if self.taskB_4 <= self.randomB4:
            self.flagB4 = 2
    

class taskB_do_4(Page):
    form_model = "player"
    form_fields = ["taskB4_01","taskB4_02","taskB4_03","taskB4_04","taskB4_05","taskB4_06","taskB4_07","taskB4_08","taskB4_09","taskB4_10","taskB4_11","taskB4_12"]

    def error_message (player, value):
        if value["taskB4_01"] != 913803255579807742:
            return "wrong number"

        if value["taskB4_02"] != 577202586672698283:
            return "wrong number"

        if value["taskB4_03"] != 529765794565389500:
            return "wrong number"

        if value["taskB4_04"] != 947858029695445204:
            return "wrong number"    

        if value["taskB4_05"] != 339484812456860452:
            return "wrong number"

        if value["taskB4_06"] != 834595928466342928:
            return "wrong number"

        if value["taskB4_07"] != 120319568634463957:
            return "wrong number"

        if value["taskB4_08"] != 250654525059565714:
            return "wrong number"

        if value["taskB4_09"] != 167403721239359872:
            return "wrong number"

        if value["taskB4_10"] != 996783923204035553:
            return "wrong number"

        if value["taskB4_11"] != 477655728589305665:
            return "wrong number"

        if value["taskB4_12"] != 708086360463123393:
            return "wrong number"

    def is_displayed(self):
        return self.flagB4 == 2 and self.role()=="4-4"





class Lego_5_1(Page):
    def is_displayed(self):
        return self.flagB1 != 2 and self.flagB2 != 2 and self.flagB3 !=2 and self.flagB4 !=2



class Last(Page):
    pass



page_sequence = [A_Start,B_readA, C_priceA_before, D_taskA_start, E_taskA,F_priceA_after, H_lego_choose, I_manual,
                Lego_1_1,Lego_1_2,taskB_1,taskB_tell_1,taskB_do_1,
                Lego_2_1,Lego_2_2,Lego_2_3,taskB_2,taskB_tell_2,taskB_do_2,
                Lego_3_1,Lego_3_2,taskB_3,taskB_tell_3,taskB_do_3,
                Lego_4_1,Lego_4_2,taskB_4,taskB_tell_4,taskB_do_4,
                Lego_5_1,Last]
