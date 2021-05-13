import minqlx
class test1(minqlx.Plugin):
    
    def __init__(self):
        super()
        self.add_command("reloadtest", self._reloadtest)
    
    def _reloadtest(self, player, msg, channel):
        player.tell("reloading")
        minqlx.reload_plugin("test1")
        player.tell("go")