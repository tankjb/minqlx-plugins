import minqlx
import os
import filecmp

class test1(minqlx.Plugin):
    
    def __init__(self):
        super()
        self.updateUrl = "https://raw.githubusercontent.com/tankjb/minqlx-plugins/master/test1.py"
        self.plugindir = os.path.dirname(os.path.realpath(__file__))
        self.updateAvailable = False
        self.add_command("reloadtest", self._reloadtest)
        self.add_hook("game_start", self._checkUpdate)
        self.add_command("checkupdate", self._manuallyCheckUpdate)
    
    def _reloadtest(self, player, msg, channel):
        player.tell("reloading")
        minqlx.reload_plugin("test1")
        player.tell("go")
        
    def _checkUpdate(self, *args, **kwargs):
        if self.updateAvailable == True:
            self._rewriteSelf()
            return
        self.getUpdate()
        
    def _manuallyCheckUpdate(self, player, msg, channel):       
        if self.updateAvailable == True:
            self._rewriteSelf()
            return
        self.getUpdate()    
        
    @minqlx.thread
    def getUpdate(self):
        os.system("mkdir " + self.plugindir + "/.temp/")
        os.system("wget " + self.updateUrl + " -P " + self.plugindir + "/.temp/")
        changed = filecmp.cmp(self.plugindir + "/test1.py",
                              self.plugindir + "/.temp/" + "test1.py",
                              shallow = False)
        self.updateAvailable = not changed
        if self.updateAvailable:
            minqlx.CHAT_CHANNEL.reply("test1: New update available.")
        else:
            minqlx.CHAT_CHANNEL.reply("test1: Plugin is up to date.")
        return
    
    @minqlx.thread
    def _rewriteSelf(self):
        os.system("mv " + self.plugindir + "/.temp/" + "test1.py" + " " + self.plugindir)
        os.system("rm -rf " + self.plugindir + "/.temp/")
        self.updateAvailable = False
        minqlx.CHAT_CHANNEL.reply("test1: Plugin has been successfully updated.")
        minqlx.reload_plugin("test1")
        return