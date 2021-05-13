# author: tankjb
# randomly add battlesuit to players when round start in CA mode

import minqlx
import random
class ca_battlesuit(minqlx.Plugin):  
    
    def __init__(self):
        self.manualdisable = False
        self.add_hook("game_countdown", self.givehint)
        self.add_hook("round_start", self.add_battlesuit)
        self.add_hook("round_countdown", self.decide_battlesuit, priority = minqlx.PRI_LOWEST)
        
    def givehint(self, *args, **kwargs):
        minqlx.CHAT_CHANNEL.reply("CABS has been enabled!")
        minqlx.CHAT_CHANNEL.reply("The battlesuit will be given to one player per side randomly.")
    
    @minqlx.delay(3)
    def decide_battlesuit(self, *args, **kwargs):
        if len(self.teams()["red"]) < 1 or len(self.teams()["blue"]) < 1:
            self.disable = True
            minqlx.CHAT_CHANNEL.reply("No enough players, there won't be any battlesuits!")
            return minqlx.RET_STOP_ALL
        else:
            self.disable = False
        self.redPlayer = random.choice(self.teams()["red"])._id
        self.bluePlayer = random.choice(self.teams()["blue"])._id
        minqlx.CHAT_CHANNEL.reply("The battlesuits will given to " + \
                                  self.player(self.redPlayer).name \
                                  + " and " + self.player(self.bluePlayer).name \
                                  + " this round!")
        
    def add_battlesuit(self, *args, **kwargs):
        if self.disable == True:
            return minqlx.RET_STOP_ALL
        self.player(self.redPlayer).powerups(reset = True, battlesuit = 10)
        self.player(self.bluePlayer).powerups(reset = True, battlesuit = 10)
        self.redPlayer = None
        self.bluePlayer = None        
        