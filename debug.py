import minqlx
import builtins
import random

class debug(minqlx.Plugin):
    
    def __init__(self):
        self.add_command("exec", self._exec)
        
    def _exec(self, player, msg, channel):
        _a = ""
        _b = ""
        for i in msg[1:]:
            _a = _a + i + " "
        for i in _a:
            if i == "\"":
                _b = _b + i
            else:
                _b = _b + i
        player.tell("Executing: " + _b)
        builtins.exec("player.tell(" + _b + ")")